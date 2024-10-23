import os
from aluno import Aluno
from grade import Grade
from matricula import Matricula
from lista_duplamente_encadeada import ListaDuplamenteEncadeada
from pesquisa_binaria import pesquisa_binaria

# Criando a lista de matrículas
lista_matriculas = ListaDuplamenteEncadeada()

def limpar_tela():
    """
    Limpa a tela do terminal.
    """
    os.system('cls')

def exibir_menu():
    """
    Exibe o menu de opções para o usuário.
    """
    print("\nMenu:")
    print("1. Incluir matrícula")
    print("2. Remover matrícula")
    print("3. Exibir matrículas")
    print("4. Consultar matrícula")
    print("5. Realizar pesquisa binária")
    print("6. Sair")

def incluir_matricula():
    """
    Solicita os dados do aluno e da grade, cria uma nova matrícula e a inclui na lista.
    """
    ra = int(input("Digite o RA do aluno: "))
    nome = input("Digite o nome do aluno: ")
    telefone = input("Digite o telefone do aluno: ")
    disciplina = input("Digite a disciplina: ")
    etapa = input("Digite a etapa: ")

    # Cria instâncias de Aluno, Grade e Matricula
    aluno = Aluno(ra, nome, telefone)
    grade = Grade(disciplina, etapa)
    matricula = Matricula(aluno, grade)
    
    # Inclui a matrícula na lista
    lista_matriculas.incluir(matricula)
    print("Matrícula incluída com sucesso!")

def remover_matricula():
    """
    Solicita o RA do aluno e remove a matrícula correspondente da lista.
    """
    ra = int(input("Digite o RA do aluno a ser removido: "))
    if lista_matriculas.remover(ra):
        print("Matrícula removida com sucesso!")
    else:
        print("Aluno não encontrado.")

def consultar_matricula():
    # Solicita o RA do aluno e consulta a matrícula correspondente na lista.
    ra = int(input("Digite o RA do aluno a ser consultado: "))
    matricula = lista_matriculas.consultar(ra)
    if matricula:
        print("Aluno encontrado:", matricula)
    else:
        print("Aluno não encontrado.")

def realizar_pesquisa_binaria():\
    # Solicita o RA do aluno e realiza uma pesquisa binária na lista de matrículas ordenada.
    ra = int(input("Digite o RA do aluno a ser pesquisado: "))

    # Ordena a lista de matrículas pelo RA do aluno
    lista_ordenada = sorted([mat for mat in lista_matriculas], key=lambda x: x.aluno.ra)

    limpar_tela()  # Limpa a tela antes de exibir o menu

    # Realiza a pesquisa binária
    resultado = pesquisa_binaria(lista_ordenada, ra)
    if resultado:
        print("Aluno encontrado:", resultado)
    else:
        print("Aluno não encontrado.")

# Loop principal do programa
while True:
    exibir_menu()
    
    # Solicita a escolha do usuário
    opcao = input("Escolha uma opção: ")

    # Executa a função correspondente à opção escolhida
    if opcao == '1':
        incluir_matricula()
    elif opcao == '2':
        remover_matricula()
    elif opcao == '3':
        print("Matrículas atuais:")
        lista_matriculas.exibir()
    elif opcao == '4':
        consultar_matricula()
    elif opcao == '5':
        realizar_pesquisa_binaria()
    elif opcao == '6':
        break  # Encerra o loop e o programa
    else:
        print("Opção inválida. Tente novamente.")
    
    input("Pressione Enter para continuar...")  # Pausa para o usuário ver o resultado