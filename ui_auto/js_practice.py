#遇到不能用send_keys()进行输入的输入框，如日期选择框，地址选择框，可以用js改变其readonly属性未false,就可以输入了
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.12306.cn/index/")
#将 dom脚本，每一句以分号隔开，存入字符串，赋值给js
js = 'ele = document.getElementById("train_date");ele.readOnly = false;'
#用execute_script函数运行 js
driver.execute_script(js)
driver.find_element_by_id("train_date").clear()
driver.find_element_by_id('train_date').send_keys("2021-2-7")
