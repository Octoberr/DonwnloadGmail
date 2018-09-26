"""
使用selenium模拟浏览器登陆gmail
调试的时候使用有界面的浏览器，
运行时可以使用无界面的浏览器
create by swm 20180919
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from functools import wraps
import time

# 计时器
def func_timer(function):
    '''
    用装饰器实现函数计时
    :param function: 需要计时的函数
    :return: None
    '''

    @wraps(function)
    def function_timer(*args, **kwargs):
        print('[Function: {name} start...]'.format(name=function.__name__))
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print('[Function: {name} finished, spent time: {time:.2f}s]'.format(name=function.__name__, time=t1 - t0))
        return result

    return function_timer


class gmail:

    def __init__(self, account, pwd):
        self.account = account
        self.pwd = pwd

    @func_timer
    def doit(self):
        chrome_options = Options()
        # 无头
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('lang=zh_CN.UTF-8')
        # chrome_options.add_argument("--window-size=1920x1080")
        # chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")
        chrome_options.add_experimental_option("prefs", {'profile.managed_default_content_settings.javascript': 2})
        chrome_driver = "./chromedriver.exe"
        # driver = webdriver.Chrome(executable_path=chrome_driver)
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
        # 1、打开登陆界面
        # driver.get("https://accounts.google.com/AccountChooser?service=mail&continue=https://mail.google.com/mail/")
        # no js
        driver.get("https://mail.google.com/mail/u/0/h/7ckx97bme0zo/?zy=c&f=1")
        # 输入账号密码然后下一步
        # accountnumber = driver.find_element_by_css_selector("#identifierId")
        # nojs
        accountnumber = driver.find_element_by_id("Email")
        accountnumber.send_keys(self.account)
        accountnumber.send_keys(Keys.ENTER)
        try:
            # passwd = WebDriverWait(driver, 10).until(
            #     EC.text_to_be_present_in_element((By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "daaWTb", " " ))]'), "忘记了密码？")
            # )
            # passwd = driver.find_element_by_css_selector(".zHQkBf")
            # nojs
            passwd = driver.find_element_by_id('Passwd')
            passwd.send_keys(self.pwd)
            passwd.send_keys(Keys.ENTER)
        except Exception as err:
            print("Error:{}\n跳转密码界面失败".format(err))
        # 跳转gmail登陆后的界面
        # 后面要增加手机验证码的情况,现在

        try:
            # for handle in driver.window_handles:
            #     driver.switch_to.window(handle)
            # 统计窗口数量
            # print(len(driver.window_handles))
            # google邮箱自己重定向后需要重新获取当前浏览器句柄
            driver.switch_to.window(driver.window_handles[0])
            inbox = WebDriverWait(driver, 20).until(
                EC.title_contains('收件箱'))
            print('登陆成功，已到收件箱')
            # print("已经跳转到登陆后的界面")
        except Exception as err:
            print("Error:{},跳转收件箱失败".format(err))
        # 打开设置页面
        # driver.find_element_by_id(':28').click()
        # time.sleep(0.5)
        # driver.find_element_by_xpath('//*[@id="ms"]').click()
        # try:
        #     setting = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "G-atb", " " ))]'), '设置'))
        # except Exception as err:
        #     print("error:{}, 没有跳转到到设置界面".format(err))
        #
        # driver.find_element_by_css_selector('#\:n6 .LJOhwe').click()
        # driver.switch_to.window(driver.window_handles[0])
        # time.sleep(0.5)
        # driver.find_element_by_name('bx_ie').click()
        # time.sleep(0.5)
        # driver.find_element_by_partial_link_text('保存更改').click()
        # no js 打开设置
        driver.find_element_by_link_text('设置').click()
        time.sleep(0.5)
        driver.find_element_by_link_text('转发和POP/IMAP').click()
        time.sleep(0.5)
        driver.find_element_by_name('p_bx_ie').click()
        time.sleep(0.5)
        driver.find_element_by_name('nvp_a_prefs').click()
        print("启用imap成功")
        # 最后关闭标签页
        driver.quit()


if __name__ == '__main__':
    account = "ocojud1@gmail.com"
    pwd = "ADSZadsz123"
    gg = gmail(account, pwd)
    gg.doit()

