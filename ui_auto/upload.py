from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.common.by import By
from time import sleep
import win32gui
import win32con
driver = webdriver.Chrome()
driver.get("https://www.layui.com/demo/upload.html")
# WebDriverWait(driver,20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'/html/body/iframe')))
# driver.switch_to.frame(driver.find_element_by_xpath('//*[@class="layui-upload"]/*[text()="上传图片"]')).click()
# WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.NAME,"uploadimg")))
driver.find_element_by_xpath('//*[@class="layui-upload"]/*[text()="上传图片"]').click()

# driver.find_element_by_name("uploadimg").click()
sleep(2)
def upload(filepath):
	dialog = win32gui.FindWindow("#32770",'打开')#一级窗口
	#二级窗口
	ComboBoxEx32 = win32gui.FindWindowEx(dialog,0,'ComboBoxEx32',None)
	#三级窗口
	ComboBox = win32gui.FindWindowEx(ComboBoxEx32,0,'ComboBox',None)
	#文本输入框窗口 - 四级
	edit = win32gui.FindWindowEx(ComboBox,0,'Edit',None)
	#打开按钮 - 二级窗口
	button = win32gui.FindWindowEx(dialog,0,'Button','打开(&O)')
	
	#输入文件地址
	win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,filepath)#发送文件
	
	#点击 打开按钮 提交文件
	win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button)
upload('E:\\微信截图_20210204150526.png')

