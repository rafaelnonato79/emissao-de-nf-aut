#Emissão de nota fiscal automatizada

import time
import pyautogui

#pausar o programa no tempo determinado
from time import sleep

#138,513
#90,567
#460,718

#Colocando dados na variavel
with open('arquivo.txt','r') as arquivo:
    for linha in arquivo:
        cnpj = linha.split(';')[0]
        procedimento = linha.split(';')[1]
        qtd = linha.split(';')[2]
        valor = linha.split(';')[3]
        paciente = linha.split(';')[4]

        #clicar no nota natalense
        pyautogui.click(138,513,duration=1)

        #mover mouse para operações
        pyautogui.moveTo(90,567,duration=1)

        #mover mouse para direita
        pyautogui.moveTo(270,569,duration=1)

        #clicar em emissão de nf
        pyautogui.click(460,718,duration=1)

        #descer a barra de rolagem para mostrar a tela completa de emissão de nf
        pyautogui.scroll(-180)

        #clicar em proximo
        pyautogui.click(682,652,duration=1)

        #clicar em informar cpf/cnpj
        pyautogui.click(570,240,duration=1)

        #clicar em campo de digitar cnpj
        pyautogui.click(619,288,duration=1)

        #escrever o cnpj
        pyautogui.write(cnpj)
        pyautogui.press('enter')

        #proximo
        pyautogui.click(687,639,duration=1)   

        #natureza da operação
        pyautogui.click(1043,285,duration=1)
        pyautogui.click(337,371,duration=1)

        #item de lista de serviço
        pyautogui.click(1047,417,duration=1)
        pyautogui.write('4.03')
        pyautogui.click(922,459,duration=0.2)

        #codigo de atividade
        pyautogui.click(1043,522,duration=1)
        pyautogui.click(887,563,duration=1)
        pyautogui.click(701,644,duration=1)

        #discriminação do serviço
        pyautogui.click(514,297,duration=0.5)
        pyautogui.write(procedimento)
        pyautogui.press('tab')
        pyautogui.write(qtd)
        pyautogui.press('tab')
        pyautogui.write(valor)

        #incluir
        pyautogui.click(737,394,duration=0.5)
        #ISS retido
        pyautogui.click(424,613,duration=1)
        #proximo
        pyautogui.click(684,657,duration=0.5)

        #outras informações
        pyautogui.click(336,517,duration=0.5)
        pyautogui.write(paciente)
        pyautogui.click(684,647,duration=1)

        #gerar nota fiscal 

        #salvar a nota fiscal na pasta correta
        #utilizar o nome da prefeitura para pesquisar a pasta, clicar na pasta e salvar de acordo com o numero da nota fiscal
        #fechar pagina de nota fiscal e guia no navegador

        #colocar na planilha os dados da nota fiscal emitida

        #voltar para o directa,  dar refresh e emitir nova nota fiscal
        time.sleep(10)
        pyautogui.press('f5')