sudo docker run \
-e KEY='$GODADDY_KEY' \
-e SECRET='GODADDY_SECRET' \
-e TTL='600' \
-e DOMAINS='subdomain|domain.com,subdomain2|domain.com' \
-e RENEW_TIME='600' \
gdy



    godaddy_ddns:
      image: dimagoltsman/godaddy-ddns-multipudater
      container_name: godaddy_ddns
      environment:
        - KEY=${GODADDY_KEY}
        - SECRET=${GODADDY_SECRET}
        - TTL=600
        - DOMAINS=subdomain|domain.com,subdomain2|domain.com
        - RENEW_TIME=600