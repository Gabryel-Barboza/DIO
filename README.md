# Repositório com o matérial do bootcamp da [Digital Innovation One](https://web.dio.me)
Estão inclusos os projetos feitos nos diretórios de desafios. <br>
Altere a **Branch** atual para alguma das opções disponíveis para visualizar outros cursos.

# Desafios
* [Infrastructure as Code I](https://github.com/Gabryel-Barboza/DIO/blob/Bash/Linux/Desafios/iac-1.sh)

# Aprendendo Comandos em Bash
Iniciando com a linguagem Bash na distribuição Linux Ubuntu, isso através de uma máquina virtual instalada com Ubuntu Server. Tópicos incluem:
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
* Scripts;

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
