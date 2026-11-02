from selenium import webdriver
from login_page import LoginPage

def test_ejecucion_pom():
    driver = webdriver.Chrome()
    try:
        login = LoginPage(driver)
        login.abrir()
        login.ingresar_credenciales("locked_out_user", "secret_sauce")
        login.click_login()
        print(f"Resultado de la prueba: {login.obtener_error()}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_ejecucion_pom()