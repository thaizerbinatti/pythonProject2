from selenium import webdriver as webdriver
from selenium.webdriver.common.by import By
import pyautogui as action
import pyautogui as loadTime
import schedule
import time

# Tarefa Monday
def tarefaMonday():
    # Abre navegador
    navegadorFake = webdriver.Chrome()
    navegadorFake.get('https://totvs-torres.monday.com')
    loadTime.sleep(2)

    # Realiza login no navegador
    loginInput = navegadorFake.find_element(By.ID, 'user_email').send_keys('thatazerb@gmail.com')
    passwordInput = navegadorFake.find_element(By.ID, 'user_password').send_keys('thaina123')
    loadTime.sleep(2)
    loginButton = navegadorFake.find_element(By.CLASS_NAME, 'next-button-component').click()
    loadTime.sleep(8)

    # Entrando no quadro de implantação
    poolServiceButton = navegadorFake.find_element(By.CLASS_NAME, 'text-with-highlights').click()
    loadTime.sleep(8)

    # Selecionando o menu e mais ações
    menuButton = navegadorFake.find_element(By.XPATH,
                                            '/html/body/div[1]/div[4]/div[3]/div[2]/div[3]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/section[2]/div[7]/div/div/div/div/span').click()
    loadTime.sleep(8)
    actionsButton = navegadorFake.find_element(By.XPATH,
                                               '/html/body/span/div/div/div[1]/div[3]/div[4]/div/div/div/span').click()
    loadTime.sleep(8)

    # Exportando quadro para o excel
    buttonExcel = 'Exportar quadro para o Excel'
    openExcelButton = navegadorFake.find_element(By.XPATH, f'//*[text()="{buttonExcel}"]').click()
    loadTime.sleep(7)
    selectOption = 'Incluir Subelementos'
    checkoutButton = navegadorFake.find_element(By.XPATH, f'//*[text()="{selectOption}"]').click()
    loadTime.sleep(6)
    exportButton = navegadorFake.find_element(By.XPATH,
                                              '/html/body/div[55]/div/div/div/div/div/div/div[3]/button').click()
    loadTime.sleep(15)


# Agendando tarefa
schedule.every().monday.at("10:00").do(tarefaMonday)

# Looping para verificar tarefas
while True:
    schedule.run_pending()
    time.sleep(5)