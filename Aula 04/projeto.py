#!/usr/bin/env python
# coding: utf-8

# Importando Bibliotecas

# In[18]:


import os
import smtplib 
import shutil 
import pyautogui
import pywhatkit as kit
import win32com.client as win32
from time import sleep
from email.message import EmailMessage
from datetime import datetime


# Organizando aquivos

# In[3]:


arquivo_excel = 'contas_processadas.xlsx'
pasta_base = 'base'


# Verificando se o arquivo existe

# In[5]:


if not os.path.exists(arquivo_excel):
    raise FileNotFoundError("Arquivo não encontrado, verifique se o download está concluído.")
# raise modifica a mensagem do código de erro
print("Arquivo encontrado!")


# Criando a pasta base dentro da pasta Aula 04

# In[6]:


if not  os.path.exists(pasta_base):
    os.makedirs(pasta_base)
    print("Pasta criada com sucesso!")

else:
    print("Pasta base já existe!")


# Movendo arquivo para dentro da pasta Base

# In[8]:


destino = os.path.join(pasta_base, os.path.basename(arquivo_excel))

if not os.path.exists(destino):
    shutil.move(arquivo_excel, destino)
    print('Arquivo movido com sucesso!')

else:
    print('Arquivo já existe na pasta Base')
    


# Criando corpo do E-mail

# In[17]:


hoje = datetime.now().strftime("%d.%m.%Y | Hora: %H:%M")

corpo_email = f""" 
Prezados, 

Segue em anexo, o relatório de contas processadas do mês de Janeiro.
Data de processamento: {hoje}

Fico a disposição em caso de dúvidas.
"""


# Configurando Outlook

# In[21]:


outlook = win32.Dispatch('Outlook.Application')

email = outlook.CreateItem(0)

email.To = 'monique.batista@jadlog.com.br; leon4rdoalves@gmail.com'
email.Subject = 'Relatório Mensal - Contas Processadas - Janeiro/26.'
email.Body = corpo_email

email.attachments.Add(
    r"C:\Users\monique.batista\OneDrive - JADLOG LOGISTICA LTDA\Área de Trabalho\Hashtag\Aula 04\base\contas_processadas.xlsx"
)

email.Send()

print('E-mail enviado com sucesso!')


# Alerta Whatsapp

# In[24]:


telefone = '+5511977629825'

mensagem = 'Relatório enviado lá no e-mail!'

kit.sendwhatmsg_instantly(
    telefone,
    mensagem,
    wait_time=10, #ATÉ 20seg
    tab_close=False
)

sleep(2)

pyautogui.press('enter')
print("Mensagem Wpp enviada com sucesso!")


# Criando executável

# In[ ]:


# !pip install pyinstaller

get_ipython().system('jupyter nbconvert --to script projeto.ipynb')

# !pyinstaller --onefile projeto.py 

