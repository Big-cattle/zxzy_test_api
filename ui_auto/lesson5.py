from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By
'''显性等待'''  #重要

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
driver.find_element_by_xpath("//div[@id='u1']//a").click()
wl='TANGRAM__PSP_11__footerULoginBtn'
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,wl)))
sleep(2)
driver.quit()