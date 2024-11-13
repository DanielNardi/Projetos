import Pessoa
import flask
from flask_cors import CORS

app = flask.Flask(__name__)

CORS(app)

@app.route('/cadastro', methods=['POST'])
def post_function_criacao():
  try:
    data = flask.request.get_json()
    nome = data.get('nome')
    data_nascimento = data.get('data_nascimento')
    cpf = data.get('cpf')
    email = data.get('email')
    senha = data.get('senha')
    if nome == None or data_nascimento == None or cpf == None or email == None or senha == None:
      return flask.jsonify({'Mensagem': 'Está faltando alguma coisa'}), 400
    p = Pessoa.Pessoa(nome,data_nascimento,cpf,email,senha)
    print(p.nome)
    return flask.jsonify({'Mensagem': p.criar_conta()}), 200
  except Exception as err1:
    print(err1)


@app.route('/login', methods=['POST'])
def post_function_login():
  try:
    data = flask.request.get_json()
    email = data.get('email')
    senha = data.get('senha')
    nome = None
    data_nascimento = None
    cpf = None
    if email == None or senha == None:
      return flask.jsonify({'Mensagem': 'Está faltando alguma coisa'}), 400
    p = Pessoa.Pessoa(nome,data_nascimento,cpf,email,senha)
    print(p.email)
    valor = p.logar()
    valor = str(valor)
    return flask.jsonify({'Mensagem': valor}), 200
  except Exception as err1:
    print(err1)

@app.route('/mandar_codigo', methods=['POST'])
def post_function_mandar_codigo():
  try:
    data = flask.request.get_json()
    cpf = data.get('cpf')
    email = None
    senha = None
    nome = None
    data_nascimento = None
    if cpf == None:
      return flask.jsonify({'Mensagem': 'Está faltando alguma coisa'}), 400
    p = Pessoa.Pessoa(nome,data_nascimento,cpf,email,senha)
    print(p.cpf)
    valor = p.mandar_codigo()
    valor = str(valor)
    return flask.jsonify({'Mensagem': valor}), 200
  except Exception as err1:
    print(err1)

@app.route('/listar/<cpf>', methods=['GET'])
def post_function_listar(cpf):
  try:
    email = None
    senha = None
    nome = None
    data_nascimento = None
    print(cpf)
    p = Pessoa.Pessoa(nome,data_nascimento,cpf,email,senha)
    valor = p.listar()
    return flask.jsonify({'Mensagem': valor}), 200
  except Exception as err1:
    print(err1)

app.run(host='0.0.0.0',port=4000)