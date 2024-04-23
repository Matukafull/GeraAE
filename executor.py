from selenium import webdriver

chrome_driver_path = r"C:\Users\SILVEIRAS\Desktop\DEV]\ALURA\Gerador de OS\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument('--disable-iinfobars')
driver= webdriver.Chrome(chrome_options=options)
driver.get("https://gss.aegea.com.br/")



print('Título da página: ', driver.title)
input("Pressione Enter para fechar o navegador")

driver.quit()

