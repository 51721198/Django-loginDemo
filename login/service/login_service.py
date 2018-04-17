import random
import re

from login.models import UserInformation


class LoginService:
    def checkSQL(self, uid, inputPassword):
        # 判断是否有sql注入
        if uid[-1] == '\'':
            print('有人尝试注入！')
            return 'wrring'
        elif inputPassword[-1] == '\'':
            print('有人尝试注入！')
            return 'wrring'
        else:
            return 0

    def getPasswd(self, uname):
        # 查询数据库,如果这里报错那可能需要命令行:python manage.py migrate
        print(uname)
        try:
            password = UserInformation.objects.get(name=uname).password
            print(password)
            return password
        except:
            return "ERROR"

    def getUserInfo(self, name):
        # 取个人信息
        print('getting info')
        # conn = MySQLdb.connect(host="localhost",user="root",passwd="root",db="userinformation",charset="utf8")
        # cursor = conn.cursor()

        # try:
        #     #这里代码比较凌乱 因为刚学 django 和 mysql 不长时间 所以不知道有什么好的语法
        #     cursor.execute('select name from userinfo where Uid = "{}"'.format(Uid))
        #     username = cursor.fetchone()[0]
        #     cursor.execute('select sex from userinfo where Uid = "{}"'.format(Uid))
        #     sex = cursor.fetchone()[0]
        #     cursor.execute('select age from userinfo where Uid = "{}"'.format(Uid))
        #     age = cursor.fetchone()[0]
        #     cursor.execute('select Email from userinfo where Uid = "{}"'.format(Uid))
        #     Email = cursor.fetchone()[0]
        #     cursor.execute('select tel from userinfo where Uid = "{}"'.format(Uid))
        #     tel = cursor.fetchone()[0]
        #     conn.close()
        #     print(username,sex,age,Email,tel)

        result = UserInformation.objects.get(name=name)
        print(result.name, result.sex, result.age, result.email, result.tel)

        # 返回1 代表成功获取信息
        # 后面的list 是个人信息
        return 1, [result.name, result.sex, result.age, result.email, result.tel]

        # except:
        #     conn.close()
        #     return 0,[]

    # 第一个参数定义为self的函数一般是类的方法,区别于普通函数或者静态方法
    def checkInforMation(self, name, sex, age, tel, password, reinput_password, email):
        # 判断数据是否为空
        if name == '':
            return 0, 'name cannot be empty.'
        elif sex == '':
            return 0, 'sex cannot be empty'
        elif password == '':
            return 0, 'password cannot be empty'
        elif email == '':
            return 0, 'Email cannot be empty'
        elif sex != '1' and sex != '2':
            return 0, 'Please input 1(man) or 2(woman) in sexText'

        # 判断数据类型 防止数据类型错误
        if age != '':
            try:
                int(age)
            except:
                return 0, 'error ,the age must be Int !'
        # 判断数据类型
        if tel != '':
            try:
                int(tel)
            except:
                return 0, 'error ,the tel must be Int !'

                # 判断 E-Mail的格式有无错误
        emailre = re.compile(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$')
        check_email = re.search(emailre, email)
        if check_email is None:
            return 0, 'error ,邮箱格式错误！'

        if self.checkValueLength(name, sex, age, tel, password, reinput_password, email) == 0:
            return 0, '请检查字符长度！'

        if password != reinput_password:
            return 0, '两次输入密码不一致！'

        a = self.checkEmail(email)  # 获取返回值
        if a == 2:
            return 0, '该邮箱已注册'
        elif a == 0:
            return 0, '该邮箱无法通过审核系统,请更换。'

        # 上面的检测都没有问题 返回1
        return 1, 'OjbK'

    def checkValueLength(self, name, sex, age, tel, password, reinput_password, Email):
        # 判断有无超出长度导致 sql注入
        # 有则返回0
        if len(name) > 50 or len(sex) > 5 or len(tel) > 15 or len(age) > 20 or len(password) > 20 or \
                len(Email) > 30:
            return 0

    def generateUid(self):
        '''简单的生成一个 uid'''
        # 生成 uid的长度
        loop__number = random.randint(8, 10)

        uid = ''
        # 使用 random 模块 生成uid
        for i in range(0, loop__number):
            uid = uid + str(random.randint(0, 9))

        # 这里是判断 uid有无重复
        result = UserInformation.objects.filter(uid=uid)
        if not result:
            # 没有重复 返回 uid
            return uid
        else:
            # 重复了 重新调用当前函数 新生成一个
            self.generateUid()

    '''
       函数约定：
       返回值 为
       1 : 通过检测
       2 : 不通过检测 , 原因 - 邮箱已注册
       0 ：不通过检测, 原因 -会造成sql注入
       '''

    def checkEmail(self, email):
        # 判断是否有注入内容
        if email[-1] != '\'':
            res = UserInformation.objects.filter(email=email)
            # 检查邮箱有无重复
            if not res:
                return 1
            else:
                return 2
        else:
            return 0

    def createUser(self, name, age, sex, tel, uid, password, email):
        UserInformation.objects.create(name=name,
                                       age=age,
                                       sex=sex,
                                       tel=tel,
                                       uid=uid,
                                       password=password,
                                       email=email)
