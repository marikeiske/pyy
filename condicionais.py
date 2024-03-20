#if, elif e else

#Exemplo IF

idade = int(input("Quantos anos vc tem: "))
print("Exemplo de comando if")
if idade >= 18:
    print("Você é maior de idade.")
elif idade >= 15:
    print("Você é adolescente.")
else:
    print("Você é menor de idade.")

mensagem = "Pode tirar a CNH" if idade >= 18 else "Você ainda não pode tirar a CNH"   
print(mensagem)


#if idade == 19:
 #   print("Você tem 19 anos.")    

#if idade <= 18:
 #   print("Você é menor de idade.")    

#if idade != 10:
 #   print("Você não tem 10 anos.")    