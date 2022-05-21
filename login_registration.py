from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

try:
    link = "http://practice.automationtesting.in/"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(link)
    driver.implicitly_wait(5)

    my_account_menu = driver.find_element_by_id("menu-item-50")   #Registration
    my_account_menu.click()
    reg_email = driver.find_element_by_id("reg_email")
    reg_email.send_keys("IvanovII052022@mail.ru")
    reg_password = driver.find_element_by_id("reg_password")
    reg_password.send_keys("BeTesterBest052022+")
    btn_register = driver.find_element_by_css_selector("[name='register']")
    btn_register.click()

    driver.get(link)    #Login
    my_account_menu = driver.find_element_by_id("menu-item-50")
    my_account_menu.click()
    login_email = driver.find_element_by_id("username")
    login_email.send_keys("IvanovII052022@mail.ru")
    login_password = driver.find_element_by_id("password")
    login_password.send_keys("BeTesterBest052022+")
    btn_login = driver.find_element_by_css_selector("[name='login']")
    btn_login.click()
    check_logout=WebDriverWait(driver,10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout > a"), "Logout")
    )

finally:
    time.sleep(3)
    driver.quit()
