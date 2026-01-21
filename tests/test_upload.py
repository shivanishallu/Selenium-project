from utils.driver_setup import get_driver
from pages.upload_page import UploadPage

def test_file_upload():
    driver=get_driver()
    page=UploadPage(driver)

    page.open()
    page.upload_file(r"C:\Users\Baba\Downloads\some-file.txt")

    assert "some-file.txt" in page.get_uploaded_filename()

    driver.quit()