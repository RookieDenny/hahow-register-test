from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.story("帳號字元小於4")
def test_accountnumberlimit():
    driver = openbrowser()
    registration_page(driver)
    driver.find_element(By.XPATH,value='/html/body/div[5]/div/div/div/div/div/form/div[1]/div/div/input').send_keys('123')
    hint = driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div/div/form/div[1]/div/div[2]').text
    assert hint == '限 4-21 碼小寫英文數字'

@allure.story("帳號已註冊過")
def test_usedaccount():
    driver = openbrowser()
    registration_page(driver)
    driver.find_element(By.XPATH,value='/html/body/div[5]/div/div/div/div/div/form/div[1]/div/div/input').send_keys('1234')
    sleep(4)
    hint = driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div/div/form/div[1]/div/div[2]').text
    assert hint == '此帳號已經註冊'
    

@allure.story("信箱格式錯誤")
def test_mailformat():
    driver = openbrowser()
    registration_page(driver)
    driver.find_element(By.XPATH,value='/html/body/div[5]/div/div/div/div/div/form/div[2]/div/div/input').send_keys('456')
    hint = driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div/div/form/div[2]/div/div[2]').text
    assert hint == '信箱格式有誤'

@allure.story("密碼字元小於8")
def test_password_limit():
    driver = openbrowser()
    registration_page(driver)
    driver.find_element(By.XPATH,value='/html/body/div[5]/div/div/div/div/div/form/div[3]/div/div/input').send_keys('789')
    hint = driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div/div/form/div[3]/div/div[2]').text
    assert hint == '限 8-24 碼英文數字符號！'

@allure.story("確認密碼錯誤")
def test_confirm_password():
    driver = openbrowser()
    registration_page(driver)
    driver.find_element(By.XPATH,value='/html/body/div[5]/div/div/div/div/div/form/div[3]/div/div[1]/input').send_keys('12345678')
    driver.find_element(By.XPATH,value='/html/body/div[5]/div/div/div/div/div/form/div[4]/div/div/input').send_keys('887')
    hint = driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div/div/form/div[4]/div/div[2]').text
    assert hint == '密碼不符，請再次確認'

@allure.step("openbrowser")
def openbrowser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://hahow.in/')
    driver.maximize_window()
    return driver
@allure.step("registration_page")
def registration_page(driver):
    login_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="header"]/nav/div/div[2]/div/ul[2]/li[2]')))
    login_element.click()
    register_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div/div/div/div/div/div[1]/div/button')))
    register_element.click()