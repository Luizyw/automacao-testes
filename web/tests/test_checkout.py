from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_fluxo_compra():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.saucedemo.com/")

        wait.until(EC.element_to_be_clickable((By.ID, "user-name"))).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

        first_name = wait.until(EC.element_to_be_clickable((By.ID, "first-name")))
        last_name = wait.until(EC.element_to_be_clickable((By.ID, "last-name")))
        postal_code = wait.until(EC.element_to_be_clickable((By.ID, "postal-code")))

        first_name.clear()
        first_name.send_keys("Luiz")

        last_name.clear()
        last_name.send_keys("Felipe")

        postal_code.clear()
        postal_code.send_keys("64000")

        wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()

        wait.until(EC.url_contains("checkout-step-two"))

        wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

        mensagem = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
        ).text

        assert mensagem == "Thank you for your order!"

    finally:
        driver.quit()