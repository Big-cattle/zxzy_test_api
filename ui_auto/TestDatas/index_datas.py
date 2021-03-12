#正常场景 - 修改密码成功
change_success_data = {'old_pwd':'xhy15820.','new_pwd':'xhy15820.','confirm_pwd':'xhy15820.'}

#异常场景 - 修改密码失败(旧密码为空，新密码为空，确认密码为空，两次密码不一致，密码只有数字，密码只有特殊符号，密码只有英文字母，密码长度小于8位)
change_error_datas = [{'old_pwd':'','new_pwd':'xhy15820.','confirm_pwd':'xhy15820.','check':'请输入旧密码'},
                      {'old_pwd':'xhy15820.','new_pwd':'','confirm_pwd':'xhy15820.','check':'请输入密码'},
                      {'old_pwd':'xhy15820.','new_pwd':'xhy15820.','confirm_pwd':'','check':'请再次输入密码'},
                      {'old_pwd': 'xhy15820.', 'new_pwd': 'xhy15820.', 'confirm_pwd': 'xhy15820','check':'两次输入密码不一致!'},
                      {'old_pwd': 'xhy15820.', 'new_pwd': '15820201', 'confirm_pwd': '15820201','check':'密码必须由数字、字母、特殊字符组合,请输入8-25位'},
                      {'old_pwd': 'xhy15820.', 'new_pwd': '......@.', 'confirm_pwd': '......@.','check':'密码必须由数字、字母、特殊字符组合,请输入8-25位'},
                      {'old_pwd': 'xhy15820.', 'new_pwd': 'aaaaaaaa', 'confirm_pwd': 'aaaaaaaa','check':'密码必须由数字、字母、特殊字符组合,请输入8-25位'},
                      {'old_pwd': 'xhy15820.', 'new_pwd': 'xhy158.', 'confirm_pwd': 'xhy158.','check':'密码必须由数字、字母、特殊字符组合,请输入8-25位'}]
#异常场景 - 修改密码失败(原密码错误，密码长度大于25)
change_error_datas1 = [  {'old_pwd':'xhy15820','new_pwd':'','confirm_pwd':'xhy15820.'},
                         {'old_pwd': 'xhy15820.', 'new_pwd': 'xhy1582020139715820201397.', 'confirm_pwd': 'xhy1582020139715820201397.'}]