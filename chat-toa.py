import os
import time
import winsound
import tkinter as tk
from datetime import datetime
from selenium import webdriver
import selenium.webdriver.chrome.options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

## cd C:\Program Files\Google\Chrome\Application

## cd C:\Program Files (x86)\Google\Chrome\Application
## chrome.exe --remote-debugging-port=9222 --user-data-dir=C:\Py\ChromeProfile
 

#service = Service()
#options = webdriver.ChromeOptions()
#options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
#driver = webdriver.Chrome(service=service, options=options)
#wait = WebDriverWait(driver, 10)

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10)


driver.get('https://clarosa.etadirect.com/mobility/')
guia_remedy = driver.window_handles[0]

print('Carregando o navegador, aguarde!')
time.sleep(10)

msg = ''
selecionafila = ''
nome_fila = ''
nome_fila_final = []
filas = ''
filas_final = []
menu_status = ['','','','','','','','','','','']

while driver.title == 'Oracle Field Service':
    print("Por gentileza faça o login no TOA e maximize a lista de chat's")
    time.sleep(5)


def msg_toa():
    hora_atual = datetime.now().hour
    global msg
    if hora_atual < 12:
        msg = 'Bom dia, um momento que já lhe atendo'
    elif 12 <= hora_atual < 18:
        msg = 'Boa tarde, um momento que já lhe atendo'
    else:
        msg = 'Boa noite, um momento que já lhe atendo'
    return msg


def menu_chat_toa(selecionafila,nome_fila,nome_fila_final,filas,filas_final,menu_status):
    selecionafila = ''
    while selecionafila != 'OK':
        print('\nEis a fila selecionada:',nome_fila_final)
        selecionafila = input(f'FILAS:\n     1-INFRA SPC1 - CAPITAL {menu_status[0]}\n     2-OMR SP1 - CAPITAL {menu_status[1]}\n     3-INFRA SPC2 - INTERIOR {menu_status[2]}\n     4-OMR SP2 - INTERIOR {menu_status[3]}\n     5-INFRA - PR/SC {menu_status[4]}\n     6-OMR - PR {menu_status[5]}\n     7-OMR - SC {menu_status[6]}\n     8-INFRA - RS {menu_status[7]}\n     9-OMR - RS {menu_status[8]}\n     10-OMR - NO {menu_status[9]}\n    \nDigita o número da fila desejada ou OK para iniciar:').upper()

    
        if selecionafila in ['1','2','3','4','5','6','7','8','9','10']:

            if selecionafila == '1':
                filas = ('//*[@id="h:824@clarosa"]/div')
                nome_fila = ('INFRA SP1 - CAPITAL')


            elif selecionafila == '2':
                filas = ('//*[@id="h:775@clarosa"]/div')
                nome_fila = ('COP REDE MOVEL SP1 - CAPITAL')

            elif selecionafila == '3':
                filas = ('//*[@id="h:844@clarosa"]/div')
                nome_fila = ('INFRA SP2 - INTERIOR')
    
            elif selecionafila == '4':
                filas = ('//*[@id="h:776@clarosa"]/div')
                nome_fila = ('COP REDE MOVEL SP2 - INTERIOR')

            elif selecionafila == '5':
                filas = ('//*[@id="h:854@clarosa"]/div')
                nome_fila = ('INFRA SUL PR SC HELPDESK')

            elif selecionafila == '6':
                filas = ('//*[@id="h:771@clarosa"]/div')
                nome_fila = ('COP REDE MOVEL PR')

            elif selecionafila == '7':
                filas = ('//*[@id="h:774@clarosa"]/div')
                nome_fila = ('COP REDE MOVEL SC')

            elif selecionafila == '8':
                filas = ('//*[@id="h:856@clarosa"]/div')
                nome_fila = ('INFRA SUL RS')

            elif selecionafila == '9':
                filas = ('//*[@id="h:773@clarosa"]/div')
                nome_fila = ('COP REDE MOVEL RS')

            elif selecionafila == '10':
                filas = ('//*[@id="h:770@clarosa"]/div')
                nome_fila = ('COP REDE MOVEL NO')


            if filas not in filas_final:
                filas_final.append(filas)
                nome_fila_final.append(nome_fila)
                menu_status[(int(selecionafila)-1)] = '>>>>>> ADICIONADO <<<<<<'
    
            else:
                filas_final.remove(filas)
                nome_fila_final.remove(nome_fila)
                menu_status[(int(selecionafila)-1)] = ''

        else:
            if selecionafila == 'OK':
                return

            else:
                os.system('cls')
                print('\nNão identificado opção na fila"',selecionafila,'"por gentileza digite novamente!')


menu_chat_toa(selecionafila,nome_fila,nome_fila_final,filas,filas_final,menu_status)
 

while True:

    try:
        chatpendente = ''


        if driver.find_element(By.XPATH, '//*[@id="activeChatsTabHead"]/div/span[1]').is_displayed() == True and driver.find_element(By.XPATH, '//*[@id="community-scroll-box-wrapper"]').is_displayed() == True:
            while chatpendente == '':
                chatpendente = driver.find_element(By.XPATH,'//span[@id="helpdeskChatsCounter"]').text
                time.sleep(2)
                print(time.ctime(),'Desenvolvido por Daniel Ledezma Vieira - Ltda© \n\nAguardando Chat da filas: ',nome_fila_final)

            if chatpendente != '':
                driver.find_element(By.ID, 'helpdeskChatsCounter').click()  # clica no 'HelpDesk'
                time.sleep(0.3)

                for n,fila in enumerate(filas_final):
                    driver.find_element(By.XPATH, fila).click()  # CHAT PENDENTE CENTRO
                    time.sleep(0.5)

                    verifica_chat = driver.find_element(By.XPATH, '//*[@id="community-chat-list"]/div[1]').text
                    if verifica_chat != 'Nenhuma conversa em espera no momento':
                        time.sleep(2)
                        driver.find_element(By.XPATH, '//*[@id="community-chat-list"]/div[1]').click()#clica na conversa
                        time.sleep(2)
                        chat_a_ser_puxado = driver.find_element(By.XPATH, '//*[@id="title-text"]').text #pega o nome da conversa            
                        print('chat_a_ser_puxado:',chat_a_ser_puxado)
                        driver.find_element(By.XPATH, '//*[@id="community-helpdesk-take-chat-button"]').click() #entra na conversa
                        time.sleep(2)
                        #driver.find_element(By.XPATH, '//*[@id="activeChatsTabHead"]/div/span[1]').click()#aba chats abertos
                        time.sleep(2)
                        chat_na_lista_abertos = driver.find_element(By.XPATH, '//*[@id="community-chat-list"]/div[1]//*[@class="community-chat-title ellipsis"]').text#nome do chat na lista
                        nome_chat_atual = driver.find_element(By.XPATH, '//*[@id="community-chat-title"]').text #nome do da pessoa no chat que será enviado a msg
                        msg = msg_toa()
                        driver.find_element(By.ID, 'community-msg-text').send_keys(msg,Keys.ENTER)
                        print('chat_na_lista_abertos',chat_na_lista_abertos)
                        print('nome_chat_atual',nome_chat_atual)

        else:
            os.system('cls')
            winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
            print('LISTA DE CHATS NÃO ESTÁ MAXIMIZADA, POR GENTILEZA MAXIME E DIGITE OK!') 
            menu_chat_toa(selecionafila,nome_fila,nome_fila_final,filas,filas_final,menu_status)   

 

    except:
        print('talvez tenha bugado :/ foi mal')
        time.sleep(2)
        if driver.find_element(By.XPATH, '//*[@id="activeChatsTabHead"]/div/span[1]').is_displayed() == False or driver.find_element(By.XPATH, '//*[@id="community-scroll-box-wrapper"]').is_displayed() == False:
            os.system('cls')
            winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
            print('LISTA DE CHATS NÃO ESTÁ MAXIMIZADA, POR GENTILEZA MAXIME E DIGITE OK!!')
            menu_chat_toa(selecionafila,nome_fila,nome_fila_final,filas,filas_final,menu_status)

 

#ESSE ANTES DE CLICAR EM ENTRAR

#NOME DO CHAT ANTES DE PUXAR? #ANTES DE ENTRAR OK

## TITULO #//*[@id="title-text"]

 

#ESSE PRA CAÇAR O NOME NA LISTA

#LISTA DE CHAT PUXADO

##titulo #//*[@id="community-chat-list"]/div[1]//*[@class="community-chat-title ellipsis"]

 

#ESSE PRA VALIDAR COM O NOME ANTERIOR

#CHAT ABERTO

#@TITULO SEM ABREVIAÇÃO #//*[@id="community-chat-title"]

 

 

 

##salva toda a lista de chat em aberto (nome, abreviação e texto que aparece)

#driver.find_element(By.XPATH, '//*[@id="community-ch