import RPi.GPIO as GPIO
import time
import smtplib
from email.message import EmailMessage
import PCF8591 as ADC

# 初始化PCF8591模块
ADC.setup(0x48)

# 设置GPIO模式和引脚
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

# 邮件相关设置
# 请替换为你的发送方邮箱地址
from_email_addr = "REPLACE_WITH_THE_SENDER_EMAIL"
# 请替换为你的发送方邮箱App密码
from_email_pass = "REPLACE_WITH_THE_SENDER_EMAIL_APP_PASSWORD"
# 请替换为你的接收方邮箱地址
to_email_addr = "REPLACE_WITH_THE_RECIPIENT_EMAIL"

# 初始化最大和最小湿度读数
max_reading = 0
min_reading = 1023


def callback(channel):
    if GPIO.input(channel):
        print("Water Detected!")
    else:
        print("No Water Detected!")


GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)


def send_email(max_reading, min_reading):
    msg = EmailMessage()
    body = f"Today's maximum moisture reading: {max_reading}\nToday's minimum moisture reading: {min_reading}"
    msg.set_content(body)
    msg['From'] = from_email_addr
    msg['To'] = to_email_addr
    msg['Subject'] = 'Daily Moisture Report'

    server = smtplib.SMTP('smtp.gmail.com', 587)  # 根据你的邮箱提供商修改
    server.starttls()
    server.login(from_email_addr, from_email_pass)
    server.send_message(msg)
    print("Email sent")
    server.quit()


try:
    day_count = 0
    while day_count < 5:
        reading_count = 0
        max_reading = 0
        min_reading = 1023
        while reading_count < 5:
            potentiometer_value = ADC.read(0)
            print(f"Sensor reading: {potentiometer_value}")
            if potentiometer_value > max_reading:
                max_reading = potentiometer_value
            if potentiometer_value < min_reading:
                min_reading = potentiometer_value
            reading_count += 1
            time.sleep(3600)  # 间隔1小时
        send_email(max_reading, min_reading)
        day_count += 1
        time.sleep(3600)  # 确保每天发送邮件的间隔
except KeyboardInterrupt:
    print("Exit")
finally:
    GPIO.cleanup()
