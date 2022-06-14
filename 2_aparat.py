import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class divar:
    def __init__(self, message, subject_search):
        self.drive = webdriver.Firefox()
        self.subject = subject_search
        self.drive.get('https://www.aparat.com')
        self.message = message

    def GetPostInPage(self, max):

        l = 0
        count_e = 1
        button_home = self.drive.find_element_by_css_selector("a[class = 'title']")
        button_home.click()
        time.sleep(3)
        while True:
            try:
                button_all_video = self.drive.find_element_by_css_selector(
                    'li.tab-item:nth-child(2) > a:nth-child(1) > '
                    'button:nth-child(1)')
                button_all_video.click()

                time.sleep(1)

                lst_post = self.drive.find_elements_by_css_selector("a[class = 'titled-link title']")
                len_lst = len(lst_post)
                # print(len_lst)

                if l == len_lst:
                    raise ValueError('error index')


                if l == max:
                    # l = 0
                    print("start clicked 0")
                    # lst_post = self.drive.find_elements_by_css_selector("a[class = 'titled-link title']")
                    lst_post[0].click()
                    print("finish clicked 0")
                    # time.sleep(3)
                    for q in range(3):
                        try:
                            time.sleep(2)
                            self.SendMessage(self.message)
                            break
                        except Exception as e:
                            self.Down(1)
                            if count_e == 3:
                                print("can not send message :", e)
                                # break
                            count_e += 1
                    break

                print(f'post {l}:', lst_post[l].text)
                time.sleep(1)
                lst_post[l].click()

                result = self.Check()
                if result:
                    break

                time.sleep(2)
                self.drive.back()
                l += 1

                time.sleep(2)

            except Exception as e:
                # print("error :",e)
                html = self.drive.find_element_by_tag_name('html')
                html.send_keys(Keys.END)
                time.sleep(3)
                lst_post = self.drive.find_elements_by_css_selector("a[class = 'titled-link title']")
                len_lst = len(lst_post)
                if l == len_lst:
                    lst_post[0].click()
                    self.Down(1)
                    self.SendMessage(self.message)
                    print("finish post")
                    break

    def Check(self):
        time.sleep(2)
        username = self.GetUsername()
        self.Down(2)
        lst_username__in_comment = self.drive.find_elements_by_css_selector("a[class = 'sc-iqseJM glJLgl link']")
        for i in range(len(lst_username__in_comment)):
            # print(lst_username__in_comment[i].text)
            if lst_username__in_comment[i].text == username:
                print("**** Your comment was found!!! **** ")
                return True

    def SendMessage(self, msg):
        input_comment = self.drive.find_element_by_css_selector("#CommentInsert")
        input_comment.send_keys(msg)

        time.sleep(1)

        button_send = self.drive.find_element_by_css_selector("button[aria-label = 'send']")
        button_send.click()
        print("send message success !!!")

        self.Sleep(60)

    def Sleep(self, t):
        time_wait = t
        while time_wait > 0:
            print(f"please wait for {time_wait} seconds...")
            time.sleep(1)
            time_wait -= 1

    def GetUsername(self):
        profile = self.drive.find_element_by_css_selector("img[class = 'sc-fKVqWL bqGhDG']")
        username = profile.get_attribute('alt')
        return username

    def Main(self, max):
        input("aftet login in divar ; please press enter:")
        l = 0
        while True:
            self.drive.get(self.subject)
            time.sleep(3)
            try:
                time.sleep(2)
                lst_post = self.drive.find_elements_by_css_selector("a[class = 'titled-link title']")
                len_lst = len(lst_post)
                # print(len_lst)

                if l == len_lst:
                    raise ValueError('error index')

                print(f'number {l}:', lst_post[l].text)
                time.sleep(1)
                lst_post[l].click()
                time.sleep(5)
                self.GetPostInPage(max)
                time.sleep(3)
                l += 1

                time.sleep(2)

            except Exception as e:
                # print("error :",e)
                html = self.drive.find_element_by_tag_name('html')
                html.send_keys(Keys.END)
                time.sleep(3)
                if l == len(self.drive.find_elements_by_css_selector("a[class = 'titled-link title']")):
                    print("finish post in subject")
                    break

    def Down(self, count):
        for c in range(count):
            html = self.drive.find_element_by_tag_name('html')
            html.send_keys(Keys.END)
            time.sleep(3)

    def Back(self, count):
        for i in range(count):
            self.drive.back()

# subject_search = 'https://www.aparat.com/search/%D9%88%D8%B1%D8%B2%D8%B4%DB%8C'
subject_search = 'https://www.aparat.com/search/%D9%85%D9%87%D8%A7%D8%AC%D8%B1%D8%AA'
message = 'درود'
d = divar(message, subject_search)
d.Main(5)



