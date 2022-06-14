import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class divar:
    def __init__(self, message, subject_search):
        self.drive = webdriver.Firefox()
        self.drive.get(subject_search)
        self.message = message

    def SendMessage(self, message):
        try:
            time.sleep(3)
            button_chat = self.drive.find_element_by_css_selector('button[class = "kt-button kt-button--outlined '
                                                                  'contact-button chat-button"]')
            button_chat.click()
            time.sleep(2)

            try:
                button_accept_roles = self.drive.find_element_by_css_selector('button[class = "kt-button '
                                                                              'kt-button--primary"]')
                button_accept_roles.click()
            except Exception as e:
                print('error in accept roles:', e)

            time.sleep(1)
            try:
                input_text = self.drive.find_element_by_css_selector('input[class = "kt-chat-input__input '
                                                                     'kt-body--stable"]')
                input_text.send_keys(message)
                time.sleep(1)
                button_send = self.drive.find_element_by_css_selector('button[class = "kt-button kt-button--primary '
                                                                     'kt-button--circular kt-chat-input__button"]')
                button_send.click()
                time.sleep(2)
                self.drive.back()
            except Exception as e:
                print("error in button send", e)
        except Exception as e:
            print("error in press button chat:", e)


    def GetPostInPage(self):
        l = 0
        input("aftet login in divar please press enter:")

        while True:
            try:

                lst_post = self.drive.find_elements_by_css_selector('div[class = "kt-post-card__title"]')
                len_lst = len(lst_post)
                # print(len_lst)
                while True:
                    try:
                        if len_lst != 0:
                            break
                        self.drive.back()
                        time.sleep(1)
                        lst_post = self.drive.find_elements_by_css_selector('div[class = "kt-post-card__title"]')
                        len_lst = len(lst_post)
                        # print("len_lst in while", len_lst)
                    except:
                        pass
                    time.sleep(1)
                # print("out of while")

                if l == len_lst:
                    raise ValueError('error index')

                try:
                    # print('number:', l, lst_post[l].text)
                    time.sleep(1)
                    # print("click start")
                    lst_post[l].click()
                    # print("click finish")
                    self.SendMessage(self.message)
                    l += 1

                except Exception as e:
                    print("error:",e)
                    s = True
                    last_index = l
                    while s:
                        try:
                            # print('number - 1:', last_index, lst_post[last_index].text)
                            lst_post[last_index].click()
                            s = False
                        except:
                            last_index -= 1
                            # print("last_index in error :", last_index)

                time.sleep(3)

            except Exception as e:
                print("error :",e)
                html = self.drive.find_element_by_tag_name('html')
                html.send_keys(Keys.END)
                time.sleep(5)


subject_search = 'https://divar.ir/s/tehran?q=%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84'
message = 'سلام'
d = divar(message, subject_search)
d.GetPostInPage()


