import sys
sys.path.append(r"E:\PycharmProjects\ZXZY_API_AUTO")
import configparser
from ZXZY_API_AUTO.common.public.abs_path import *
class ReadConfig:
	@staticmethod
	def read_cf(section,option):
		rc = configparser.ConfigParser()
		rc.read(conf_path,encoding='utf-8')
		return  eval(rc.get(section,option))

if __name__ == '__main__':
	print(type(ReadConfig().read_cf('CON','mode')))
	res = ReadConfig.read_cf('CON','mode')
	print(res)
	
