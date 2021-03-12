import logging
from TestDatas.Common_Datas import *


class GetLog:
	def make_log(self, msg, level):
		my_log = logging.getLogger('zxzy_UI_autotest')  # 定义一个日志收集器
		my_log.setLevel(level)  # 设置日志级别
		formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息：%(message)s')  # 设置日志输出格式
		fh = logging.FileHandler(log_path, encoding='utf-8')  # 定义一个输出渠道，将日志写入文件
		fh.setLevel(level)  # 设置日志级别
		fh.setFormatter(formatter)
		my_log.addHandler(fh)  # 两者对接
		if level == "DEBUG":
			my_log.debug(msg)
		elif level == "INFO":
			my_log.info(msg)
		elif level == "WARNING":
			my_log.warning(msg)
		elif level == "ERROR":
			my_log.error(msg)
		elif level == "CRITICAL":
			my_log.critical(msg)
		my_log.removeHandler(fh)
	
	def debug_log(self, msg):
		self.make_log(msg, "DEBUG")
	
	def info_log(self, msg):
		self.make_log(msg, "INFO")
	
	def warn_log(self, msg):
		self.make_log(msg, "WARNING")
	
	def error_log(self, msg):
		self.make_log(msg, "ERROR")
	
	def critical_log(self, msg):
		self.make_log(msg, "CRITICAL")


if __name__ == '__main__':
	# GetLog().debug_log("他开着邻居的toyouta")
	# GetLog().info_log("追着日落")
	# GetLog().error_log('从不耍赖')
	# GetLog().warn_log("很烦打断")
	# GetLog().critical_log("父母说的最危险的地方")
	print(log_path)