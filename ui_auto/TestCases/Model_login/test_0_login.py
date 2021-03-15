# import unittest
# from ddt import ddt,data
from selenium import webdriver
from PageObjects.login_page import *
from TestDatas .Common_Datas import *
from PageObjects.index_page import *
from TestDatas.login_datas import *
import pytest
from Common.get_log import *
# @ddt
# @pytest.mark.demo
# @pytest.mark.usefixtures("class_demo")
# @pytest.mark.usefixtures("func_demo")
# def test_demo():
# 	demo()
# 	assert False
# def demo():
# 	print("那就不要留，时光一去不再有")


@pytest.mark.usefixtures("access_web")
@pytest.mark.usefixtures("refresh_page")
class TestLogin:
	
	# #异常场景 -- 用户名格式不正确（为空，已注销的用户名，错误的用户名）
	# @data(*username_datas)
	@pytest.mark.parametrize("data", username_datas)
	def test_login_2_user_wrongFormat(self, data, access_web):
		GetLog().info_log("**********登录用例：异常场景：输入框为空等异常情况**********")
		access_web[1].login(data['username'], data['password'], data['code'])
		assert data['check'], access_web[1].get_errorMsg_from_loginArea()
		
		# # 异常场景 --用户名错误，密码错误，验证码错误，用户名已失效，未分配角色用户名,密码错误次数超过三次
		# @data(*error_datas)
	@pytest.mark.parametrize("data", error_datas)
	def test_login_1_user_wrongFormat(self, data, access_web):
		GetLog().info_log("**********登录用例：异常场景：错误数据**********")
		access_web[1].login(data['username'], data['password'], data['code'])
		assert access_web[1].get_errMsg_from_login_alertArea(), data['check']
		
		# #登录页面重置按钮功能测试
		# @data(*reset_datas)
	@pytest.mark.parametrize("data", reset_datas)
	def test_login_0_reset_button(self, data, access_web):
		GetLog().info_log("**********登录用例：重置按钮功能**********")
		assert access_web[1].reset_button(data['username'], data['password'], data['code'])
	
	@pytest.mark.smoke
	# 输入正确的账号和密码，成功登录
	def test_login_4_success(self, access_web):
		GetLog().info_log("**********登录用例：正常场景：使用正确的用户名和密码登录**********")
		# 步骤： 输入用户名及密码，点击登录  #fixture的函数名称，用来接收它的返回值
		access_web[1].login(success_data['username'], success_data['password'])
		# 断言
		assert IndexPage(access_web[0]).is_element_exist()
#让全部用例在一个窗口中运行，然后在一个用例执行完后，刷新页面
	# @classmethod
	# def setUpClass(cls) :
	# 	# 前置 ，创建实例，打开网址
	# 	option = webdriver.ChromeOptions()
	# 	option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
	# 	cls.driver = webdriver.Chrome(chrome_options=option)
	# 	cls.driver.get(web_login_url)
	#
	# 	# 创建登录页面实例
	# 	cls.lg = LoginPage(cls.driver)
	# 	cls.driver.implicitly_wait(10)
	# @classmethod
	# def tearDownClass(cls) :
	# 	cls.driver.quit()
	#
	# #每个用例执行完后，刷新页面
	# def tearDown(self) :
	# 	#关闭驱动
	# 	self.driver.refresh()
	
		
	
	
	#
	
	
# if __name__ == '__main__':
# 	driver = webdriver.Chrome()
# 	driver.get(web_login_url)
# 	lg = LoginPage(driver)
# 	bp = IndexPage(driver)
# 	lg.login(success_data['username'],success_data['password'])
	
	# bp.change_password('1582020', '1582020', '1582020')