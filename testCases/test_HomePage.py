import pytest
from selenium import webdriver
from pageObjects.HomePage import HomePage
from testCases.Confest import setup
from utilities.readProperties import ReadConfig

class Test_001_SearchBar:

    #baseUrl = format(str(ReadConfig.getApplicationURL()))
    baseUrl = "https://todomvc.com/examples/react/#/active"
    #format(str(baseUrl))

#Test Case to match the title of the page . Test Case result = failed because the title is wrong
    def test_homePageTitle(self,setup):

        self.driver = setup
        self.driver.get(self.baseUrl)
        act_Title = self.driver.title
        self.driver.close()
        if act_Title== "Abc":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False


    def test_homePageSearch(self,setup):

        self.driver = setup
        self.driver.get(self.baseUrl)
        self.hp = HomePage(self.driver)
        self.hp.setSearchBar(self.driver)

    def test_homePageSearchAll(self,setup):

        self.driver = setup
        self.driver.get(self.baseUrl)
        self.hp = HomePage(self.driver)
        self.hp.setActiveSearch(self.driver)



