class Grade:
    """
    Classe que representa a grade de uma disciplina.
    """
    def __init__(self, disciplina, etapa):
        """
        Inicializa uma nova instância de Grade.

        Args:
            disciplina (str): Nome da disciplina.
            etapa (str): Etapa da disciplina.
        """
        self.disciplina = disciplina  # Atribui o nome da disciplina ao atributo disciplina
        self.etapa = etapa  # Atribui a etapa da disciplina ao atributo etapa

    def __str__(self):
        """
        Retorna uma representação em string da grade.

        Returns:
            str: Uma string que representa a grade, incluindo o nome da disciplina e a etapa.
        """
        return f"Disciplina: {self.disciplina}, Etapa: {self.etapa}"