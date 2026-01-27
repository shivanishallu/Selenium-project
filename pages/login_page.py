from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    MESSAGE=("id","flash")
    
    def __init__(self,driver):
        self.driver=driver

    USERNAME_INPUT=(By.ID,"username")
    PASSWORD_INPUT=(By.ID,"password")
    LOGIN_BTN=(By.CSS_SELECTOR,"button.radius")
  


    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def login(self,username,password):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password) 
        self.driver.find_element(*self.LOGIN_BTN).click()

    def get_message(self):
        wait = WebDriverWait(self.driver, 10)
        msg = wait.until(EC.visibility_of_element_located(self.MESSAGE))
        return msg.text