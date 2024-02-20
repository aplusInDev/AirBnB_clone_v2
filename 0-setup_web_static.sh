#!/usr/bin/env bash
# sets up the web servers for the deployment of web_static

sudo apt update
sudo apt install nginx -y
sudo mkdir -p "/data/web_static/releases/test/"
sudo mkdir -p "/data/web_static/shared/"
sudo touch /data/web_static/releases/test/index.html
sudo echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
oldstr="location / {"
newstr="location /hbnb_static/ {\n\talias /data/web_static/current/;\n    }\n\n    $oldstr"
sudo sed -i -z "s|$oldstr|$newstr|" /etc/nginx/sites-enabled/aplusdev.tech
sudo nginx -t
sudo service nginx restart
