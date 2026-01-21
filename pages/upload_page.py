from selenium.webdriver.common.by import By

class UploadPage:
    def __init__(self, driver):
        self.driver = driver
    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/upload")

    def upload_file(self, path):
        self.driver.find_element(By.ID,"file-upload").send_keys(path)
        self.driver.find_element(By.ID,"file-submit").click()

    def get_uploaded_filename(self):
        return self.driver.find_element(By.ID,"uploaded-files").text