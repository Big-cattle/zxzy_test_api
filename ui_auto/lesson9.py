from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
#第一步，定位需要操作的元素
ele = driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
#第二步，实例化ActionChains类
ac = ActionChains(driver)
#第三步，把操作添加到actions列表中
ac.move_to_element(ele)
#第四步，调用perform()来执行鼠标操作
ac.perform()
