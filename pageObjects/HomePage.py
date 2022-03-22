from selenium import webdriver
from selenium.webdriver import Keys

# Includes the locators which are useful for us and
class HomePage:
    searchbar_xpath = "/html/body/section/div/header/input"
    searchbar_checkbox_xpath = "/html/body/section/div/section/ul/li/div/input"
    searchbar_hyperlink_All_xpath = "/html/body/section/div/footer/ul/li[1]/a"
    searchbar_hyperlink_Active_xpath = "/html/body/section/div/footer/ul/li[2]/a"
    searchbar_hyperlink_Active_xpath = "/html/body/section/div/footer/ul/li[3]/a"
    searchbar_button_Clear_xpath = "/html/body/section/div/footer/button"
    searchbar_Togglebutton_xpath = "/html/body/section/div/section/label"

    def __init__(self , driver):   # construtor of python
        self.driver = driver

 # Simple Search Test Case
    def setSearchBar(self, search_data):
        self.driver.find_element_by_xpath(self.searchbar_xpath).clear()
        self.driver.find_element_by_xpath(self.searchbar_xpath).send_keys("ahmad")
        self.driver.find_element_by_xpath(self.searchbar_xpath).send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath(self.searchbar_hyperlink_All_xpath).click()
        self.driver.find_element_by_xpath(self.searchbar_checkbox_xpath).click()
        self.driver.find_element_by_xpath(self.searchbar_button_Clear_xpath).click()


    def setActiveSearch(self , search_data):
        self.driver.find_element_by_xpath(self.searchbar_xpath).clear()
        self.driver.find_element_by_xpath(self.searchbar_xpath).send_keys("active user")
        self.driver.find_element_by_xpath(self.searchbar_xpath).send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath(self.searchbar_button_Clear_xpath).click()



