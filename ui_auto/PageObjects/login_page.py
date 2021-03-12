from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PageLocators.loginpage_locators import LoginPageLocator as loc
from selenium import webdriver
from TestDatas.Common_Datas import *
from Common.basepage import BasePage

class LoginPage(BasePage):#继承BasePage类
	doc = "登录页面_登录功能"
	#登录
	def login(self,username,password,code='uw31'):
		#输入用户名,调用BasePage类的元素输入操作函数
		self.input_text(loc.name_text,username,self.doc)
		# 输入密码，调用BasePage类的元素输入操作函数
		self.input_text(loc.pwd_text,password,self.doc)
		#输入验证码，调用BasePage类的元素输入操作函数
		self.input_text(loc.code_text,code,self.doc)
		# 点击登录,调用BasePage类的元素点击函数
		self.click_element(loc.login_but,self.doc)
	
	#判断元素是否存在
	def is_element_exist(self,ele):
		try:
			WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,ele)))
			return True
		except:
			return False

	#获取用户登录区域的异常提示信息
	def get_errorMsg_from_loginArea(self):
		doc = "登录页面_登录功能"
		self.wait_eleVisible(loc.null_prompt,doc=doc)
		return  self.get_text(loc.null_prompt,doc)
	
	#获取异常登录弹出框错误提示语信息
	def get_errMsg_from_login_alertArea(self):
		self.wait_eleVisible(loc.error_prompt, doc=self.doc)
		return self.get_text(loc.error_prompt,self.doc)
		
	#清空输入框 - 重置按钮
	def reset_button(self,username,password,code='uw31'):
		# 输入用户名
		self.input_text(loc.name_text,self.doc)
		# 输入密码
		self.input_text(loc.pwd_text,self.doc)
		# 输入验证码
		self.input_text(loc.code_text,self.doc)
		#点击重置按钮
		self.click_element(loc.reset_but,self.doc)
		if self.get_element_attribute(loc.name_text,'value',self.doc) ==""and self.get_element_attribute(loc.pwd_text,'value',self.doc) =="" and self.get_element_attribute(loc.code_text,'value',self.doc) == "":
			return True
		else:
			return False
		
if __name__ == '__main__':
	driver = webdriver.Chrome()
	lg = LoginPage(driver)
	driver.get(web_login_url)
	# doc = "登陆页面"
	# lg.click_element(loc.name_text)
	# lg.click_element(loc.pwd_te
	name = "登陆页面_登录功能"
	lg.save_screenshot(name)
	
	print("123")
	


