from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
from flask import url_for
from flask_mail import Mail
from flask_mail import Message
from flask import send_from_directory
from flask import flash
from flask import Markup
from gerador_certidao import gerar_certidao
import random
import string
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './temp_pdf/'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'apenasparatestar3@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASSWORD') 
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
app.secret_key = 'MINHAKEYALEATORIA'

def _gerar_codigo():
  # exemplos de codigos gerados por essa função: A2C5D6, H1C6Z2
  codigo = [] 
  codigo.append(random.choice(string.ascii_letters).upper()) # 
  codigo.append(str(random.randint(0,9)))
  codigo.append(random.choice(string.ascii_letters).upper()) # 
  codigo.append(str(random.randint(0,9)))
  codigo.append(random.choice(string.ascii_letters).upper()) # 
  codigo.append(str(random.randint(0,9)))

  return ''.join(codigo)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
      codigo = _gerar_codigo() 

      session['codigo'] = codigo
      session['nome'] = request.form.get('nomeRazaoSocial')
      session['cpf_cnpj'] = request.form.get('cpfCnpj') 
      session['email'] = request.form.get('email')

      msg = Message("TRT - Código de Verificação", sender = "apenasparatestar3@gmail.com")
      msg.add_recipient(request.form.get('email'))
      msg.html = "Caro " + session["nome"] +  ", aqui está seu código de confirmação: <b>" + codigo + "</b>"
      mail.send(msg)
      return redirect('/confirmar')
    else:
      return render_template('index.html')

@app.route('/confirmar', methods=['GET', 'POST'])
def confirmar():
  nome = (session['nome'])

  if nome == None or nome == "":
    redirect('/')

  cpf_cnpj = session['cpf_cnpj']
  email = session['email']

  if request.method == 'POST':
    if session['codigo'] == request.form.get('codigo'):
      nome_arquivo = gerar_certidao(nome=nome, cpf_cnpj=cpf_cnpj)
      return send_from_directory(app.config['UPLOAD_FOLDER'], nome_arquivo)
    else:
      flash('Código Inválido!!!', 'danger')
      return redirect('/confirmar') 
  else:
    m = Markup('O código de verificação foi enviado para o email: <b>' + email + '</b>.')
    flash(m, 'primary')
    return render_template('confirmar.html', nome=nome, cpf_cnpj=cpf_cnpj)

@app.route('/deletar')
def deletar_pdfs_temporarios():
  os.system('rm -rf ./temp_pdf/*')

  return 'deletado com sucesso!'

if __name__ == '__main__':
  app.run(host='0.0.0.0')
