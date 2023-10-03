import sqlite3

class Aluno:
    def __init__(self, nome, sobrenome, matricula, idade, email):
        self.nome= nome
        self.sobrenome = sobrenome
        self.matricula = matricula
        self.idade = idade
        self.email = email
        self.__id = None   
        
    def get_id(self):
        return self.__id

    def set_id(self, aluno_id):
        self.__id = aluno_id

    def __str__(self):
        return f'\n\nID: {self.get_id()}\nNome: {self.nome}\nSobrenome: {self.sobrenome}\nMatrícula: {self.matricula}\nIdade: {self.idade}\nEmail: {self.email}'