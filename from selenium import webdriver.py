from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep

driver = webdriver.Chrome("C:\GIT\Skillfactory\testGITinstruction\chromedriver")
driver.get("http://google.com")
driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys('facebook' + Keys.RETURN)
sleep(2)
driver.save_screenshot('sf.png')
driver.quit()