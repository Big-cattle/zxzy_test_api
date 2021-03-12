from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Chrome()#创建会话
driver.implicitly_wait(5)#隐式等待
driver.get("https://www.baidu.com")#打开网址
driver.find_element_by_id("kw").send_keys("柠檬班")#定位百度输入框
driver.find_element_by_id("su").click()#定位百度确认按钮，并点击
# handle = driver.window_handles  获取全部窗口句柄，返回列表
# wl = '//div[@tpl="tieba_general"]/h3/a'
WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'//div[@tpl="tieba_general"]/h3/a'))).click()#显性等待，定位元素
#WebDriverWait(driver,20).until(EC.new_window_is_opened(handle))#显性等待，判断新窗口是否出现
handle = driver.window_handles #获取全部窗口句柄，返回列表，最新打开的窗口，排在列表中的最后
driver.switch_to.window(handle[-1])#获取最新打开的窗口
driver.find_element_by_id("j_head_focus_btn").click()#定位新窗口中的元素

# driver.implicitly_wait(5)
# driver.find_element_by_xpath('//div[@tpl="tieba_general"]/h3/a').click()