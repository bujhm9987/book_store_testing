from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://practice.automationtesting.in/")
    driver.implicitly_wait(5)

    driver.execute_script("window.scrollBy(0,600);")
    btn_selenium_ruby=driver.find_element_by_css_selector("#text-22-sub_row_1-0-2-0-0 a.button")
    btn_selenium_ruby.click()
    btn_reviews=driver.find_element_by_css_selector(".woocommerce-tabs .reviews_tab")
    btn_reviews.click()
    fifth_star=driver.find_element_by_class_name("star-5")
    fifth_star.click()
    review_text=driver.find_element_by_id("comment")
    review_text.send_keys("Nice book!")
    name_input=driver.find_element_by_id("author")
    name_input.send_keys("Ivan")
    name_input=driver.find_element_by_id("email")
    name_input.send_keys("IvanovII@mail.ru")
    name_input=driver.find_element_by_id("submit")
    name_input.click()


finally:
    time.sleep(5)
    driver.quit()
