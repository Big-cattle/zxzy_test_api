import pytest
from selenium import webdriver
from TestDatas .Common_Datas import *
from PageObjects.index_page  import *
from PageObjects.login_page import *
from time import sleep
driver = None
@pytest.fixture(scope="class")
def access_index_page():
	global driver
	driver = webdriver.Chrome()
	driver.get(web_login_url)
	ip = IndexPage(driver)
	LoginPage(driver).login('zb_15820201301', 'xhy15820.')
	sleep(2)
	yield (driver,ip)
	driver.quit()

@pytest.fixture()
def refresh_page():
	global driver
	yield
	driver.refresh()
	
	