#!/bin/bash

echo "======================="
echo "Atualizando Servidor"

apt-get update
apt-get upgrade -y

echo "======================="
echo "Instalando pacotes"

apt-get install apache2 -y
apt-get install unzip -y

echo "======================="
echo "Baixando projeto"

cd /tmp
wget https://github.com/denilsonbonatti/linux-site-dio/archive/refs/heads/main.zip

echo "======================="
echo "Copiando o arquivo para o diretório da aplicação web"

unzip main.zip
cp -r linux-site-dio-main/* /var/www/html/

