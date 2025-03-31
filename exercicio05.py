nota1= float (input("Digite a primeira nota"))
nota2= float (input ("Digite a segunda nota"))
nota3= float (input  ("Digite a terceira nota"))
media= (nota1+nota2+nota3)/3
if media>=7:
    print (f"Aprovado : {media:.2f}")
elif 4>=media:
    print (f"Recuperação, média: {media:.2f}")
else:
    print (f"Reprovado, média: {media :.2f}")

