# Modo de escrita em manipulação de arquivos

# Cria o arquivo automaticamente se não existir
# Apaga o conteúdo do arquivo para começar a escrever novamente
arquivo = open("./POO/teste.txt", "w")

# Escrita de arquivo
arquivo.write("Escrevendo dados em um novo arquivo")
arquivo.write(" ")

# Recebe um Iterável para a escrita
arquivo.writelines(["com ", "Python"])
arquivo.writelines(["\n", "Interagindo", "\n", "com", "\n", "o arquivo"])
arquivo.close()