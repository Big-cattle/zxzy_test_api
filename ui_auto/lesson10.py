from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
ele = driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
ac = ActionChains(driver)
ac.move_to_element(ele).perform()
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[text()="高级搜索"]'))).click()



