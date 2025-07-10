from warnings import catch_warnings
import pyautogui
import random
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = uc.ChromeOptions()

options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-browser-side-navigation")


driver = uc.Chrome(options=options)


driver.execute_script("window.open('https://rateyourmusic.com/film_collection/Basurero/r0.5-5.0', '_blank')")
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])


import undetected_chromedriver as uc
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pyautogui
import random
import time

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

class SecurityBypass:
    """
    Handles security-related interactions such as bypassing captchas and accepting cookie popups.
    In this implementation, we simulate a physical click on the captcha checkbox using pyautogui,
    calculating its screen coordinates dynamically to avoid the use of fixed positions.
    """

    def __init__(self, driver: uc.Chrome, wait: WebDriverWait) -> None:
        """
        Initialize the SecurityBypass with a Selenium driver and its associated wait helper.
        
        :param driver: An instance of undetected_chromedriver.Chrome.
        :param wait: A WebDriverWait instance for managing dynamic waits.
        """
        self.driver = driver
        self.wait = wait

    def bypass_captcha(self) -> None:
        """
        Attempts to bypass the captcha by:
          1. Switching into the captcha iframe.
          2. Locating the captcha checkbox element.
          3. Calculating its center coordinates relative to the screen.
          4. Using pyautogui to physically move the mouse to that position and click.
          
        Adjust the selectors as needed based on the captcha's actual structure.
        """
        try:
            logging.info("Attempting captcha bypass with physical click simulation.")

            # Wait for the captcha iframe (typical for Google reCAPTCHA v2) and switch to it.
            self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src*='api2/anchor']")))
            logging.info("Switched to captcha iframe.")

            # Wait for the captcha checkbox element to be visible.
            checkbox = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.recaptcha-checkbox-border")))
            logging.info("Captcha checkbox element located.")

            # Ensure the element is scrolled into view and retrieve its location and size.
            location = checkbox.location_once_scrolled_into_view  # {'x': ..., 'y': ...}
            size = checkbox.size  # {'width': ..., 'height': ...}
            logging.info(f"Checkbox location (viewport): {location} with size: {size}")

            # Compute the center of the checkbox in viewport coordinates.
            element_center_x = location['x'] + size['width'] / 2
            element_center_y = location['y'] + size['height'] / 2
            logging.info(f"Element center in viewport: ({element_center_x}, {element_center_y})")

            # Get the browser window's position on the screen.
            # Note: get_window_position() returns the top-left coordinates of the browser window.
            window_position = self.driver.get_window_position()
            logging.info(f"Browser window position (screen): {window_position}")

            # Calculate the absolute screen coordinates for the element's center.
            # Es importante que la ventana del navegador esté en primer plano.
            # Dependiendo del entorno, quizá debas ajustar el offset (por ejemplo, si existe una barra de título).
            screen_x = window_position['x'] + element_center_x
            screen_y = window_position['y'] + element_center_y
            logging.info(f"Calculated screen coordinates for click: ({screen_x}, {screen_y})")

            # Simulate a physical mouse movement and click using pyautogui.
            move_duration = random.uniform(0.5, 1.5)
            pyautogui.moveTo(screen_x, screen_y, duration=move_duration)
            logging.info(f"Mouse moved to calculated coordinates over {move_duration:.2f} seconds.")

            time.sleep(random.uniform(0.5, 1))  # Simulate human hesitation.
            pyautogui.click()
            logging.info("Physical click on captcha checkbox simulated successfully.")

            # Return to the main document.
            self.driver.switch_to.default_content()

        except TimeoutException:
            logging.error("Captcha iframe or checkbox did not load within the timeout period.")
        except Exception as e:
            logging.error(f"Error during captcha bypass with physical click simulation: {e}")

    def bypass_cookies(self) -> None:
        """
        Handles the cookie consent popup using Selenium by waiting for and clicking the specified button.
        """
        try:
            logging.info("Handling cookie consent popup using Selenium.")
            cookie_btn_xpath = '/html/body/div[13]/div[2]/div[2]/div[2]/div[2]/button[2]/p'
            self.wait.until(EC.element_to_be_clickable((By.XPATH, cookie_btn_xpath)))
            cookie_btn = self.driver.find_element(By.XPATH, cookie_btn_xpath)
            cookie_btn.click()
            logging.info("Cookie consent accepted successfully.")
            time.sleep(random.uniform(0.5, 1))
        except Exception as e:
            logging.warning(f"Cookie consent button not found or timed out: {e}")


try:
    # mov random mouse
    pyautogui.moveTo(random.randint(0, 1920), random.randint(
        0, 1080), duration=random.uniform(0.5, 4.5))

    # wait
    time.sleep(random.uniform(2,6))

    # mov to checkbox
    checkbox_position = (540,380)
    pyautogui.moveTo(
        checkbox_position[0], checkbox_position[1], duration=random.uniform(0.5, 4.5))
    time.sleep(random.uniform(0.5, 2))
    # click checkbox
    pyautogui.click()
except:

    print("No se encontró el checkbox")



   
   # //*[@id="page_body"]/div[14]/div[2]/div[2]/div[2]/div[2]/button[2]/p
    
try:
    # mov mouse to pop up
    checkbox_position = (1127,815)
    pyautogui.moveTo(checkbox_position[0],checkbox_position[1],
                    duration=random.uniform(0.5, 4.5))
    time.sleep(random.uniform(3,6))
    driver.find_element(By.XPATH, '/html/body/div[13]/div[2]/div[2]/div[2]/div[2]/button[2]/p').click()


except:

    print("No se encontró el checkbox")

    
try:
    # mov mouse to pop up
    time.sleep(random.uniform(0.5,2))

    driver.find_element(By.XPATH, '/html/body/div[13]/div[2]/div[3]/div[2]/div/div[3]/div[8]/label[2]/span[2]/input').click()
    time.sleep(random.uniform(0.1,1))
                                                                             
    pyautogui.scroll(-80)
    driver.find_element(By.XPATH, '/html/body/div[13]/div[2]/div[3]/div[2]/div/div[3]/div[8]/label[2]/span[2]/span').click()
    time.sleep(random.uniform(0.5,2))
    driver.find_element(By.XPATH, '').click()
    pyautogui.scroll(-100)
    time.sleep(random.uniform(0.1,0.5))
    driver.find_element(By.XPATH, '/html/body/div[13]/div[2]/div[3]/div[2]/div/div[3]/div[10]/label[2]/span[2]/input').click()
    
    time.sleep(random.uniform(0.1,0.5))
    driver.find_element(By.XPATH, '/html/body/div[13]/div[2]/div[3]/div[2]/div/div[3]/div[11]/label[2]/span[2]/input').click()


    time.sleep(random.uniform(0.1,0.5))
    driver.find_element(By.XPATH, '/html/body/div[13]/div[2]/div[3]/div[2]/div/div[3]/div[12]/label[2]/span[2]/input').click()




except:

    print("No se encontró el checkbox")
         




input("Presioná ENTER para cerrar...")
driver.quit()

                                      
