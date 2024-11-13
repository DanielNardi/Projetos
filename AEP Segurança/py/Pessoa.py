import pandas as pd
import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

class Pessoa:

  def __init__(self, nome, data_nascimento, cpf, email, senha, cartao=None):
    
    self.nome = nome
    self.data_nascimento = data_nascimento
    self.cpf = cpf
    self.email = email
    self.senha = senha
    self.cartao = cartao

  def criar_conta(self):
    try:
      engine = sqlalchemy.create_engine('postgresql+psycopg2://manfrim:manfrim@localhost:5432/manfrim')
      df = pd.read_sql("""
                        select 
                          id
                        from faculdade.pessoas p
                        where
                          p.email = %(self.email)s
                          or p.cpf = %(self.cpf)s
                        """, engine, params={'self.email':self.email,'self.cpf':self.cpf})
      if not df.empty:
        return False
    except Exception as e:
      print('Erro ao verificar se a conta já existe', e)
    try:
      df = pd.DataFrame({'nome':self.nome,'data_nascimento':pd.to_datetime(self.data_nascimento),'cpf':self.cpf,'email':self.email,'senha':self.senha,'cartão':self.cartao}, index=[1])
      df.to_sql('pessoas', con=engine, schema='faculdade', if_exists='append', index=False)
      return True
    except Exception as e:
      print('Erro ao adicionar o valor no banco', e)    

    #sistema que faz a verificação se o e-mail ou cpf ja existe e se não existir cria a conta

  def logar(self):
    try:
      engine = sqlalchemy.create_engine('postgresql+psycopg2://manfrim:manfrim@localhost:5432/manfrim')
      df = pd.read_sql("""
                        select 
                          cpf
                        from faculdade.pessoas p
                        where
                          p.email = %(self.email)s
                          and p.senha = %(self.senha)s
                        """, engine, params={'self.email':self.email,'self.senha':self.senha})
      if df.empty:
        return 0
      else:
        valor = df['cpf'].iloc[0]
        return valor
    except Exception as e:
      print('Erro ao verificar email e senha', e)

    #loga sua conta de acordo com a senha e e-mail da pessoa

  def mandar_codigo(self):
    try:
      engine = sqlalchemy.create_engine('postgresql+psycopg2://manfrim:manfrim@localhost:5432/manfrim')
      df = pd.read_sql("""
                        select 
                          email
                        from faculdade.pessoas p
                        where
                          p.cpf = %(self.cpf)s
                        """, engine, params={'self.cpf':self.cpf})
      codigo = random.randint(100000, 999999)
      mensagem = f"""
        <!DOCTYPE html>
        <html>
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Exemplo de E-mail</title>
          <style>
            body {{
              font-family: Arial, sans-serif;
              color: #333;
              margin: 0;
              padding: 0;
              background-color: #f0f0f0;
            }}
            .container {{
              width: 100%;
              max-width: 600px;
              margin: 0 auto;
              padding: 20px;
              background-color: #f0f0f0;
            }}
            .center-box {{
              background-color: #ffffff;
              border: 1px solid #ddd;
              padding: 40px;
              text-align: center;
              margin: 0 auto;
              max-width: 500px;
              border-radius: 8px;
              box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }}
            .header-text {{
              font-size: 18px;
              color: #333;
              margin-bottom: 20px;
            }}
            .main-text {{
              font-size: 24px;
              font-weight: bold;
              color: #4CAF50;
            }}
          </style>
        </head>
        <body>
          <div class="container">
            <div class="center-box">
              <p class="header-text">Aqui está o número que você irá colocar para fazer a autenticação.</p>
              <p class="main-text">{codigo}</p>
            </div>
          </div>
        </body>
        </html>
        """
      email_host = "smtp.gmail.com"
      porta = 587
      email = "apimanfrim@gmail.com"
      senha = "wewp otvb sgjt xfko"
      msg = MIMEMultipart()
      msg["From"] = email
      msg["To"] = df['email'].iloc[0]
      msg["Subject"] = 'Codigo de Altenticação da Conta'
      msg.attach(MIMEText(mensagem, 'html'))
      with smtplib.SMTP(email_host, porta) as server:
          server.starttls()
          server.login(email, senha)
          server.sendmail(email, df['email'].iloc[0], msg.as_string())
      return codigo
    except Exception as e:
        print(f"Ocorreu um erro ao enviar o e-mail: {e}")

  def listar(self):
    try:
      engine = sqlalchemy.create_engine('postgresql+psycopg2://manfrim:manfrim@localhost:5432/manfrim')
      df = pd.read_sql("""
                        select 
                          *
                        from faculdade.pessoas p
                        where
                          p.cpf = %(self.cpf)s
                        """, engine, params={'self.cpf':self.cpf})
      usuario = {
        "nome": df['nome'].iloc[0],
        "data_nascimento": str(df['data_nascimento'].iloc[0]),
        "cpf": df['cpf'].iloc[0],
        "email": df['email'].iloc[0],
        "senha": df['senha'].iloc[0]
      }
      return usuario
    except Exception as e:
      print(f"Ocorreu um erro ao enviar o e-mail: {e}")

    #sistema que verifica o token do login