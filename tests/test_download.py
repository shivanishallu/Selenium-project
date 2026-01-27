from pages.upload_page import UploadPage

def test_sample_download(driver):
    driver.get("https://the-internet.herokuapp.com/download")
    assert "/download" in driver.current_url
