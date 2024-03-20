print("For usando lista")
lista = [1,2,3,4,5]
for elemento in lista:
   print(elemento) 

print("For usando tupla")
tupla = [1,2,3,4,5]   
for elemento in tupla:
   print(elemento)

pessoa = {"nome": "Mari", "idade":18, "city":"Pinda"}   
print("\n For usando chaves")
for chave in pessoa.keys():
   print(chave)

for valor in pessoa.values():
   print(valor)   

for chave, valor in pessoa.items():
   print(f"{chave}: {valor}") 

# range (): intervalo numérico
#[0,1,2,3,4,5,6,7]
   print("\n Utilizando a funçao range()")
for numero in range(5):
   print("Numero:", numero)     

print("\n Utilizando  a função range() com len()")  
lista = [1,2,3,4,5]
for indice in range(0, len(lista)):
   if indice == 3:
    lista[indice] = 5
   else:
      lista[indice] = 0
      print(lista)


# enumerete()
lista_enumerete = ["a", "b", "c"]
for indice, valor in enumerate (lista_enumerete):
   print(f"{indice}: {valor}")
   if indice == 1:
      print   ("Indice 1")
