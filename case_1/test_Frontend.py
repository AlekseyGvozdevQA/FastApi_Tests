import subprocess
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Tests_Fronts:
    """Проверка фронтенда, проверка ID User'ов чата"""

    def test_config(self):
        # Отрытие файла  "main.py" сразу в тесте
        proc = subprocess.Popen(["python", "main.py"], stdout=subprocess.PIPE)

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.base_url = "http://127.0.0.1:8000"
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element(By.XPATH, "//input[@id='messageText']").click()
        driver.find_element(By.XPATH, "//input[@id='messageText']").clear()
        wait = WebDriverWait(driver, 10)
        send_text = driver.find_element(By.XPATH, "//input[@id='messageText']")
        wait.until(EC.element_to_be_clickable(send_text))
        sent_button = driver.find_element(By.XPATH, "//button[contains(text(),'Send')]")
        wait.until(EC.element_to_be_clickable(sent_button))
        sent_button.click()
        driver.find_element(By.XPATH, "//span[@id='ws-id']")
        text = driver.find_element(By.XPATH, "//body/h2[1]")
        wait.until(EC.element_to_be_clickable(text))
        text_1 = text.text
        nums = re.findall(r'\d+', text_1)
        text2 = driver.find_element(By.XPATH, "/html[1]/body[1]/ul[1]/li[3]")
        wait.until(EC.element_to_be_clickable(text2))
        text_2 = text2.text
        nums2 = re.findall(r'\d+', text_2)
        assert nums[0] == nums2[0]
        proc.kill()
        self.driver.close()