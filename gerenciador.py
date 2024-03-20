def adicionar_tarefa(tarefas, nome_tarefa):
 
 tarefa = {"nome": nome_tarefa, "completada": False}
 tarefas.append(tarefa)
 print(f"tarefa {nome_tarefa} foi add com suceesso!")
 return

tarefas = []
while True:
 print("\n Menu:")
 print("1. Add tarefas")
 print("2. Ver tarefas")
 print("3. Atualizar tarefas")
 print("4. Completar tarefas")
 print("5. Deletar ")
 print("6. Sair")

 escolha = input("Digite a escolha: ")

 if escolha == "1":
  nome_tarefa = input("Digite o nome da tarefa escolhida: ")
  adicionar_tarefa(tarefas, nome_tarefa)
 
 if escolha == "6":
  break
 
print("Fim")
