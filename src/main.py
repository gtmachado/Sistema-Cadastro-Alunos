import sqlite3
from aluno import Aluno
from banco import Banco_Dados

def exibir_menu():
    print("----- Menu -----")
    print("1. Cadastrar Novo Aluno")
    print("2. Visualizar Alunos")
    print("3. Modificar Informações de Aluno")
    print("4. Deletar")
    print("0. Sair\n")

sistema = Banco_Dados()

while True:
    exibir_menu()
    escolha_menu = input("Escolha uma opção: ")

    if escolha_menu == "0":
        print("Saindo do programa.")
        break

    elif escolha_menu == "1": 
        
        nome = input("\nNome do Aluno: ")
        sobrenome = input("Sobrenome: ")
        matricula = input("Matrícula: ")
        idade = input("Idade: ")
        email = input("Email: ")
        id_aluno = sistema.cadastrar_aluno(Aluno(nome, sobrenome, matricula, idade, email ))
        print("\nAluno cadastrado com sucesso!\n\n")

    elif escolha_menu == "2": 
        
        for aluno_info in sistema.visualizar_alunos():
            aluno_existente = Aluno(aluno_info[1], aluno_info[2], aluno_info[3], aluno_info[4], aluno_info[5])
            aluno_existente.set_id(aluno_info[0])
            print(aluno_existente)
        print()

    elif escolha_menu == "3": 

        id_aluno = int(input("ID do Aluno a ser atualizado: "))
        novo_nome = input("\nNovo Nome: ")
        novo_sobrenome = input("Novo Sobrenome: ")
        nova_matricula = input("Nova Matrícula: ")
        nova_idade = input("Nova Idade: ")
        novo_email = input("Novo Email: ")
        sistema.atualizar_aluno(id_aluno, novo_nome, novo_sobrenome, nova_matricula, nova_idade, novo_email)
        print("\n\nAluno atualizado com sucesso.\n\n")


    elif escolha_menu == "4":
         
        id_aluno = int(input("ID do Aluno a ser deletado: "))
        sistema.deletar_aluno(id_aluno)
        print("\nAluno deletado com sucesso.\n\n")

    else:
        print("Opção inválida.")

sistema.fechar_conexao()