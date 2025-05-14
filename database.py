import sqlite3

def criar_tabela_se_nao_existir():
    conn = sqlite3.connect('Agendamentos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS agendamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cpf TEXT,
            telefone TEXT,
            email TEXT,
            procedimento TEXT,
            data TEXT,
            horario TEXT
        )
    ''')
    conn.commit()
    conn.close()


def inserir_agendamento(nome, cpf, telefone, email, tipo_procedimento, data, horario):
    conn = sqlite3.connect('agendamentos.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO agendamentos 
        (nome, cpf, telefone, email, tipo_procedimento, data, horario)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (nome, cpf, telefone, email, tipo_procedimento, data, horario))
    conn.commit()
    conn.close()

def buscar_agendamentos():
    conn = sqlite3.connect('agendamentos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM agendamentos')
    agendamentos = cursor.fetchall()
    conn.close()
    return agendamentos
