from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

def ejecutar_pruebas():
    try:
        # --- CASO 1: Login exitoso ---
        print("Ejecutando Caso 1: Login...")
        driver.get("https://www.saucedemo.com")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        assert "inventory.html" in driver.current_url
        print("✅ Caso 1 completado con éxito.")

        # --- CASO 2: Agregar al carrito ---
        print("Ejecutando Caso 2: Agregar producto...")
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert badge == "1"
        print("✅ Caso 2 completado con éxito.")

        # --- CASO 3: Login fallido (usuario bloqueado) ---
        print("Ejecutando Caso 3: Login fallido...")
        driver.delete_all_cookies()
        driver.get("https://www.saucedemo.com")
        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        # CORRECCIÓN: By.DATA_TEST no existe, se usa un selector CSS
        error_msg = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        assert "Sorry, this user has been locked out" in error_msg
        print("✅ Caso 3 completado con éxito.")

    except Exception as e:
        print(f"❌ Error durante la ejecución: {e}")
    finally:
        driver.quit()

ejecutar_pruebas()