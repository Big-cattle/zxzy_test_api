from selenium.webdriver.common.by import By
class IndexPageLocator:
	#首页右上角下标，修改密码上级
	xuanfu = (By.XPATH,'//*[@class="iconfont iconnavbar_icon_arrow"]')
	
	#修改密码入口
	change_pwd = (By.XPATH,'//*[@class="el-dropdown-menu__item"]/span')
	
	#旧密码输入框
	old_pwd = (By.XPATH,'//*[@for="originPassword"]/following-sibling::div/div/input')
	
	#新密码输入框
	new_pwd = (By.XPATH,'//*[@for="password"]/following-sibling::div/div/input')
	
	#确认密码输入框
	comfirm_pwd = (By.XPATH,'//*[@for="rePassword"]/following-sibling::div/div/input')
	
	#修改密码框确定按钮
	confirm_but = (By.XPATH,'//span[text()="确 定"]')
	
	#密码修改界面 提示语
	change_pwd_tip = (By.XPATH,'//*[@class="el-message__content"]')
	#密码修改区域 提示语
	change_pwd_cArea_tip = (By.XPATH, '//*[@class="el-form-item__error"]')
	