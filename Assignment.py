'''
Created on 18-Sep-2023

@author: suraj
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as waitE
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)



class Test(unittest.TestCase):
    
    page_to_be_tested = "https://www.bt.com/"


    def setUp(self):
        
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.page_to_be_tested)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


    def test(self):
        
        #Popup
        self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, "truste_popframe"))
        time.sleep(3)
        self.driver.find_element(By.XPATH,"/html/body/div[8]/div[1]/div/div[3]/a[1]").click()
        self.driver.switch_to.parent_frame()
        time.sleep(3)
        
        #Mouse Hover
        first = self.driver.find_element(By.XPATH, '//div[2]/div[2]/div/div[1]/div[1]/ul/li[4]/a/span')
        second = self.driver.find_element(By.XPATH, '//div[2]/div[2]/div/div[1]/div[1]/ul/li[4]/ul/li/ul/li[2]/a')
        hover= ActionChains(self.driver)
        hover.move_to_element(first).perform()
        WebDriverWait(self.driver,5).until(waitE.visibility_of(second), "message")
        hover.move_to_element(second).click(second).perform()
        time.sleep(3)
        
        #Scrolling1
        scroll1 = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[4]/a')
        hover.scroll_to_element(scroll1).perform()
        time.sleep(3)
        
        #Banners present
        banner_list= self.driver.find_elements(By.XPATH, '//*[@id="__next"]/div/div[4]/div/div')
        x = len(banner_list)
        print("Count of Banners present= ",x)
        if x<3:
            print("Less than 3 Banners present")
        else:
            print("Atleast 3 Banners are present")
        time.sleep(3)
        
        #Scrolling2
        scroll2 = self.driver.find_element(By.XPATH, '//div/div[5]/div[2]/div[1]/div/div/div/div[2]/div/div[3]/a')
        hover.scroll_to_element(scroll2).perform()
        scroll2.click()
        time.sleep(3)
        
        #Title of the new webpage
        print("Title of the webpage is: ",self.driver.title)
        
        #Discount offer check
        scroll3 = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[4]/div[2]/div/div[2]/div[10]')
        hover.scroll_to_element(scroll3).perform()
        time.sleep(3)
        Discount = scroll3.is_displayed()
        if Discount == True:
            print("Discount is present")
        else:
            print("No discount")
        time.sleep(3)
        
    def tearDown(self):
        
        self.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()