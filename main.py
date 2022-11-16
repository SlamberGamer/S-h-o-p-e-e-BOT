from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("https://shopee.com.my/product/168114093/6184726748")

print(driver.title)

try:
    element = WebDriverWait(driver,100).until(
       EC.presence_of_element_located((By.CLASS_NAME, "language-selection__list"))
    )
    element.click()

    login = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.CLASS_NAME, "_3Kiuzg"))
    )
    login.click()

    username = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='loginKey']"))
    )
    username.send_keys("username")

    password = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
    )
    password.send_keys("pass")
    password.send_keys(Keys.RETURN)

    beli = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-solid-primary btn--l _3Kiuzg']"))
    )
    beli.click()

    SEMAK = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, "//div [@class='cart-page-footer cart-page-footer--overlap'] //button [@class='shopee-button-solid shopee-button-solid--primary ']"))
    )
    SEMAK.click()

finally:

    pesanan = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='_1OBq_Q AKriam'] //button"))
    )
    pesanan.click()

#username = driver.find_element_by_xpath("//input[@name='loginKey']")
#password = driver.find_element_by_xpath("")
#username.send_keys("test")
#password.send_keys("$axwE2CExW6wz9X")
#driver.find_element_by_name("1ruZ5a").click()

