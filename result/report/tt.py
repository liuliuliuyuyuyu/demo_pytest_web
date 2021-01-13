import os

import readConfig
from result.report.configEmail import MyEmail

#测试路径
# path = os.path.join(readConfig.proDir, "result", "report", "report")
# for f in os.listdir(path):
#     absFile = os.path.join(path, f)  # 子文件的绝对路径
#     # print(absFile)
#     if os.path.isdir(absFile):  # 判断是文件夹，继续深度读取。
#         relFile = absFile[len(os.path.dirname(os.path.realpath(__file__))) + 1:]
#         print(relFile)


#测试邮件发送
email = MyEmail.get_email()
email.send_email()