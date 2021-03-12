from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://guanjia.qq.com/sem/970/index.html?ADTAG=media.buy.baidu.SEM")
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="mgr_nav_login"]').click()
#driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@name="login_ifr"]'))
#driver.switch_to.frame("login_ifr")

WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it("login_ifr"))
goods = driver.find_element_by_xpath('//span[text()=" 导入商品"]')

driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@name="ptlogin_iframe"]'))
#driver.switch_to.frame(driver.find_element_by_name('ptlogin_iframe'))
driver.find_element_by_xpath('//*[text()="帐号密码登录" and @class="link"]').click()
sleep(3)
driver.quit()