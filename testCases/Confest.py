from selenium import webdriver
import pytest
@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path=r"C:\Users\saadc\Downloads\chromedriver_win32 (1)\chromedriver.exe")
    return driver

