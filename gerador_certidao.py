from fpdf import FPDF
import uuid
from datetime import datetime
import pytz

def gerar_certidao(nome='', cpf_cnpj=''):
  nome_arquivo = str(uuid.uuid4()) + '.pdf'
  data = datetime.now(pytz.timezone('America/Recife')).strftime("%d/%m/%Y - %H:%M")

  pdf = FPDF()
  pdf.add_page()
  pdf.set_font("Arial", size=18)
  pdf.cell(200, 10, txt="CERTIDÃO DE QUITAÇÃO DO TRT", ln=1, align="C")
  pdf.set_font("Arial", size=10)

  for i in range(2):
    pdf.cell(200, 10, txt="", ln=1)

  pdf.multi_cell(200, 10, txt="Sr(a). " + nome + ", "+cpf_cnpj+", está sem dívidas na justiça do trabalho. E AI MEU AMIGO, QUAL A BOA DESSA PORRA? TOMAR BOMBA E PA FICAR GRANDE! USAVA DIFERENTE, SABE PORQUE? USA HTML CRIAVA ASSIM N EU QUABRAVA NUM HTML ", align="L")
  pdf.cell(200, 10, txt=data, ln=1, align="R")

  pdf.output('./temp_pdf/' + nome_arquivo)

  return nome_arquivo 
