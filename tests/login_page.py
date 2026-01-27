from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self,driver):
        self.driver=driver

    USERNAME_INPUT=(By.ID,"username")
    PASSWORD_INPUT=(By.ID,"password")
    LOGIN_BTN=(By.CSS_SELECTOR,"button.radius")
    MESSAGE=(By.ID,"flash")


    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def login(self,username,password):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password) 
        self.driver.find_element(*self.LOGIN_BTN).click()

    def get_message(self):
        return self.driver.find_element(*self.MESSAGE).text