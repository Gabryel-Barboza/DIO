#!/bin/bash

echo "Removendo diretórios"
rm -r /publico /adm /ven /sec

echo "Removendo usuários criados"
userdel -rf carlos
userdel -rf maria
userdel -rf joao
userdel -rf debora
userdel -rf sebastiana
userdel -rf roberto
userdel -rf josefina
userdel -rf amanda
userdel -rf rogerio

echo "Removendo grupos criados"
groupdel GRP_ADM
groupdel GRP_VEN
groupdel GRP_SEC
