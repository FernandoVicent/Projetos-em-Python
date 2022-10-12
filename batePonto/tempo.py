import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium import webdriver

# hora = time.localtime()
# print(hora)

while 1:
    hora = time.localtime()
    #print("agora são", + hora[3], "e", + hora[4])


    if hora[3] == 13 and hora[4] == 0:
        #------------ENTRADA-------------------
        navegador = webdriver.Chrome()

        # --------------------LOGAR-----------------------------------------------
        navegador.get("http://www.outsourcing.prodesp.sp.gov.br/login.aspx")
        navegador.find_element_by_xpath('//*[@id="txtUsuario"]').send_keys("49093405802")
        navegador.find_element_by_xpath('//*[@id="txtSenha"]').send_keys("Fer-1092")
        navegador.find_element_by_xpath('//*[@id="btnEntrar"]').click()
        time.sleep(2)
        # --------------------------------entrada 13:00------------------------

        navegador.find_element(By.XPATH, '//*[@id="MainContent_btnTarefas"]').click()

        dropdown2 = navegador.find_element(By.XPATH, '//*[@id="MainContent_ddlAtividade"]')
        dd2 = Select(dropdown2)
        dd2.select_by_visible_text("Suporte a Estações de Trabalho e Equipamentos de TI (Instalação,Configuração, Análise e Diagnóstico)")

        navegador.find_element(By.XPATH, '//*[@id="MainContent_btnIniciar"]').click()
        break

    if hora[3] == 17 and hora[4] == 0:

        #--------------ALMOÇO---------------------------------
        navegador = webdriver.Chrome()

        navegador.get("http://www.outsourcing.prodesp.sp.gov.br/login.aspx")
        navegador.find_element_by_xpath('//*[@id="txtUsuario"]').send_keys("49093405802")
        navegador.find_element_by_xpath('//*[@id="txtSenha"]').send_keys("Fer-1092")
        navegador.find_element_by_xpath('//*[@id="btnEntrar"]').click()
        time.sleep(2)

        navegador.find_element(By.XPATH, '//*[@id="MainContent_btnTarefas"]').click()
        navegador.find_element_by_xpath('//*[@id="MainContent_btnFinalizar"]').click()
        break

    if hora[3] == 18 and hora[4] == 0:
        #------------VOLTA-----------------------
        navegador = webdriver.Chrome()

        # --------------------LOGAR-----------------------------------------------
        navegador.get("http://www.outsourcing.prodesp.sp.gov.br/login.aspx")
        navegador.find_element(By.XPATH,'//*[@id="txtUsuario"]').send_keys("49093405802")
        navegador.find_element(By.XPATH,'//*[@id="txtSenha"]').send_keys("Fer-1092")
        navegador.find_element(By.XPATH,'//*[@id="btnEntrar"]').click()
        time.sleep(2)

        # --------------------------------entrada 18:00------------------------

        navegador.find_element(By.XPATH, '//*[@id="MainContent_btnTarefas"]').click()

        dropdown2 = navegador.find_element(By.XPATH, '//*[@id="MainContent_ddlAtividade"]')
        dd2 = Select(dropdown2)
        dd2.select_by_visible_text("Suporte a Estações de Trabalho e Equipamentos de TI (Instalação,Configuração, Análise e Diagnóstico)")

        navegador.find_element(By.XPATH, '//*[@id="MainContent_btnIniciar"]').click()
        break


    if hora[3] == 22 and hora[4] == 0:
        # --------------Saída---------------------------------
        navegador = webdriver.Chrome()

        navegador.get("http://www.outsourcing.prodesp.sp.gov.br/login.aspx")
        navegador.find_element(By.XPATH, '//*[@id="txtUsuario"]').send_keys("49093405802")
        navegador.find_element(By.XPATH, '//*[@id="txtSenha"]').send_keys("Fer-1092")
        navegador.find_element(By.XPATH, '//*[@id="btnEntrar"]').click()
        time.sleep(2)
        navegador.find_element(By.XPATH, '//*[@id="MainContent_btnTarefas"]').click()
        navegador.find_element(By.XPATH, '//*[@id="MainContent_btnFinalizar"]').click()
        break
