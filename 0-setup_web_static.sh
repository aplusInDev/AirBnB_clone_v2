#!/usr/bin/env bash
# sets up the web servers for the deployment of web_static

trap 'exit 0' ERR

if ! command -v nginx &> /dev/null; then
    sudo apt update
    sudo apt install nginx -y
fi
sudo mkdir -p "/data/web_static/releases/test/"
sudo mkdir -p "/data/web_static/shared/"
sudo touch /data/web_static/releases/test/index.html
sudo echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
sudo rm -rf /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-enabled/default
sudo service nginx restart
