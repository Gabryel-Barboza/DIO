# Verifica se ocupa a mesma região de memória

curso = "Curso de Python";
nome_curso = curso;
saldo, limite = 1000, 500;

print(saldo is limite);
print(curso is nome_curso);
print(saldo is not nome_curso);
limite = 1000;
print(saldo is limite);