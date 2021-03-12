from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageLocators.indexpage_locators import IndexPageLocator as loc
from Common.basepage import BasePage
from selenium import webdriver

class IndexPage(BasePage):
	
	def is_element_exist(self):
		try:
			WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[text()="首页"]')))
			return True
		except:
			return False
	
	def  change_password(self,old_pwd,new_pwd,confirm_pwd):
		self.wait_eleVisible(loc.xuanfu)
		self.click_element(loc.xuanfu)
		self.wait_eleVisible(loc.change_pwd)
		self.click_element(loc.change_pwd)
		self.input_text(loc.old_pwd,old_pwd)
		self.input_text(loc.new_pwd,new_pwd)
		self.input_text(loc.comfirm_pwd,confirm_pwd)
		self.click_element(loc.confirm_but)
		
	#密码修改界面弹出框提示
	def change_password_tip(self):
		self.wait_eleVisible(loc.change_pwd_tip)
		return self.get_text(loc.change_pwd_tip)
	
	#密码修改区域提示
	def change_password_cArea_tip(self):
		self.wait_eleVisible(loc.change_pwd_cArea_tip)
		return self.get_text(loc.change_pwd_cArea_tip)
	
if __name__ == '__main__':
	import os
	base_path = os.path.split(os.getcwd())[0]
	picture_path = os.path.join(base_path, 'Outputs\screenshots')
	print(picture_path)