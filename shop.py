import selenium.webdriver.support.expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://practice.automationtesting.in/"

def product_page_display():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(link)

    my_account_menu = driver.find_element_by_id("menu-item-50")
    my_account_menu.click()
    login_email = driver.find_element_by_id("username")
    login_email.send_keys("IvanovII052022@mail.ru")
    login_password = driver.find_element_by_id("password")
    login_password.send_keys("BeTesterBest052022+")
    btn_login = driver.find_element_by_css_selector("[name='login']")
    btn_login.click()
    check_logout = WebDriverWait(driver,5).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout > a"), "Logout")
    )
    shop_menu = driver.find_element_by_id("menu-item-40")
    shop_menu.click()
    html5_forms_book = driver.find_element_by_css_selector(".post-181 .woocommerce-LoopProduct-link")
    html5_forms_book.click()
    check_title_html5_forms = WebDriverWait(driver,5).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".product_title.entry-title"), "HTML5 Forms")
    )
    driver.quit()

def count_products_in_category():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(link)

    my_account_menu = driver.find_element_by_id("menu-item-50")
    my_account_menu.click()
    login_email = driver.find_element_by_id("username")
    login_email.send_keys("IvanovII052022@mail.ru")
    login_password = driver.find_element_by_id("password")
    login_password.send_keys("BeTesterBest052022+")
    btn_login = driver.find_element_by_css_selector("[name='login']")
    btn_login.click()
    check_logout = WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout > a"), "Logout")
    )
    shop_menu = driver.find_element_by_id("menu-item-40")
    shop_menu.click()
    cat_html = driver.find_element_by_css_selector(".cat-item-19 >a")
    cat_html.click()
    check_count_html = driver.find_elements(By.CSS_SELECTOR, ".product_cat-html")
    if len(check_count_html) != 3:
        print("Количество товаров HTML не равно 3")
    driver.quit()

def sorting_products():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(link)

    my_account_menu = driver.find_element_by_id("menu-item-50")
    my_account_menu.click()
    login_email = driver.find_element_by_id("username")
    login_email.send_keys("IvanovII052022@mail.ru")
    login_password = driver.find_element_by_id("password")
    login_password.send_keys("BeTesterBest052022+")
    btn_login = driver.find_element_by_css_selector("[name='login']")
    btn_login.click()
    check_logout = WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout > a"), "Logout")
    )
    shop_menu = driver.find_element_by_id("menu-item-40")
    shop_menu.click()
    selector_sort = driver.find_element_by_css_selector("[value='menu_order']")
    selector_sort_att = selector_sort.get_attribute("selected")
    if selector_sort_att is None:
        print("В селекторе не выбрано значение по умолчанию")
        driver.quit()
    select_max_to_min = Select(driver.find_element_by_class_name("orderby"))
    select_max_to_min.select_by_visible_text("Sort by price: high to low")
    selector_sort = driver.find_element_by_css_selector("[value='price-desc']")
    selector_sort_att = selector_sort.get_attribute("selected")
    if selector_sort_att is None:
        print("В селекторе не выбрано значение Sort by price: high to low")
        driver.quit()
    driver.quit()

def product_discount():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(link)

    my_account_menu = driver.find_element_by_id("menu-item-50")
    my_account_menu.click()
    login_email = driver.find_element_by_id("username")
    login_email.send_keys("IvanovII052022@mail.ru")
    login_password = driver.find_element_by_id("password")
    login_password.send_keys("BeTesterBest052022+")
    btn_login = driver.find_element_by_css_selector("[name='login']")
    btn_login.click()
    check_logout = WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout > a"), "Logout")
    )
    shop_menu = driver.find_element_by_id("menu-item-40")
    shop_menu.click()
    android_book = driver.find_element_by_class_name("product_cat-android")
    android_book.click()
    old_price = driver.find_element_by_css_selector(".price > del > span")
    assert old_price.text == "₹600.00", "Старая цена не равна 600.00"
    new_price = driver.find_element_by_css_selector(".price > ins > span")
    assert new_price.text == "₹450.00", "Новая цена не равна 450.00"
    click_image = driver.find_element_by_class_name("woocommerce-main-image")
    click_image.click()
    image_look = WebDriverWait(driver,5).until(
        EC.visibility_of_element_located((By.ID, 'fullResImage'))
    )
    wait_close_btn = WebDriverWait(driver,5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "pp_close"))
    )
    wait_close_btn.click()
    driver.quit()

def check_price_in_cart():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(link)

    shop_menu = driver.find_element_by_id("menu-item-40")
    shop_menu.click()
    btn_add = driver.find_element_by_css_selector("a[data-product_id='182']")
    btn_add.click()
    time.sleep(1)
    count = driver.find_element_by_css_selector('.wpmenucart-contents > span:nth-child(2)')
    price = driver.find_element_by_css_selector('.wpmenucart-contents > span:nth-child(3)')
    assert count.text == "1 Item" and price.text == "₹180.00", "Количество или цена не совападает"
    move_cart = driver.find_element_by_css_selector('a.wpmenucart-contents')
    move_cart.click()
    check_subtotal = WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal > td > span"), "₹180.00")
    )
    check_total = WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total > td > strong >span"), "₹189.00")
    )
    driver.quit()

def work_in_cart():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(link)

    shop_menu = driver.find_element_by_id("menu-item-40")
    shop_menu.click()
    btn_add = driver.find_element_by_css_selector("a[data-product_id='182']")
    btn_add.click()
    time.sleep(1)
    driver.execute_script("window.scrollBy(0,300);")
    btn_add2 = driver.find_element_by_css_selector("a[data-product_id='180']")
    btn_add2.click()
    time.sleep(1)
    move_cart = driver.find_element_by_css_selector('a.wpmenucart-contents')
    move_cart.click()
    delete_first = driver.find_element_by_css_selector("tr:nth-child(1) > td.product-remove > a")
    delete_first.click()
    time.sleep(2)
    undo_delete = driver.find_element_by_css_selector(".woocommerce-message > a")
    undo_delete.click()
    quantity_first = driver.find_element_by_css_selector("tr:nth-child(1) > td.product-quantity > div > input")
    quantity_first.clear()
    quantity_first.send_keys("3")
    btn_update = driver.find_element_by_css_selector('[name="update_cart"]')
    btn_update.click()
    time.sleep(2)
    quantity_first = driver.find_element_by_css_selector("tr:nth-child(1) > td.product-quantity > div > input")
    quantity_value = quantity_first.get_attribute("Value")
    assert quantity_value == "3", "Количество элементов не равно 3"
    time.sleep(1)
    btn_apply_coupon = driver.find_element_by_css_selector('[name="apply_coupon"]')
    btn_apply_coupon.click()
    check_total = WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-error > li"), "Please enter a coupon code.")
    )
    driver.quit()

def buy_product():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(link)

    shop_menu = driver.find_element_by_id("menu-item-40")
    shop_menu.click()
    driver.execute_script("window.scrollBy(0,300);")
    btn_add = driver.find_element_by_css_selector("a[data-product_id='181']")
    btn_add.click()
    time.sleep(1)
    move_cart = driver.find_element_by_css_selector('a.wpmenucart-contents')
    move_cart.click()
    time.sleep(1)
    proceed_to_checkout = WebDriverWait(driver,5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".wc-proceed-to-checkout > a"))
    )
    proceed_to_checkout.click()
    first_name = WebDriverWait(driver,5).until(
        EC.visibility_of_element_located((By.ID, "billing_first_name"))
    )
    first_name.send_keys("Ivan")
    last_name = driver.find_element_by_id("billing_last_name")
    last_name.send_keys("Ivanov")
    email = driver.find_element_by_id("billing_email")
    email.send_keys("IvanovII052022@mail.ru")
    phone = driver.find_element_by_id("billing_phone")
    phone.send_keys("89999999999")
    select = driver.find_element_by_id("s2id_billing_country")
    select.click()
    search_select = driver.find_element_by_id("s2id_autogen1_search")
    search_select.send_keys("Russia")
    select_result = driver.find_element_by_id("select2-results-1")
    select_result.click()
    street_adress = driver.find_element_by_id("billing_address_1")
    street_adress.send_keys("Лунина, 125")
    city = driver.find_element_by_id("billing_city")
    city.send_keys("Москва")
    state = driver.find_element_by_id("billing_state")
    state.send_keys("Московская область")
    postcode = driver.find_element_by_id("billing_postcode")
    postcode.send_keys("525452")
    driver.execute_script("window.scrollBy(0,600);")
    time.sleep(2)
    check_payment = driver.find_element_by_id("payment_method_cheque")
    check_payment.click()
    btn_place_order = driver.find_element_by_id("place_order")
    btn_place_order.click()
    check_total = WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received.")
    )
    check_total = WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "li.method > strong"), "Check Payments")
    )
    driver.quit()

product_page_display()
count_products_in_category()
sorting_products()
product_discount()
check_price_in_cart()
work_in_cart()
buy_product()