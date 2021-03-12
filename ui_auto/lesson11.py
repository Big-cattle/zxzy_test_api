from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.common.by import By
#第一步导入Keys类
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
#第二步，定位操作元素，并输入柠檬班，以逗号隔开，键盘操作ENTER
driver.find_element_by_id("kw").send_keys("柠檬班",Keys.ENTER)
# driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//div[@id="10"]/h3/a')))
ele = driver.find_element_by_xpath('//div[@id="10"]/h3/a')
driver.execute_script("arguments[0].scrollIntoView();",ele)