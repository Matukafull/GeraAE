import pyautogui
import subprocess
import time
import subprocess

# Caminho para o executável do Microsoft Edge
edge_path = "C://Program Files (x86)//Microsoft//Edge//Application//msedge.exe"

# URL da página que você deseja abrir
url = "https://gss.aegea.com.br/ords/portal/aegea/r/portal/selecionar-unidade?session=12968390753485"

# Abre o Microsoft Edge
subprocess.Popen([edge_path, url])

#Abrir unidade
# Coordenadas do ponto onde você quer clicar
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

time.sleep(7)
# Localize a imagem na tela e obtenha as coordenadas
button_location = pyautogui.locateOnScreen("C:/Users/SILVEIRAS/Desktop/DEV]/ALURA/Gerador de OS/IMG/.log.png")

if button_location is not None:
    # Obtenha o centro do botão
    button_center = pyautogui.center(button_location)
    pyautogui.write('guariroba')
    time.sleep(2)
    pyautogui.press('enter')
    
    # Clique no centro do botão
    pyautogui.click(button_center.x, button_center.y)
else:
    print("Imagem não encontrada na tela.")

time.sleep(3)

## Para abrir o menu opções
button_location = pyautogui.locateOnScreen("C:/Users/SILVEIRAS/Desktop/DEV]/ALURA/Gerador de OS/IMG/.opcoes")

if button_location is not None:
    # Obtenha o centro do botão
    button_center = pyautogui.center(button_location)
    pyautogui.write('guariroba')
    time.sleep(2)
    pyautogui.press('enter')
    
    # Clique no centro do botão
    pyautogui.click(button_center.x, button_center.y)
else:
    print("Imagem não encontrada na tela.")

time.sleep(2)

##Para abrir o menu atendimento
button_location = pyautogui.locateOnScreen("C:/Users/SILVEIRAS/Desktop/DEV]/ALURA/Gerador de OS/IMG/.atendimento")

if button_location is not None:
    # Obtenha o centro do botão
    button_center = pyautogui.center(button_location)
    pyautogui.write('guariroba')
    time.sleep(2)
    pyautogui.press('enter')
    
    # Clique no centro do botão
    pyautogui.click(button_center.x, button_center.y)
else:
    print("Imagem não encontrada na tela.")

time.sleep(2)

# Abrindo ACATAMENTO

button_location = pyautogui.locateOnScreen("C:/Users/SILVEIRAS/Desktop/DEV]/ALURA/Gerador de OS/IMG/.acatamento")

if button_location is not None:
    # Obtenha o centro do botão
    button_center = pyautogui.center(button_location)
    pyautogui.write('guariroba')
    time.sleep(2)
    pyautogui.press('enter')
    
    # Clique no centro do botão
    pyautogui.click(button_center.x, button_center.y)
else:
    print("Imagem não encontrada na tela.")

time.sleep(2)

# Gerando a OS
button_location = pyautogui.locateOnScreen("C:/Users/SILVEIRAS/Desktop/DEV]/ALURA/Gerador de OS/IMG/.geraros")

if button_location is not None:
    # Obtenha o centro do botão
    button_center = pyautogui.center(button_location)
    pyautogui.write('guariroba')
    time.sleep(2)
    pyautogui.press('enter')
    
    # Clique no centro do botão
    pyautogui.click(button_center.x, button_center.y)
else:
    print("Imagem não encontrada na tela.")

time.sleep(2)

# Botao Origem da solicitação
button_location = pyautogui.locateOnScreen("C:/Users/SILVEIRAS/Desktop/DEV]/ALURA/Gerador de OS/IMG/.origemdasolicitacao")

if button_location is not None:
    # Obtenha o centro do botão
    button_center = pyautogui.center(button_location)
    pyautogui.write('guariroba')
    time.sleep(2)
    pyautogui.press('enter')
    
    # Clique no centro do botão
    pyautogui.click(button_center.x, button_center.y)
else:
    print("Imagem não encontrada na tela.")
time.sleep(1)
pyautogui.write('1')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
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

# Tela de por matrícula
time.sleep(1)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write('17904869')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')

# Hora de gerar OS
time.sleep(1)
pyautogui.press('tab')
pyautogui.write('119002')
time.sleep(1)
pyautogui.press('enter')


# Captura as coordenadas atuais do cursor do mouse
x, y = pyautogui.position()

# Exibe as coordenadas
#print(f"Coordenadas do mouse: (x: {x}, y: {y})")
#pyautogui.displayMousePosition()




