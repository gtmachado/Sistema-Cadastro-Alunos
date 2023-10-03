import sqlite3

class Aluno:
    def __init__(self, nome, sobrenome, matricula, idade, email):
        self.nome= nome
        self.sobrenome = sobrenome
        self.matricula = matricula
        self.idade = idade
        self.email = email
        self.__nome = nome
        self.__id = None   

    def get_nome(self):
        return self.__nome

    def get_sobrenome(self):
        return self.__sobrenome

    def get_matricula(self):
        return self.__matricula

    def get_idade(self):
        return self.__idade

    def get_email(self):
        return self.__email

    def set_nome(self, nome):
        self.__nome = nome

    def set_sobrenome(self, sobrenome):
        self.__sobrenome = sobrenome

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def set_idade(self, idade):
        self.__idade = idade

    def set_email(self, email):
        self.__email = email
        
    def get_id(self):
        return self.__id

    def set_id(self, aluno_id):
        self.__id = aluno_id

    def __str__(self):
        return f'\n\nID: {self.get_id()}\nNome: {self.nome},\nSobrenome: {self.sobrenome}\nMatrícula: {self.matricula}\nIdade: {self.idade}\nEmail: {self.email}'