import datetime
from re import S
import smtplib
import time
from datetime import timedelta
from email.header import Header
from email.mime.text import MIMEText


def caltime(date1, date2):
    date1 = time.strptime(date1, "%Y-%m-%d")
    date2 = time.strptime(date2, "%Y-%m-%d")
    date1 = datetime.datetime(date1[0], date1[1], date1[2])
    date2 = datetime.datetime(date2[0], date2[1], date2[2])
    return(date2-date1).days

def rtday(day):
    baby = selectBaby()

    print(str(day))
    dl = str(day).split()

    time1 = str(baby['brithday'])
    time2 = dl[0]
    return caltime(time1, time2)

def retYearMonth():
    y = datetime.datetime.now().strftime("%Y")  # 年份
    m = datetime.datetime.now().strftime("%m")  # 月份

    return "{}-{}".format(y,m)

def retWeekend():
    now = datetime.datetime.now()
    this_week_end = now + timedelta(days=6 - now.weekday())
    return (str(this_week_end.year) + "-" + str(this_week_end.month) + "-" + str(this_week_end.day))

def get_weekday(date):
    week_map = {0: '一', 1: '二', 2: '三', 3: '四', 4: '五', 5: '六', 6: '日'}
    week = datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
    return  f"{date} 星期{week_map[week]}"

#日期
today = (str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(
            datetime.datetime.now().day))

holidays =[
    ['周末',retWeekend()],
    ['愚人节','2022-04-01'],
    ['清明节','2022-04-05'],
    ['劳动节','2022-05-01'],
    ['端午节','2022-06-03'],
    ['中秋节','2022-09-10'],
    ['国庆节','2022-10-01'],
    ['程序员节','2022-10-24'],
    ['圣诞节','2022-12-25'],
    ['元旦','2023-01-01'],
    ['春节','2023-01-22'],
    ['情人节','2023-02-14'],
]

def main():
    '''
    程序入口
    '''
    # str_1 ='[摸鱼办提醒您]:今天是'+get_weekday(today)+'，冬季寒冷，注意保暖，少喝凉水。工作再累，一定不要忘记摸鱼哦！有事没事起身去茶水间，去厕所，去廊道走走别老在工位上坐着，钱是老板的,但命是自己的。'
    str_1 ='[摸鱼办提醒您]:今天是'+get_weekday(today)+'，新春伊始,万物复苏,加油吧!打工人。工作再累，一定不要忘记摸鱼哦！有事没事起身去茶水间，去厕所，去廊道走走别老在工位上坐着，钱是老板的,但命是自己的。'
    str_2 = ''
    str_3 = '认认真真上班，这根本就不叫赚钱，那是用劳动换取报酬。只有偷懒，在上班的时候摸鱼划水，你才是从老板手里赚到了钱。最后，祝愿天下所有摸鱼人都能愉快的渡过每一天！'
    print(str_1)
    for i in holidays:
        print("距离"+i[0]+"还有"+ str(caltime(today,i[1]))+ "天")
    print(str_3)


mail_host="smtp.XXX.com"  #设置服务器  
mail_user="XXXXX"    #用户名
mail_pass="XXXXX"   #口令 
 
 
sender = 'XXXXXX'
receivers = ['XXXXX']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
message = MIMEText( 
    '[摸鱼办提醒您]:今天是'+get_weekday(today)+'，新春伊始,万物复苏,加油吧!打工人。工作再累，一定不要忘记摸鱼哦！有事没事起身去茶水间，去厕所，去廊道走走别老在工位上坐着，钱是老板的,但命是自己的。'
    '----------------------------------------------------------------'
    '认认真真上班，这根本就不叫赚钱，那是用劳动换取报酬。只有偷懒，在上班的时候摸鱼划水，你才是从老板手里赚到了钱。最后，祝愿天下所有摸鱼人都能愉快的渡过每一天！', 'plain', 'utf-8')
message['From'] = Header("摸鱼办", 'utf-8')
message['To'] =  Header("摸鱼小达人", 'utf-8')
 
subject = 'Py摸鱼办公室'
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException as e:
    print('error',e)
    print ("Error: 无法发送邮件")
 


 