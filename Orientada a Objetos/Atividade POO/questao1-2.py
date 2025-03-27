class Aluno:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso
    
    def exibir_dados(self):
        print(f'\nNome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Curso: {self.curso}')

aluno1 = Aluno('Sávio Alves', 19, 'Sistemas para Internet')
aluno2 = Aluno('Henrique Vieira', 20, 'Engenharia de Software')
aluno1.exibir_dados()
aluno2.exibir_dados()