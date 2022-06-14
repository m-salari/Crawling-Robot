import time
import random
from selenium import webdriver

subject_search = 'https://www.instagram.com/accounts/login/'


class FollowInstagram:
    def __init__(self, username, password, list_message):
        self.username = username
        self.password = password

        self.driver = webdriver.Firefox()
        self.driver.get(subject_search)
        self.flag_follow = 0
        self.flag_direct = 0
        self.lst_message = list_message

    def Login(self, username, password):
        input_username = self.driver.find_element_by_css_selector("input[name = 'username']")
        input_username.send_keys(username)

        input_password = self.driver.find_element_by_css_selector("input[name = 'password']")
        input_password.send_keys(password)

        button_login = self.driver.find_element_by_css_selector("button[type = 'submit']")
        button_login.click()

        time.sleep(4)

        print("press on button_save_info ")
        button_save_info = self.driver.find_element_by_css_selector("button[class = 'sqdOP yWX7d    y3zKF     ']")
        button_save_info.click()

        time.sleep(5)

        print("press on button_notification ")
        button_notification = self.driver.find_element_by_css_selector("button[class = 'aOOlW   HoLwm ']")
        button_notification.click()

    def ReplaceLine(self, file_name, line_num):
        read = open(file_name, 'r')
        lines = read.readlines()
        if lines[line_num][0] != '-':
            lines[line_num] = '-' + lines[line_num]
            read.close()
            out = open(file_name, 'w')
            out.writelines(lines)
            out.close()
        else:
            read.close()

    def Search(self, id):
        self.driver.get(id)

    def main(self):
        self.Login(self.username, self.password)
        time.sleep(2)
        f = open("insta_usernames.txt", "r")
        users = f.readlines()
        for i in range(len(users)):
            users[i] = users[i].replace("\n", '')
            user = users[i]
            if user[0] == '-':
                user = user[1:]
            print(user)
            self.Search(user)
            time.sleep(5)
            self.FollowOrDirect()
            self.ReplaceLine("insta_usernames.txt", i)
            time.sleep(6)

    def FollowOrDirect(self):
        try:
            button_message = self.driver.find_element_by_css_selector('.sqdOP')
            # print("try send message")
            if self.flag_direct == 1:
                # time.sleep(8 * 60)
                count_d = 30
                while count_d > 0:
                    print('please wait for {0} seconds'.format(count_d))
                    count_d -= 1
                    time.sleep(1)
                self.flag_direct = 0
                self.flag_follow = 0

            button_message.click()
            time.sleep(5)
            self.SendMessage()
            self.flag_direct = 1

        except:
            try:
                button_follow = self.driver.find_element_by_css_selector('._6VtSN')
                # print("button_follow:", button_follow.text)
                if button_follow.text == "Follow":
                    # print("try follow")
                    if self.flag_follow == 1:
                        # time.sleep(8 * 60)
                        count_f = 20
                        while count_f > 0:
                            print('please wait for {0} seconds'.format(count_f))
                            count_f -= 1
                            time.sleep(1)
                        self.flag_follow = 0
                        self.flag_direct = 0

                    button_follow.click()
                    self.flag_follow = 1
                else:
                    raise ValueError
            except:
                print("can not follow and direct")


    def SendMessage(self):
        message = random.choice(self.lst_message)
        text_message = self.driver.find_element_by_css_selector('.ItkAi > textarea:nth-child(1)')
        text_message.send_keys(message)

        # button_send = self.driver.find_element_by_css_selector("div.qF0y9:nth-child(3) > button:nth-child(1)")
        # button_send.click()


# username = "username"
# password = "password"
lst_message = ['سلام', 'سال تحویل', 'نوروز']
f = FollowInstagram(username, password, lst_message)
f.main()

# حداکثر 50 دایرکت در روز به فاصله 5 -8 دقیقه
# پیام های تکراری ارسال نکنید
# در بازه زمانی یک ساعت تنها اجازه فالو کردن 10 نفر , در روز حدود 200 نفر
