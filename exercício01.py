#Programa que ler um nome,idade e salario
nome=input("Qual é o seu nome?")
idade=int (input("Qual é a sua idade?"))
salario=float(input("Qual é o seu salário?"))
print(f"O seu nome é {nome},Sua idade é {idade}, Seu salário é {salario}")

#aumento percentual  do salário
porcentagem=float(input("Qual foi o aumento percentual do seu salário?"))
salariofinal=float(((porcentagem+100)*salario)/100)
print(f"O seu novo salário é {salariofinal}