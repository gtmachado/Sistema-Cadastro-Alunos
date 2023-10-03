import sqlite3

class Banco_Dados:
    def __init__(self, db_name="db/cadastro.db"):
        self.conn = sqlite3.connect(db_name)

        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS Aluno (
                ID_Aluno INTEGER PRIMARY KEY AUTOINCREMENT,
                Nome TEXT NOT NULL,
                Sobrenome TEXT NOT NULL,
                Matricula TEXT NOT NULL,
                Idade INTEGER,
                Email TEXT NOT NULL
            )
        ''')

    def cadastrar_aluno(self, aluno):
        cursor = self.conn.execute('''
            INSERT INTO Aluno (Nome, Sobrenome, Matricula, Idade, Email) VALUES (?, ?, ?, ?, ?)
        ''', (aluno.nome, aluno.sobrenome, aluno.matricula, aluno.idade, aluno.email))
        self.conn.commit()
        return cursor.lastrowid

    def visualizar_alunos(self):
        cursor = self.conn.execute('SELECT * FROM Aluno')
        return cursor.fetchall()

    def atualizar_aluno(self, aluno_id, novo_nome, novo_sobrenome, nova_matricula, nova_idade, novo_email):
        self.conn.execute('''
            UPDATE Aluno SET Nome=?, Sobrenome=?, Matricula=?, Idade=?, Email=? WHERE ID_Aluno=?
        ''', (novo_nome, novo_sobrenome,nova_matricula, nova_idade, novo_email, aluno_id))
        self.conn.commit()
        
    def deletar_aluno(self, aluno_id):
        self.conn.execute('DELETE FROM Aluno WHERE ID_Aluno=?', (aluno_id,))
        self.conn.commit()

    def fechar_conexao(self):
        self.conn.close()