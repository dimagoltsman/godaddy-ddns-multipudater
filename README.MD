# Godaddy Ip Updater (like duckdns updater but for godaddy)

First you have to generate api key and secret in your godaddy account: https://developer.godaddy.com/keys  (make sure you generate a Production key)

Add subdomain with an A record and set it to any ip.

Run the docker.



Run simple docker:

        sudo docker run \
        -e KEY='$GODADDY_KEY' \
        -e SECRET='$GODADDY_SECRET' \
        -e TTL='600' \
        -e DOMAINS='subdomain|domain.com,subdomain2|domain.com' \
        -e RENEW_TIME='600' \
        dimagoltsman/godaddy-ddns-multipudater


Compose:

    godaddy_ddns:
      image: dimagoltsman/godaddy-ddns-multipudater
      container_name: godaddy_ddns
      environment:
        - KEY=${GODADDY_KEY}
        - SECRET=${GODADDY_SECRET}
        - TTL=600
        - DOMAINS=subdomain|domain.com,subdomain2|domain.com
        - RENEW_TIME=600


change to `dimagoltsman/godaddy-ddns-multipudater:arm64` for arm architecture
