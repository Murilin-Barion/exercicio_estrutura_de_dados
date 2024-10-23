class Matricula:
    # Classe que representa uma matrícula de um aluno em uma disciplina.
    
    # Método construtor
    def __init__(self, aluno, grade):
        """
        Inicializa uma nova instância de Matricula.

        Args:
            aluno (Aluno): Instância da classe Aluno.
            grade (Grade): Instância da classe Grade.
        """
        self.aluno = aluno  # Atribui a instância de Aluno à matrícula
        self.grade = grade  # Atribui a instância de Grade à matrícula

    # Método para representação em string
    def __str__(self):
        """
        Retorna uma representação em string da matrícula.

        Returns:
            str: Uma string que representa a matrícula, incluindo o nome do aluno, RA, disciplina e etapa.
        """
        return f"Aluno: {self.aluno.nome}, RA: {self.aluno.ra}, Disciplina: {self.grade.disciplina}, Etapa: {self.grade.etapa}"