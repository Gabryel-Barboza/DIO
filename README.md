# Repositório com o matérial do bootcamp da [Digital Innovation One](https://web.dio.me)
Estão inclusos os projetos feitos nos diretórios de desafios. <br>
Altere a **Branch** atual para alguma das opções disponíveis para visualizar outros cursos.

# Índice
1. [Aprendendo Comandos em Bash](https://github.com/Gabryel-Barboza/DIO/tree/Bash#aprendendo-comando-em-bash)
   * [Desafio IaC II](https://github.com/Gabryel-Barboza/DIO/tree/Bash#desafio-iac-ii)
3. [Fundamentos do Docker](https://github.com/Gabryel-Barboza/DIO/tree/Bash#fundamentos-do-docker)
   * [Docker Compose Apache Web](https://github.com/Gabryel-Barboza/DIO/tree/Bash#docker-compose-apache-web)
   * [Clusters Swarm Provisionados com Vagrant](https://github.com/Gabryel-Barboza/DIO/tree/Bash#clusters-swarm-provisionados-com-vagrant)

# Desafios
* [Infrastructure as Code I](https://github.com/Gabryel-Barboza/DIO/blob/Bash/Linux/Desafios/iac-1.sh)
* [Infrastructure as Code II](https://github.com/Gabryel-Barboza/DIO/blob/Bash/Linux/Desafios/iac-2.sh)
* [Apache App com Docker Compose](https://github.com/Gabryel-Barboza/DIO/tree/Bash/docker_fundamentals/Desafios/docker-compose-web-app)
* [Script de provisionamento com Vagrant](https://github.com/Gabryel-Barboza/DIO/tree/Bash/docker_fundamentals/Desafios/vagrant-vm-provision)

# Aprendendo Comandos em Bash
Iniciando com a linguagem Bash na distribuição Linux Ubuntu, isso através de uma máquina virtual instalada com Ubuntu Server.

Tópicos incluem:
* Conexão SSH no Linux e via Putty no Windows ao servidor remoto na máquina virtual;
* Manipulação de arquivos e diretórios;
* Comandos de listagem e procura de arquivos;
* Filtragem de dados;
* Histórico;
* Permissões administrativas;
* Controle de acesso e usuários;
* Sistemas de permissão;
* Grupos;
* Comandos de ajuda;
* Editores de Texto;
* Gerenciadores de Pacotes;
* Scripts;
* Gerenciadores de Discos;
* Ambientes gráficos.

Como desafio deste módulo, foi criado um script para provisionar uma estrutura de diretórios, grupos e usuários, além de adicionar as permissões apropriadas 
para essa estrutura. [Infrastructure as Code I](https://github.com/Gabryel-Barboza/DIO/blob/Bash/Linux/Desafios/iac-1.sh)
```bash
# Estrutura de diretórios criada:
/
├── adm
├── publico
├── sec
└── ven
# Suas respectivas permissões:
  drwxrwx--- 2 root root 4096 jan 14 21:56 adm
  drwxrwxrwx 2 root root 4096 jan 14 21:56 publico
  drwxrwx--- 2 root root 4096 jan 14 21:56 sec
  drwxrwx--- 2 root root 4096 jan 14 21:56 ven

# Grupos e usuários adicionados:
  GRP_ADM:x:1001:carlos,maria,joao
  GRP_VEN:x:1002:debora,sebastiana,roberto
  GRP_SEC:x:1003:josefina,amanda,rogerio
```
Também está disponibilizado um script para desfazer as alterações na pasta de desafios.

## Desafio IaC II
Para o segundo desafio, [Infrastructure as Code II](https://github.com/Gabryel-Barboza/DIO/blob/Bash/Linux/Desafios/iac-2.sh) está criado um script de provisionamento de um servidor web simples com Apache. O script atualiza o sistema e instala os pacotes necessários para
subir o servidor web localmente.

A aplicação web provisionada após execução do script:
![Screenshot 2025-01-18 at 15-53-11 Sparsh Architecture](https://github.com/user-attachments/assets/50700e6b-507e-42fb-a701-55eb8c865250) <br>

Site disponibilizado pela DIO para realizar o desafio.

# Fundamentos do Docker
Este tópico foi desenvolvido no curso de **Docker Fundamentals** e fornece a base para criar contêineres Docker, arquivos Dockerfile, automações com Docker Compose, clusteres com Docker Swarm e provisionamento de máquinas com Vagrant.

![Captura de tela de 2025-04-22 01-21-09](https://github.com/user-attachments/assets/b460cf82-186d-416c-9f1f-2f506b72a059)

## Docker Compose Apache Web
O primeiro desafio do módulo possui os seguintes requisitos:
* Criar um documento `docker-compose.yaml` com as configurações para construir um servidor web com Apache
* Criar uma aplicação web para o contêiner provisionado com o Docker Compose
Além desses requerimentos, o desafio é elevado ao usar um ´dockerfile´ para construir o contêiner e copiar a aplicação automaticamente para o servidor.

Estrutura do documento usado no Docker Compose:
```yaml

```
## Clusters Swarm Provisionados com Vagrant
O segundo desafio do módulo consiste em criar um arquivo para provisionamento de máquinas virtuais com o software Vagrant. O arquivo possui as seguintes funcionalidades:
* Três máquinas virtuais com Ubuntu Server 22.04 provisionadas
* Uma máquina master para ser o nó gerenciador do cluster Swarm e nós workers
* Instalação automática do Docker
* Configuração automática do cluster Swarm
