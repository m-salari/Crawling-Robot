import time
from selenium import webdriver

class Istgah:
    def __init__(self, message, subject):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.istgah.com/')
        self.message = message
        self.subject = subject

    def Search(self):
        input_search = self.driver.find_element_by_css_selector("input[class = 'form-control']")
        input_search.send_keys(self.subject)
        time.sleep(2)
        button_search = self.driver.find_element_by_css_selector("button[type = 'submit']")
        button_search.click()

    def GetPost(self):
        self.Switch(0)
        time.sleep(3)
        lst_post = self.driver.find_elements_by_css_selector('a[class = "lititle"]')
        print(len(lst_post))

        for i in range(len(lst_post)):
            lst_post = self.driver.find_elements_by_css_selector('a[class = "lititle"]')
            print(lst_post[i].text)
            lst_post[i].click()
            result = self.SendMesssage()
            if result:
                self.Switch(0)
            time.sleep(3)
            self.driver.back()
            time.sleep(2)

    def NextPage(self):
        button_next_page = self.driver.find_element_by_css_selector("span[class = 'glyphicon glyphicon-chevron-left']")
        button_next_page.click()

    def main(self):
        self.Search()
        self.Whatsapp()
        time.sleep(1)
        while True:
            try:
                self.GetPost()
                self.NextPage()
                time.sleep(2)

            except Exception as e:
                print("error:", e)
                break

    def SendMesssage(self):
        path = '/html/body/div[5]/div[1]/div[2]/div[1]/div[2]/div[1]/div/div/a'
        lst_possible_path = ['', '[2]', '[3]']
        for j in range(4):
            try:
                button_whatsapp = self.driver.find_element_by_xpath(path + lst_possible_path[j])
                if button_whatsapp.text == 'چت واتساپ':
                    # print("path + lst_possible_path[j]:", path + lst_possible_path[j])
                    break
            except:
                return False

        button_whatsapp.click()
        self.Switch(1)
        while True:
            try:
                box_message = self.driver.find_element_by_css_selector("div[title = 'Type a message']")
                box_message.clear()
                time.sleep(1)
                box_message.send_keys(self.message)
                time.sleep(1)
                button_send = self.driver.find_element_by_css_selector("button[class = '_4sWnG']")
                button_send.click()
                break
            except:
                print("waiting to open whatsapp...")
                time.sleep(2)

        time.sleep(2)
        self.driver.close()
        return True

    def Whatsapp(self):
        self.driver.execute_script("window.open('" + 'https://web.whatsapp.com/' + "', '_blank')")
        self.Switch(1)
        input("after login press enter")
        self.driver.close()

    def Switch(self, page):
        windows = self.driver.window_handles[page]
        self.driver.switch_to.window(windows)


subject = 'کامیون'
msg = "hello"

i = Istgah(msg, subject)
i.main()
