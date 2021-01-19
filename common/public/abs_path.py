'''储存项目路径的绝对路径，方便调用'''
import  os
base_path = os.path.split(os.path.split(os.path.split(__file__)[0])[0])[0] #项目首路径

log_path = os.path.join(base_path,'result/log/zxzy_test_log.txt') #日志文件路径

testdata_path = os.path.join(base_path,'test_data\\first_try.xlsx') #Excel测试数据路径

test_report_path = os.path.join(base_path,'result/test_report/test_report.html')#测试报告路径

conf_path = os.path.join(base_path,'common/conf/config.ini')#配置文件路径