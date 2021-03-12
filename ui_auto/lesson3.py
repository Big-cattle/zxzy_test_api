from selenium import webdriver
from time import sleep
#创建会话，启动Chromedriver驱动程序服务器
driver = webdriver.Chrome()
'''发送请求'''

#打开百度网页
driver.get("https://www.baidu.com")

#窗口最大化
driver.maximize_window()

#打开淘宝网页
driver.get("http://www.taobao.com")

#回退到上一页面
driver.back()

#前进一页（跳到淘宝页）
driver.forward()

#刷新页面
driver.refresh()

#打印标题
print(driver.title)

#打印网址
print(driver.current_url)

#打印当前窗口句柄，即网页ID
print(driver.current_window_handle)

#等待三秒
sleep(3)

#结束会话
driver.quit()