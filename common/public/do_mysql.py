import pymysql
from ZXZY_API_AUTO.common.conf.read_config import ReadConfig
class DoMysql:
	@staticmethod
	def do_mysql(sql):
		db_config = ReadConfig.read_cf('DATABASE','db_config')#读取配置文件中的数据库连接数据
		
		cnn = pymysql.connect(**db_config)#建立数据库连接
		
		cursor = cnn.cursor()##建立游标
		
		cursor.execute(sql)#执行sql语句
		
		res = cursor.fetchall()#存储sql语句执行结果
		
		cursor.close()#关闭游标
		
		cnn.close()#关闭数据库连接
		
		return res#返回sql执行结果

if __name__ == '__main__':
	sql = 'select * from zy_goods where id=-8912732694605987840'
	print(DoMysql.do_mysql(sql))
 
	
		