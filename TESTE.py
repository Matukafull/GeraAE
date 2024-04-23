import pyautogui
import subprocess
import time
import subprocess
from unidades import Unidade
from App import Inicio

class Gerador: 


    # Caminho para o executável do Microsoft Edge
    edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"

    # URL da página que você deseja abrir
    url = "https://gss.aegea.com.br/ords/portal/aegea/r/portal/selecionar-unidade?session=12968390753485"

    # Abre o Microsoft Edge
    subprocess.Popen([edge_path, url])

    #Abrir unidade
    # Coordenadas do ponto onde você quer clicar
    x = 1500
    y = 1500
    #Coordenadas da seleção de unidades
    xuni = 1869
    yuni = 503

    #Coordenadas da aba opções na lateral
    xopc= 1387
    yopc=99

    #Coordenadas da aba atendimento
    xatend= 1467 
    yatend=225

    #Coordenadas da aba acatamento
    xacat= 1469 
    yacat=257

    #Coordenadas do botão NOVO
    xnovo= 2539
    ynovo= 651

    #Coordenadas da aba select
    xselect= 2078
    yselect= 262

    #Coordenadas da aba nome do cliente
    xnamegenos= 1586
    ynamegenos= 469

    #Coordenadas da aba endereço do cliente
    xendgenos= 1604
    yendgenos= 557

    #Coordenadas do botão 'próximo' na geração de OS
    xnextos= 2450
    ynextos= 634


    def gerar_os():
        time.sleep(7)
        # Localize a imagem na tela e obtenha as coordenadas
        pyautogui.press('tab')
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.write(self._unidade)
        time.sleep(1)
        pyautogui.press('enter')

        time.sleep(7)
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        #pyautogui.press('enter')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('right')
        pyautogui.press('down')
        pyautogui.press('enter')

        time.sleep(5)
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')

        time.sleep(5)
        pyautogui.click(x,y)
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.write('1')
        pyautogui.press('tab')
        pyautogui.write('1')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.write('1')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')                                                                                      
        pyautogui.press('enter')




        # Abrindo a unidade
        #time.sleep(2)
        # Faz um clique no local específico sem mover o mouse
        #pyautogui.click(xuni, yuni, duration=0)
        # Adicione um pequeno atraso antes de clicar (opcional)



