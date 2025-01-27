#!/bin/bash

echo "Criando diretórios de departamento"
mkdir /publico /adm /ven /sec

echo "Criando grupos"
groupadd GRP_ADM
groupadd GRP_VEN
groupadd GRP_SEC

echo "Criando usuários e expirando senhas"
useradd carlos -ms /bin/bash -c "Carlos Barbosa" -p $(openssl passwd senha123)
passwd -e carlos
useradd maria -ms /bin/bash -c "Maria Gonçalves" -p $(openssl passwd senha123)
passwd -e maria
useradd joao -ms /bin/bash -c "João da Silva" -p $(openssl passwd senha123)
passwd -e joao
useradd debora -ms /bin/bash -c "Débora Lima" -p $(openssl passwd senha123)
passwd -e debora
useradd sebastiana -ms /bin/bash -c "Sebastiana de Souza" -p $(openssl passwd senha123)
passwd -e sebastiana
useradd roberto -ms /bin/bash -c "Roberto Nonato" -p $(openssl passwd senha123)
passwd -e roberto
useradd josefina -ms /bin/bash -c "Josefina Barbosa" -p $(openssl passwd senha123)
passwd -e josefina
useradd amanda -ms /bin/bash -c "Amanda Nunes" -p $(openssl passwd senha123)
passwd -e amanda
useradd rogerio -ms /bin/bash -c "Rogério Silva" -p $(openssl passwd senha123)
passwd -e rogerio

echo "Adicionando usuários aos grupos"
usermod -G GRP_ADM carlos
usermod -G GRP_ADM maria
usermod -G GRP_ADM joao
usermod -G GRP_VEN debora
usermod -G GRP_VEN sebastiana
usermod -G GRP_VEN roberto
usermod -G GRP_SEC josefina
usermod -G GRP_SEC amanda
usermod -G GRP_SEC rogerio

echo "Adicionando permissões de acesso dos diretórios"
chmod 777 /publico
chmod 770 /adm
chmod 770 /ven
chmod 770 /sec

echo "Alterando proprietário e grupo de diretórios"
chown root:GRP_ADM /adm
chown root:GRP_VEN /ven
chown root:GRP_SEC /sec
