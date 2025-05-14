import sqlite3

def criar_tabela():
    conn = sqlite3.connect('agendamentos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS agendamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL,
            telefone TEXT NOT NULL,
            email TEXT NOT NULL,
            tipo_procedimento TEXT NOT NULL,
            data TEXT NOT NULL,
            horario TEXT NOT NULL
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