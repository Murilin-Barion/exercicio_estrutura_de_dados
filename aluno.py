class Aluno:
    """
    Classe que representa um aluno.
    """
    def __init__(self, ra, nome, telefone):
        """
        Inicializa uma nova instância de Aluno.

        Args:
            ra (int): Registro Acadêmico (RA) do aluno.
            nome (str): Nome do aluno.
            telefone (str): Telefone do aluno.
        """
        self.ra = ra  # Atribui o RA do aluno ao atributo ra
        self.nome = nome  # Atribui o nome do aluno ao atributo nome
        self.telefone = telefone  # Atribui o telefone do aluno ao atributo telefone

    def __str__(self):
        """
        Retorna uma representação em string do aluno.

        Returns:
            str: Uma string que representa o aluno, incluindo RA, nome e telefone.
        """
        return f"RA: {self.ra}, Nome: {self.nome}, Telefone: {self.telefone}"