#1.封装基本函数 - 执行日志/ 异常处理/ 失败截图
import logging
import datetime
import os
from TestDatas.Common_Datas import *
from Common.get_log import GetLog as gl
import time
#2.所有页面公共的部分

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
class BasePage:
	def __init__(self,driver):
		self.driver = driver
		
	#等待元素可见
	def wait_eleVisible(self,locator,times=30.0,poll_frequency=0.5,doc=""):
		gl().info_log("等待元素 {} 可见".format(locator))
		try:
			#开始等待的时间
			start = datetime.datetime.now()
			WebDriverWait(self.driver,times,poll_frequency).until(EC.visibility_of_element_located(locator))
			# 等待时间结束的点
			end = datetime.datetime.now()
			# 耗时
			use_time = (end-start).seconds
			gl().info_log("等待结束，等待时长为：{}".format(use_time))
		except:
			logging.exception("等待元素可见失败！！！")
			#截图
			self.save_screenshot(doc)
			raise
			
	
	#等待元素存在
	def wait_elePresence(self,locator,times=30.0,poll_frequency=0.5,doc=""):
		gl().info_log("等待元素存在：{}".format(locator))
		try:
			#开始等待时间
			start = datetime.datetime.now()
			WebDriverWait(self.driver,times,poll_frequency).until(EC.presence_of_element_located(locator))
			#等待结束时间
			end = datetime.datetime.now()
			#耗时
			use_time = (end-start).seconds
			gl().info_log("等待结束，等待时长为{}".format(use_time))
		except:
			logging.exception("等待元素存在失败！！！")
			#截图
			self.driver.save_screenshot(doc)
			raise
	
	#查找元素
	def get_element(self,locator,doc=""):
		gl().info_log("查找元素：{}".format(locator))
		try:
			return self.driver.find_element(*locator)
		except:
			logging.exception("定位元素失败！！！")
			#截图
			self.save_screenshot(doc)
			raise
	
	#点击操作
	def click_element(self,locator,doc=""):
		#找元素
		ele = self.get_element(locator,doc)
		#元素操作
		gl().info_log("{0} ,点击元素：{1}".format(doc,locator))
		try:
			ele.click()
		except:
			logging.exception("元素点击失败！！！")
			# 截图
			self.save_screenshot(doc)
			raise
		
		
	
	#输入操作
	def input_text(self,locator,text,doc=""):
		# 找元素
		ele = self.get_element(locator, doc)
		# 元素操作
		gl().info_log("{0} ,输入内容：{1}".format(doc, locator))
		try:
			ele.send_keys(text)
		except:
			logging.exception("内容输入失败！！！")
			# 截图
			self.save_screenshot(doc)
			raise
		
	
	#获取元素的文本内容
	def get_text(self,locator,doc=""):
		#找元素
		ele = self.get_element(locator,doc)
		#元素操作
		gl().info_log("{} 获取元素文本内容".format(doc))
		try:
			return ele.text
		except:
			logging.info("获取元素文本内容失败！！！")
			#截图
			self.save_screenshot(doc)
			raise
	
	
	#获取元素的属性
	def get_element_attribute(self,locator,key,doc=""):
		#找元素
		ele = self.get_element(locator,doc)
		#元素操作
		gl().info_log("{0}获取元素的{1}属性".format(doc,key))
		try:
			return ele.get_attribute(key)
		except:
			logging.info("获取元素的属性失败！！！")
			#截图
			self.driver.save_screenshot(doc)
		
		pass

	#alert处理
	def alert_action(self,action='accept'):
		pass
	
	#iframe切换
	def switch_iframe(self,iframe_reference):
		pass
	
	#上传操作
	def upload_file(self):
		pass
	
	#截图
	def save_screenshot(self,doc):
		#图片名称：模块名_页面名称_操作名称_年-月-日_时分秒.png
		# file_path = os.path.
		file_name = picture_path+ "/{0}_{1}.png".format(doc,time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime()))
		try:
			self.driver.save_screenshot(file_name)
			gl().info_log("截取网页成功，文件路径为：{0}".format(file_name,))
		except:
			logging.exception("截取网页失败！！！")
if __name__ == '__main__':
	from selenium import webdriver
	from selenium.webdriver.common.by import By
	from PageLocators.loginpage_locators import LoginPageLocator as loc
	driver = webdriver.Chrome()
	driver.implicitly_wait(10)
	bp = BasePage(driver)
	driver.get("http://zy-admin-web-zhenxuanziyan.apps.dev.ht.paas.cmic.cn/#/login")
	login = (By.XPATH,'//*[@class="login-box"]/h3')
	bp.click_element(loc.name_text)
	bp.click_element(loc.pwd_text)
	
	print(bp.get_text(loc.null_prompt))
	print(bp.get_text(login))