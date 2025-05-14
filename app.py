from flask import Flask, render_template, request, redirect, url_for
import database
from datetime import datetime
from email.message import EmailMessage
import smtplib
import os
from dotenv import load_dotenv
from database import criar_tabela_se_nao_existir
app = Flask(__name__)

# Garante que a tabela seja criada na inicialização do aplicativo
criar_tabela()
criar_tabela_se_nao_existir()

load_dotenv()


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def agendar():
    mensagem = ""
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        telefone = request.form['telefone']
        email = request.form['email']
        tipo_procedimento = request.form['tipo_procedimento']
        data_str = request.form['data']
        horario = request.form['horario']

        agendamentos_existentes = database.buscar_agendamentos()
        for ag in agendamentos_existentes:
            if ag[6] == data_str and ag[7] == horario:
                mensagem = "Este horário já está agendado. Por favor, escolha outro."
                return render_template('agendamento.html', mensagem=mensagem)

        database.inserir_agendamento(nome, cpf, telefone, email, tipo_procedimento, data_str, horario)
        enviar_email_confirmacao(nome, cpf, telefone, email, tipo_procedimento, data_str, horario)
        return "Agendamento concluido"
    
    return render_template('agendamento.html', mensagem=mensagem)

@app.route('/agendamentos')
def agendamentos_realizados():
   agendamentos = database.buscar_agendamentos()
   return render_template('agendamentos.html', agendamentos=agendamentos)


import os
import smtplib
from email.message import EmailMessage


def enviar_email_confirmacao(nome, cpf, telefone, email_cliente, procedimento, data, horario):
    remetente = os.getenv("EMAIL_REMETENTE")
    senha = os.getenv("EMAIL_SENHA")
    destinatario = os.getenv("EMAIL_DESTINATARIO")

    corpo = f'''
    Novo agendamento realizado:

    Nome: {nome}
    CPF: {cpf}
    Telefone: {telefone}
    E-mail: {email_cliente}
    Procedimento: {procedimento}
    Data: {data}
    Horário: {horario}
    '''

    msg = EmailMessage()
    msg.set_content(corpo)
    msg['Subject'] = 'Novo Agendamento'
    msg['From'] = remetente
    msg['To'] = destinatario

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(remetente, senha)
            smtp.send_message(msg)
            print("E-mail enviado com sucesso.")
    except Exception as e:
        print("Erro ao enviar e-mail:", e)


#if __name__ == '__main__':
 #   database.criar_tabela()
  #  app.run(debug=True)
