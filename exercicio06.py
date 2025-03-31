#lê o nome e numero de gols de dois times e escrever no nome do vencedor
timea= input (f"Qual é o nome do primeiro time?")
golsa= int (input(f"Digite o numero de gols do time {timea}, "))
timeb= input (f"Qual é o nome do primeiro time?")
golsb= int (input (f"Digite o numero de gols do time {timeb}"))
if golsa>golsb:
    print (f"Time {timea} venceu")
else:
    if golsb>golsa:
        print (f"Time {timeb} venceu")
    else:
        print ("EMPATE")
