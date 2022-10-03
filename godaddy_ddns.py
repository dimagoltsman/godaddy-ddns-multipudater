import requests
import re
import os
import time
from loguru import logger
import traceback

KEY=os.getenv('KEY')
SECRET=os.getenv('SECRET')
TTL=int(os.getenv('TTL'))
DOMAINS=os.getenv('DOMAINS')
RENEW_TIME=int(os.getenv('RENEW_TIME'))


def main():
    while True:
        try:
            do_renew()
        except:
            tb = traceback.format_exc()
            logger.error(tb)
        time.sleep(RENEW_TIME)

def do_renew():
    logger.info("trying renew")
    
    current_machine_ip=get_external_ip()
    logger.info(f'external ip: {current_machine_ip}')
    
    domains_arr = DOMAINS.split(",")
    
    for domain_entry in domains_arr:
        raw = domain_entry.split("|")
        subd = raw[0]
        fulld = raw[1]
    
        info = requests.get(f'https://api.godaddy.com/v1/domains/{fulld}/records/A/{subd}', headers = {"Authorization": f"sso-key {KEY}:{SECRET}"}).json()
        # [{'data': '1.1.1.1', 'name': 'test', 'ttl': 600, 'type': 'A'}]
        current_ip_in_gd = info[0]['data']
        ttl_in_gd = info[0]['ttl']
        
        logger.info(f'ip of {subd}.{fulld} in godaddy is set to: {current_ip_in_gd} TTL: {TTL}')
    
        if current_ip_in_gd != current_machine_ip or ttl_in_gd != TTL:
            logger.info(f'updating subdomain {subd} from {current_ip_in_gd} to {current_machine_ip}, TTL: {TTL}')
            data=[{
               "data": current_machine_ip,
               "port": 65535,
               "priority": 0,
               "protocol": "",
               "service": "",
               "ttl": TTL,
               "weight": 0
             }]
            res=requests.put(
                f'https://api.godaddy.com/v1/domains/{fulld}/records/A/{subd}',
                headers={"Authorization": f"sso-key {KEY}:{SECRET}"},
                json=data
                )
    
    
    
def get_external_ip():
    return requests.get('https://ipv4.icanhazip.com/').content.decode("utf-8").strip()
    


if __name__ == "__main__":
    main()