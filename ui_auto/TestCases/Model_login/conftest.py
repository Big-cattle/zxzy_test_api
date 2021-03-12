import pytest
from selenium import webdriver
from TestDatas .Common_Datas import *
from PageObjects.login_page import *
#声明他是一个fixture
driver = None
@pytest.fixture(scope="class")#scope设置作用域（session，class，function）
def access_web():
	global driver
	#前置操作
	print("================所有测试类之前的，===整个测试类只执行一次================")
	driver = webdriver.Chrome()
	driver.get(web_login_url)
	lg = LoginPage(driver)
	yield(driver,lg)#分割线；#候面接返回值
	#后置操作
	print("================所有测试类之后的，===整个测试类只执行一次================")
	driver.quit()
	
@pytest.fixture()#默认function
def refresh_page():#刷新页面
	global driver
	#前置操作
	yield
	#后置操作
	driver.refresh()
	
@pytest.fixture(scope="session")
def session_demo():
	print("**********我是整个测试绘画期间的开始**********")
	yield
	print("**********我是整个测试绘画期间的结束**********")


@pytest.fixture(scope="class")
def class_demo():
	print("**********我是class的开始**********")
	yield
	print("**********我是class的结束**********")
	
@pytest.fixture()
def func_demo():
	print("**********我是function的开始**********")
	yield
	print("**********我是function的结束**********")
	