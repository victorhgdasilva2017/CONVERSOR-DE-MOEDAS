# CODING MARK:1
#
# VICTOR HUGO
#
# --------------------------


print "CONVERSOR DE MOEDA: \n";
print "SELECIONE A MOEDA A SER CONVERTIDA: ";

print "1--DÓLAR PARA REAL\n2--DÓLAR PARA EURO\n3--EURO PARA REAL\n4--EURO PARA DÓLAR\n";

chomp($resposta = <STDIN>);

if($resposta == 1)
{

print"DÓLAR PARA REAL: \n";

print"DIGITE O VALOR DO DÓLAR: \n";
chomp($vldolar = <STDIN>);

print"DIGITE O VALOR A SER CONVERTIDO EM DÓLARES: \n";
chomp($dolar = <STDIN>);

print"O VALOR EM REAIS É:" .$dolar*$vldolar;

}


if($resposta == 2)
{

print"DÓLAR PARA EURO: \n";

print"DIGITE O VALOR DO DÓLAR EM EUROS: \n";
chomp($vldolar = <STDIN>);

print"DIGITE O VALOR A SER CONVERTIDO EM DÓLARES: \n";
chomp($dolar = <STDIN>);

print"O VALOR EM EUROS É:" .$dolar*$vldolar;

}


if($resposta == 3)
{

print"EURO PARA REAL: \n";

print"DIGITE O VALOR DO EURO: \n":
chomp($vleuro = <STDIN>);

print"DIGITE O VALOR A SER CONVERTIDO EM EUROS: \n";
chomp($euro = <STDIN>);

print"O VALOR EM REAIS É:" .$vleuro*$euro;

}


if($resposta == 4)
{

print"EURO PARA DÓLAR: \n";

print"DIGITE O VALOR DO EURO EM DÓLARES: \n";
chomp($vleuro = <STDIN>);

print"DIGITE O VALOR A SER CONVERTIDO EM EUROS: \n";
chomp($euro = <STDIN>);

print"O VALOR EM DÓLARES É:" .$vleuro*$euro;

}

