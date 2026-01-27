import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_file_upload(driver):
    logging.info("Opening upload page")
    page = UploadPage(driver)
    page.open()
    logging.info("Uploading file")
    page.upload_file("C:/test.txt")
    assert page.get_success_message() == "File Uploaded!"
    logging.info("Test passed")