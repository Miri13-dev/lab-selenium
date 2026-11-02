from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_page import LoginPage

def test_login_exitoso(driver):
    login = LoginPage(driver)
    login.abrir()
    login.ingresar_credenciales("standard_user", "secret_sauce")
    login.click_login()
    assert "inventory.html" in driver.current_url

def test_agregar_al_carrito(driver):
    login = LoginPage(driver)
    login.abrir()
    login.ingresar_credenciales("standard_user", "secret_sauce")
    login.click_login()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
    badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    assert badge.text == "1"

def test_login_fallido(driver):
    login = LoginPage(driver)
    login.abrir()
    login.ingresar_credenciales("locked_out_user", "secret_sauce")
    login.click_login()
    assert "locked out" in login.obtener_error()