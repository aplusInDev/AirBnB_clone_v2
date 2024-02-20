#!/usr/bin/env bash
# sets up the web servers for the deployment of web_static

if ! command -v nginx &> /dev/null; then
    sudo apt update
    sudo apt install nginx -y
fi
sudo mkdir -p "/data/web_static/releases/test/"
sudo mkdir -p "/data/web_static/shared/"
sudo touch /data/web_static/releases/test/index.html
sudo echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
oldstr="location / {"
newstr="location /hbnb_static {\n\talias /data/web_static/current/;\n    }\n\n    $oldstr"
sudo sed -i -z "s|$oldstr|$newstr|" /etc/nginx/sites-enabled/default
newstr="location =/hbnb_static {\n\talias /data/web_static/current/index.html;\n    }\n\n    $oldstr"
sudo sed -i -z "s|$oldstr|$newstr|" /etc/nginx/sites-enabled/default
sudo service nginx restart
