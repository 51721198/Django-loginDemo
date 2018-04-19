from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from login.service.login_service import LoginService

'''
@ author：jaydenchan

'''

loginservice = LoginService()


class Login:
    def login(self, request):
        # 判断是否为 post请求
        if request.POST:
            # 取输入信息
            name = request.POST['uname']
            password = request.POST['password']

            # 检测是否有sql注入
            check_result = loginservice.checkSQL(name, password)
            if check_result == 'wrring':
                return HttpResponse('想注入我没那么简单！')

                # 验证用户名
            real_passwd = loginservice.getPasswd(name)
            if real_passwd == "ERROR":
                return HttpResponse('没有这个用户名!')

            print(real_passwd, password)

            # 验证密码
            if password == real_passwd:
                run_result, Info = loginservice.getUserInfo(name)
                if run_result == 1:
                    # 渲染网页
                    connect = {
                        'login_result': "登录成功!",
                        'user_sex': Info[1],
                        'user_Email': Info[3],
                        'user_age': Info[2],
                        'user_name': Info[0],
                        'user_tel': Info[4]
                    }
                    return render(request, "login.html", connect)
                else:

                    connect = {
                        'login_result': "登录成功 获取信息失败！"
                    }
                    return render(request, 'login.html', connect)

                    # return HttpResponse("登录成功 获取信息失败！")
            else:
                return HttpResponse("密码错误！")

    def index(self, response):
        # 显示主页
        connect = {}
        return render(response, 'index.html', connect)


class SignUp:
    def sign_up_index(self, response):
        # 渲染主页
        connect = {}
        return render(response, 'sign-up.html', connect)

    def signUp(self, request):
        if request.POST:
            # 获取输入信息
            name = request.POST['name']
            sex = request.POST['sex']
            age = request.POST['age']
            tel = request.POST['tel']
            password = request.POST['password']
            reinput_password = request.POST['passwd_reInput']
            email = request.POST['Email']

            # State_code 为状态码  Check_info 为返回的提示信息
            State_code, Check_info = loginservice.checkInforMation(name, sex, age, tel, password, reinput_password, email)

            if State_code == 0:
                # 如果出现了错误 就提示用户
                return HttpResponse("错误！" + Check_info)
            else:
                print(name, password, email, age, sex, tel)
                uid = loginservice.generateUid()

                # 数据库插入
                loginservice.createUser(name, age, sex, tel, uid, password, email)
                return HttpResponse('注册成功！你的账号(UID)是 ：' + uid)
