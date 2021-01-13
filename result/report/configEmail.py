# coding=UTF-8


import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from datetime import datetime
import threading
import readConfig as readConfig
import zipfile
import glob

localReadConfig = readConfig.ReadConfig()                               #初始化读取配置信息的类


class Email:
    def __init__(self):                                                #初始化email配置信息
        global host, user, password, port, sender, title
        host = localReadConfig.get_email("mail_host")
        user = localReadConfig.get_email("mail_user")
        password = localReadConfig.get_email("mail_pass")
        port = localReadConfig.get_email("mail_port")
        sender = localReadConfig.get_email("sender")
        title = localReadConfig.get_email("subject")
        # content = localReadConfig.get_email("content")

        # get receiver list
        self.value = localReadConfig.get_email("receiver")            #获取接收邮箱
        self.receiver = []                                             #可能有多个邮箱，用列表存储
        for n in str(self.value).split("/"):
            self.receiver.append(n)

        # defined email subject
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")         #定义电子邮件主题
        self.subject = "接口测试报告" + " " + date                    #邮件名

        self.msg = MIMEMultipart('related')                          #生成包括多个部分的邮件   邮件中有多个附件

    def config_header(self):
        """定义的电子邮件头包括主题，发件人和收件人
        defined email header include subject, sender and receiver
        :return:
        """
        self.msg['subject'] = self.subject                           #主题
        self.msg['from'] = sender                                    #发件人
        self.msg['to'] = ";".join(self.receiver)                     #收件人

    def config_content(self):
        """写电子邮件的内容
        write the content of email
        :return:
        """
        f = open(os.path.join(readConfig.proDir, 'testFile', 'emailStyle.txt'),encoding="utf-8")
        content = f.read()
        f.close()
        content_plain = MIMEText(content, 'html', 'UTF-8')
        self.msg.attach(content_plain)
        self.config_image()

    def config_image(self):
        """内容使用的配置图片
        config image that be used by content
        :return:
        """
        # defined image path  定义图像路径
        image1_path = os.path.join(readConfig.proDir, 'testFile', 'img', '测试账户.png')
        #打开图像路径
        fp1 = open(image1_path, 'rb')
        msgImage1 = MIMEImage(fp1.read())
        # self.msg.attach(msgImage1)
        fp1.close()

        # defined image id     定义图片名
        msgImage1.add_header('Content-ID', '<image1>')
        msgImage1["Content-Disposition"] = 'attachment; filename="testimage.png"'      #把图片文件格式从bin变成可识别的格式
        self.msg.attach(msgImage1)

        #第二张图片或其他附件，需要时再添加
        # image2_path = os.path.join(readConfig.proDir, 'testFile', 'img', 'logo.jpg')
        # fp2 = open(image2_path, 'rb')
        # msgImage2 = MIMEImage(fp2.read())
        # # self.msg.attach(msgImage2)
        # fp2.close()
        #
        # # defined image id     定义图片名
        # msgImage2.add_header('Content-ID', '<image2>')
        # self.msg.attach(msgImage2)

    # 定义一个函数，递归读取absDir文件夹中所有文件，并塞进zipFile文件中。参数absDir表示文件夹的绝对路径。
    def writeAllFileToZip(self,absDir, zipFile):
        for f in os.listdir(absDir):
            absFile = os.path.join(absDir, f)  # 子文件的绝对路径，路径是字符串，一个字符一个位置
            if os.path.isdir(absFile):  # 判断是文件夹，继续深度读取。
                relFile = absFile[len(os.path.dirname(os.path.realpath(__file__))) + 1:]  # 改成相对路径，路径是字符数组，str_list[20:]一个字符一个位置，len(os.getcwd())代表当前路径，获取后面段的字符串，这里根据文件路径不同，后面加的数字也不同
                # 上面相当于把D:\亿能达\测试\测试框架\demo_pytest_web\result\report\report截取字符数组的len(os.getcwd()位也就是到report，再加11位后面的字符相当于str_list[20:]
                zipFile.write(relFile)  # 在zip文件中创建文件夹
                self.writeAllFileToZip(absFile, zipFile)  # 递归操作
            else:  # 判断是普通文件，直接写到zip文件中。
                relFile = absFile[len(os.path.dirname(os.path.realpath(__file__))) + 1:]  # 改成相对路径
                zipFile.write(relFile)
        return

    def config_file(self):
        """配置邮件文件
        config email file
        :return:
        """

        # if the file content is not null, then config the email file          如果文件内容不为空，则配置电子邮件文件
        if self.check_file():

            #压缩测试结果文件夹
            reportpath = os.path.join(readConfig.proDir, "result", "report", "report")          #要压缩的文件夹绝对路径。
            zipFilePath = os.path.join(readConfig.proDir, "result", "测试报告.zip") #先定义zip文件绝对路径
            # files = glob.glob(reportpath + '\*')    #glob.glob是匹配所有的符合条件的文件名，并将其以list的形式返回
            zipFile = zipfile.ZipFile(zipFilePath, 'w', zipfile.ZIP_DEFLATED) #创建空的zip文件(ZipFile类型)。参数w表示写模式。zipfile.ZIP_DEFLATE表示需要压缩，文件会变小。ZIP_STORED是单纯的复制，文件大小没变。

            self.writeAllFileToZip(reportpath, zipFile)#开始压缩。如果当前工作目录跟脚本所在目录一样，直接运行这个函数
            # for file in files:老的压缩方法
            #     # 修改压缩文件的目录结构
            #     f.write(file, '/report/'+os.path.basename(file))    #这个只能压缩一层，深层的会丢失
            # f.close()

            reportfile = open(zipFilePath, 'rb').read()                             #发送邮箱附件的test.zip文件
            filehtml = MIMEText(reportfile, 'base64', 'utf-8')
            filehtml['Content-Type'] = 'application/octet-stream'
            filehtml['Content-Disposition'] = 'attachment; filename="test.zip"'
            self.msg.attach(filehtml)

    def check_file(self):
        """检查测试报告
        check test report
        :return:
        """
        reportpath = os.path.join(readConfig.proDir, "result", "report", "report", "index.html")
        if os.path.isfile(reportpath) and not os.stat(reportpath) == 0:
            return True
        else:
            return False

    def send_email(self):
        """发送邮件
        send email
        :return:
        """
        self.config_header()
        self.config_content()
        self.config_file()
        try:                                        #设置smtp信息
            smtp = smtplib.SMTP()
            smtp.connect(host)
            smtp.login(user, password)
            smtp.sendmail(sender, self.receiver, self.msg.as_string())
            smtp.quit()
        except Exception as ex:
            print('发送失败:{}'.format(ex))


class MyEmail:
    email = None
    mutex = threading.Lock()                 #线程锁

    def __init__(self):
        pass

    @staticmethod
    def get_email():

        if MyEmail.email is None:
            MyEmail.mutex.acquire()           #线程调用acquire方法获得锁，锁进入locked状态
            MyEmail.email = Email()           #启动Email初始化
            MyEmail.mutex.release()
        return MyEmail.email


if __name__ == "__main__":
    email = MyEmail.get_email()
    email.send_email()