from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://ke.qq.com/')
driver.maximize_window()
driver.find_element_by_id("js_login").click()
driver.find_element_by_xpath('//*[@class="js-btns-enter btns-enter btns-enter-qq"]').click()
WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it("login_frame_qq"))
# driver.switch_to.frame("login_frame_qq")
driver.find_element_by_xpath('//a[text()="帐号密码登录"]').click()
#driver.find_element_by_xpath('//a[@id="uin_del"]').click()
driver.find_element_by_xpath("//*[@id='u']").send_keys("460290847")
driver.find_element_by_xpath('//*[@id="p"]').send_keys("HAOy@779351126")
time.sleep(3)
driver.find_element_by_xpath('//*[@class="submit"]//a').click()
