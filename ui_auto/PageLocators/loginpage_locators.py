from selenium.webdriver.common.by import By
class LoginPageLocator:
		#元素定位
		#用户名输入框
		name_text = (By.XPATH,'//*[@placeholder="请输入用户名"]')
		#密码输入框
		pwd_text = (By.XPATH,'//*[@placeholder="请输入密码"]')
		#验证码输入框
		code_text = (By.XPATH,'//*[@placeholder="请输入验证码"]')
		#登录按钮
		login_but = (By.XPATH,'//*[text()="登录"]')
		
		#用户名，密码，验证码为空提示语
		null_prompt = (By.XPATH,'//*[@class="el-form-item__error"]')
		
		#登录页面弹出框错误提示语
		error_prompt = (By.XPATH,'//*[@class="el-message__content"]')

		#登陆页面重置按钮
		reset_but = (By.XPATH,'//*[text()="重置"]')

		# 获取用户登录区域的异常提示信息
		loginArea = (By.XPATH,'//*[@class="el-form-item__error"]')

		# 获取异常登录弹出框错误提示语信息
		loginArea_error = (By.XPATH,'//*[@class="el-message__content"]')