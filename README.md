# Repositório com o matérial do bootcamp da [Digital Innovation One](https://web.dio.me)
Estão inclusos os projetos feitos nos diretórios de desafios. <br>
Altere a **Branch** atual para alguma das opções disponíveis para visualizar outros cursos.

# Desafios
* [Infrastructure as Code I](https://github.com/Gabryel-Barboza/DIO/blob/Bash/Linux/Desafios/iac-1.sh)
* [Infrastructure as Code II](https://github.com/Gabryel-Barboza/DIO/blob/Bash/Linux/Desafios/iac-2.sh)

# Aprendendo Comandos em Bash
Iniciando com a linguagem Bash na distribuição Linux Ubuntu, isso através de uma máquina virtual instalada com Ubuntu Server.<br>
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
subir o servidor web localmente. <br>
A aplicação web provisionada após execução do script:
![Screenshot 2025-01-18 at 15-53-11 Sparsh Architecture](https://github.com/user-attachments/assets/50700e6b-507e-42fb-a701-55eb8c865250) <br>

Site disponibilizado pela DIO para realizar o desafio.

