saldo = 1000;
saque = 200;
limite = 100;
conta_especial = True;

print(saldo >= saque and saque <= limite);

print(saldo > saque or saque < limite);

print(not(saldo < saque));
print(not "Verdadeiro se preenchido");
print(not "");

conta_com_saldo_suficiente = saldo >= saque and saque <= limite;
conta_especial_com_saldo_suficiente = saldo >= saque and conta_especial;
print(conta_com_saldo_suficiente or conta_especial_com_saldo_suficiente);
