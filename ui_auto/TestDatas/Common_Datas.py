import os
#全局 -—— 系统访问地址 —— 登录链接
web_login_url = "http://zy-admin-web-zhenxuanziyan.apps.dev.ht.paas.cmic.cn/#/login"

#文件首路径
base_path = os.path.split(os.path.split(__file__)[0])[0]

#截图存放路径
picture_path = os.path.join(base_path,r'Outputs\screenshots\\')

#日志存放路径
log_path = os.path.join(base_path,r'Outputs\log\test_run_log.txt')