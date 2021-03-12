
from selenium import webdriver
from PageObjects.index_page import IndexPage
from TestDatas.Common_Datas import *
from time import sleep
from ddt import ddt,data
from PageLocators.indexpage_locators import IndexPageLocator as loc
from PageObjects.login_page import LoginPage as lg
import unittest
from TestDatas.index_datas import *
import pytest
from Common.get_log import GetLog

# @ddt
@pytest.mark.usefixtures("access_index_page")
@pytest.mark.usefixtures("refresh_page")

class TestIndex:
	# @classmethod
	# def setUpClass(cls) :
	# 	cls.driver = webdriver.Chrome()
	# 	cls.driver.get(web_login_url)
	# 	cls.ip = IndexPage(cls.driver)
	# 	lg(cls.driver).login('zb_15820201301','xhy15820.')
	# 	sleep(2)
	# @classmethod
	# def tearDownClass(cls) :
	# 	#cls.driver.quit()
	# 	pass
	# def tearDown(self) :
	# 	self.driver.refresh()
	# 	# self.driver.quit()
	@pytest.mark.smoke
	def test_change_pwd_success(self,access_index_page):
		GetLog().info_log("**********登录用例：正常场景：修改密码成功**********")
		access_index_page[1].change_password(change_success_data['old_pwd'],change_success_data['new_pwd'],change_success_data['confirm_pwd'])
		assert access_index_page[1].change_password_tip(),'修改密码成功'
	@pytest.mark.parametrize("data",change_error_datas)
	def test_change_pwd_error(self,data,access_index_page):
		GetLog().info_log("**********登录用例：异常场景：输入错误数据修改密码失败**********")
		access_index_page[1].change_password(data['old_pwd'], data['new_pwd'],data['confirm_pwd'])
		assert access_index_page[1].change_password_cArea_tip(),data['check']
	

	
		
		
	
	