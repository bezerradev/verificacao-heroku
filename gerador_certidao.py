from fpdf import FPDF
import uuid
from datetime import datetime
from datetime import timedelta
import pytz

def gerar_certidao(nome='', cpf_cnpj=''):
  nome_arquivo = str(uuid.uuid4()) + '.pdf'
  data = datetime.now(pytz.timezone('America/Recife'))
  dataNRed = data.strftime("%d/%m/%Y, %H:%M")
  dataRed = data.strftime("%d %B, %Y")
  dataF = data + timedelta(days=30)
  dataFim = dataF.strftime("%d/%m/%Y, %H:%M")
  
  pdf = FPDF()
  pdf.add_page()
  pdf.set_font("Arial", size=12)
  pdf.cell(200, 5, txt="PODER JUDICIÁRIO", align="C", ln=1)
  pdf.cell(200, 5, txt="JUSTIÇA DO TRABALHO", align="C", ln=1)
  pdf.cell(200, 5, txt="TRIBUNAL REGIONAL DO TRABALHO DA 21ª REGIÃO", align="C", ln=1)

  pdf.set_font("Arial", size=9, style="I")
  pdf.cell(200, 3, txt="Missão: Promover justiça, no âmbito das relações de trabalho, com", align="C", ln=1)
  pdf.cell(200, 3, txt="celeridade, eficiência e efetividade, contribuindo para a paz social e o", align="C", ln=1)
  pdf.cell(200, 3, txt="fortalecimento da cidadania.", align="C", ln=1)
  
  pdf.ln(5)

  pdf.set_font("Courier", size=12, style="B")
  pdf.cell(200, 5, txt="CERTIDÃO DE AÇÕES TRABALHISTAS", align="C", ln=1)

  pdf.ln(5)

  pdf.set_font("Courier", size=12)
  pdf.cell(200, 5, txt="Certidão nº: 00017/2019", align="L", ln=1)
  pdf.cell(200, 5, txt="Data de Emissão: " + dataNRed, align="L", ln=1)
  pdf.cell(200, 5, txt="Válida até: " + dataFim + " (30 dias)", align="L", ln=1)

  pdf.ln(5)

  pdf.set_font("Courier", size=12, style="B")
  pdf.cell(200, 5, txt="Dados Pesquisados:", align="L", ln=1)
  
  pdf.set_font("Courier", size=12)
  pdf.cell(200, 5, txt="CPF/CNPJ: " + cpf_cnpj, align="L", ln=1)
  pdf.cell(200, 5, txt="Nome: " + nome, align="L", ln=1)

  pdf.ln(5)


  pdf.set_font("Courier", size=12)
  pdf.write(5, txt="CERTIFICA-SE, que em pesquisa nos Sistemas de Acompanhamento Processual de 1ª e 2ª Instâncias (SAP1 e SAP2), bem como nos de Processos Eletrônicos da Justiça do Trabalho de 1º e 2º grau (PJe-1 e PJe-2) do Tribunal Regional do Trabalho da 21ª Região, e de acordo com os dados fornecidos pelo solicitante, NÃO CONSTAM, até a presente data, ações trabalhistas em tramitação.")

  pdf.ln(5)
  pdf.ln(5)

  pdf.set_font("Courier", size=12, style="B")
  pdf.cell(200, 5, txt="Observações:", align="L", ln=1)

  pdf.ln(5)  

  pdf.set_font("Courier", size=12)
  pdf.write(5, txt="1. A pesquisa nos Sistemas de Acompanhamento Processual de 1ª e 2ª Instâncias (SAP1 e SAP2), bem como nos de Processos Eletrônicos da Justiça do Trabalho de 1º e 2º grau (PJe-1 e PJe-2) não abrange processos arquivados definitivamente e foi realizada EXCLUSIVAMENTE pelo CPF ou CNPJ registrado na Secretaria da Receita Federal do Brasil, sendo opcional, consulta adicional pela exata grafia do nome informado pelo requerente.")
  pdf.ln(5)
  pdf.write(5, txt="2. Não são objeto de consulta para Certidão os processos que são: Ação Rescisória (AR), Carta de Ordem (CARTORD), Consignação em Pagamento(CONPAG), Correição Parcial (CORPAR), Embargos de Terceiro(ET), Inquérito para Apuração de Falta Grave(IAFG), Mandado de Segurança(MS) e Mandado de Segurança Coletivo(MSCOL), conforme classificação adotada pelo CNJ.")
  pdf.ln(5)
  pdf.write(5, txt="3. Esta certidão não gera os efeitos da Certidão Negativa de Débitos Trabalhistas - CNDT (www.tst.jus.br/certidão - documento que prova a regularidade trabalhista em todo o País para participar de licitações, nos termos da Lei nº 12.440, de 07/07/2011).")
  pdf.ln(5)
  pdf.write(5, txt="4. Para verificar a autenticidade desta Certidão, acesse o link de Emissão de Certidões Trabalhistas no endereço https://www.trt21.jus.br/Html/VerDoc.asp e informe o código do documento presente na tarjeta lateral.")
  pdf.ln(5)
  pdf.write(5, txt="5. Os dados constantes desta Certidão estão atualizados até 11/04/2019.")
  pdf.ln(5)
  pdf.write(5, txt="6. Certidão emitida gratuitamente.")

  pdf.ln(5)
  pdf.ln(5)

  pdf.cell(200, 5, txt="Natal/RN, " + dataRed + "     ", align="R", ln=1)

  pdf.output('./temp_pdf/' + nome_arquivo)

  return nome_arquivo 
