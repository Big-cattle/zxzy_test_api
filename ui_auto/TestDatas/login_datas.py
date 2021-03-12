#正常场景 -- 测试数据
success_data = {"username":'flz_15333333333','password':'long,12012'}

#异常场景 -- 测试数据异常场景 -- （用户名为空，密码为空，验证码为空）
username_datas = [{"username":'','password':'long,12012','check':'请输入用户名','code':'uw31'},
                  {"username":'zb_15876527944','password':'','check':'请输入密码','code':'uw31'},
				{"username":'zb_15876527944','password':'long,12012','check':'验证码不能为空','code':''}]

#异常场景 --用户名错误，密码错误，验证码错误，用户名已失效，未分配角色用户名，密码错误次数超过三次
error_datas = [{"username":'zb_1587652794','password':'long,12012','check':'登录账号或者密码有误','code':'uw31'},
                            {"username":'zb_15820201301','password':'long,1201','check':'登录账号或者密码有误','code':'uw31'},
                            {"username":'zb_15876527944','password':'long,12012','check':'验证码错误或者已失效','code':'uw32'},
                            {"username": 'zb_15820201397', 'password': 'a@15820201397', 'check': '账号未激活或已失效，请联系超管！', 'code': 'uw31'},
                            {"username": 'zb_15820201398', 'password': 'a@1582020', 'check': '未分配角色，请联系管理员', 'code': 'uw31'},
               {"username":'zb_15820201302','password':'long,1201','check':'登录账号或者密码有误','code':'uw31'},
               {"username":'zb_15820201302','password':'long,1201','check':'登录账号或者密码有误','code':'uw31'},
               {"username":'zb_15820201302','password':'long,1201','check':'登录账号或者密码有误','code':'uw31'},
               {"username":'zb_15820201302','password':'long,1201','check':'登录错误次数已达3次，请30分钟后重试','code':'uw31'}]

#登陆页面，重置按钮功能 - 清空用户名输入框/清空密码输入框/清空验证码输入框
reset_datas = [ {"username":'zb_15876527944','password':'','code':''},
                {"username": '', 'password': '1234546', 'code': ''},
                {"username": '', 'password': '', 'code': 'uw31'},
                {"username": 'zb_15876527944', 'password': '1321654',  'code': 'uw31'}]


if __name__ == '__main__':
    print(*error_datas)