from selenium import webdriver
import unittest, time, re
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import datetime
from datetime import timedelta
import os

ftest44Link = "https://stage.fabrtech.ru/"

#Настраиваем webdriver и браузер, подключаем плагин ЭЦП к запускаемому браузеру
options = webdriver.ChromeOptions()
options.add_extension('C:/chromedriver/extension_1_2_13_0.crx')
browser = webdriver.Chrome(options=options)
browser.set_window_size(1920, 1080)
browser.get(ftest44Link)

try:
    #Начало авторизации по ЭЦП
    autorizationWindow = browser.find_element(By.XPATH, value='//*[@id="btnLoginModal"]')
    autorizationWindow.click()
    time.sleep(2)

    sertificate = browser.find_element(By.XPATH, value='//*[@id="sert"]/div[1]/div/fieldset/div/table/tbody/tr[3]/td[1]/div/label/span[1]')
    sertificate.click()

    button = browser.find_element(By.XPATH, value='//*[@id="loginModal"]/div/div/div[3]/div[1]/div[2]/button')
    button.click()
    time.sleep(7)

    customer = browser.find_element(By.XPATH, value='//*[@id="row-4"]/td[3]/div/label/span[1]')
    customer.click()
    time.sleep(5)
    button = browser.find_element(By.XPATH, value='//*[@id="login-ambiguous-ecp-buttonWrapper-element"]/input')
    button.click()
    time.sleep(5)
    #Конец авторизации по ЭЦП

    dateToday = (datetime.datetime.now()) + datetime.timedelta(days=4) #Расчеты дат для ДОПЗ
    dateTodayStr = dateToday.strftime("%d.%m.%Y %H:%M")
    dateFuture = dateToday + datetime.timedelta(days=5)
    dateFutureStr = dateFuture.strftime("%d.%m.%Y")
    dateFutureNext = dateToday + datetime.timedelta(days=10)
    dateFutureNextStr = dateFutureNext.strftime("%d.%m.%Y")

    #Старт создания процедуры ЗМО
    linkZMO = browser.find_element(By.XPATH, value='//*[@id="CustomerCatalog44"]/div[1]/div[1]/div[3]/div/a') #Открытие формы создания извещения
    linkZMO.click()

    procedureName = browser.find_element(By.XPATH, value='//*[@id="common-info-name"]') #Заполнение извещения и лота
    procedureName.send_keys('Закупка радиоактивных крыс')
    price = browser.find_element(By.XPATH, value='//*[@id="common-info-maxSum"]')
    price.send_keys('590000')
    OKPD2 = browser.find_element(By.XPATH, value='//*[@id="common-items-0-okpd2-okpd2"]')
    OKPD2.click()
    time.sleep(3)
    OKPD2Choose = browser.find_element(By.XPATH, value='//*[@id="rowId-8873882"]/td[1]/div/label/span[1]')
    OKPD2Choose.click()
    OKPD2Btn = browser.find_element(By.XPATH, value='/html/body/div[7]/div/div/div[3]/button[2]')
    OKPD2Btn.click()
    lotName = browser.find_element(By.XPATH, value='//*[@id="common-items-0-okpd2-name"]')
    lotName.send_keys('Крыса радиоактивная')
    lotCount = browser.find_element(By.XPATH, value='//*[@id="row-0"]/td[2]/input')
    lotCount.send_keys('5')
    time.sleep(2)
    lotType = Select(browser.find_element(By.XPATH, value='//*[@id="common-items-0-okpd2-type"]'))
    lotType.select_by_visible_text('Товар')
    measure = browser.find_element(By.XPATH, value='//*[@id="common-items-0-okpd2-okei"]')
    measure.click()
    time.sleep(4)
    measureChoose = browser.find_element(By.XPATH, value='//*[@id="rowId-506"]/td[1]/div/label/span[1]')
    measureChoose.click()
    measureBtn = browser.find_element(By.XPATH, value='/html/body/div[7]/div/div/div[3]/button[2]')
    measureBtn.click()

    dateEnd = browser.find_element(By.XPATH, value='//*[@id="common-terms-requestEndDateTime"]') #Даты ДОПЗ и протоколов
    dateEnd.send_keys(dateTodayStr)
    dateResults = browser.find_element(By.XPATH, value='//*[@id="common-terms-sumDefinitionSupplierDateTime"]')
    dateResults.send_keys(dateFutureStr)
    dateContract = browser.find_element(By.XPATH, value='//*[@id="common-terms-planContractDateTime"]')
    dateContract.send_keys(dateFutureNextStr)

    deliveryPlace = browser.find_element(By.XPATH, value='//*[@id="common-delivery-place"]')
    deliveryPlace.send_keys('Цитадель зла')
    deliveryShedule = browser.find_element(By.XPATH, value='//*[@id="common-delivery-schedule"]')
    deliveryShedule.send_keys('Семь дней')
    cash = browser.find_element(By.XPATH, value='//*[@id="common-delivery-paymentCondition"]')
    cash.send_keys('Наличными крупными купюрами')

    # Добавление док-ов, необязательно
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    docsName = browser.find_element(By.XPATH, value='//*[@id="row-0"]/td[1]/input')
    docsName.send_keys('Стопка документов')
    docs = browser.find_element(By.XPATH, value='//*[@id="row-0"]/td[2]/div/input[1]')
    docs.send_keys(file_path)
    docsSend = browser.find_element(By.XPATH, value='//*[@id="row-0"]/td[2]/div/button[1]')
    docsSend.click()
    time.sleep(10)
    #Конец заполнения извещения

    #Публикация и подписание извещения ЭЦП
    publicate = browser.find_element(By.XPATH, value='//*[@id="common-resultButtons-element"]/input[2]')
    publicate.click()
    time.sleep(5)
    acknowledgement = browser.find_element(By.XPATH, value='/html/body/div[7]/div/div/div[3]/button')
    acknowledgement.click()

finally:
    time.sleep(40)
    browser.quit()
