def pesquisa_binaria(lista_ordenada, ra):
    """
    Realiza uma pesquisa binária em uma lista ordenada de matrículas para encontrar um aluno pelo RA.

    Args:
        lista_ordenada (list): Lista de matrículas ordenada pelo RA do aluno.
        ra (int): RA do aluno a ser pesquisado.

    Returns:
        Matricula: A matrícula do aluno se encontrado, caso contrário, None.
    """
    inicio = 0  # Índice inicial da lista
    fim = len(lista_ordenada) - 1  # Índice final da lista
    
    while inicio <= fim:
        meio = (inicio + fim) // 2  # Calcula o índice do meio
        matricula_atual = lista_ordenada[meio]  # Obtém a matrícula no índice do meio
        
        if matricula_atual.aluno.ra == ra:
            # Se o RA do aluno na matrícula atual for igual ao RA pesquisado, retorna a matrícula
            return matricula_atual
        elif matricula_atual.aluno.ra < ra:
            # Se o RA do aluno na matrícula atual for menor que o RA pesquisado, ajusta o índice inicial
            inicio = meio + 1
        else:
            # Se o RA do aluno na matrícula atual for maior que o RA pesquisado, ajusta o índice final
            fim = meio - 1
    
    return None  # Retorna None se o aluno não for encontrado