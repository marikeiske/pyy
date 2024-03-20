# Exemplo

def saudacao(nome):
 print(f"Olá, {nome}!")

print("\n Chamando função:")
saudacao("Keke")
saudacao("KaKa")

def quadrado(numero):
 resultado = numero ** 2
 return resultado

print("\n Chamando quadrado:")
resultado_quadrado = quadrado(6)
print("Resultado:", resultado_quadrado)

def soma(num1, num2):
 resultado = num1 + num2
 return resultado

print("A soma:" )
num1 = 30
num2 = 90
resultado_soma = soma(num1,num2)
print("A soma do num %s e o num %s é  %s" % (num1, num2, resultado_soma))