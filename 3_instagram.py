import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select

subject_search = 'https://www.instagram.com/accounts/login/'


class instagram:
    def __init__(self, username, password, userid, count):
        self.username = username
        self.password = password
        self.id = userid
        self.max = count

        self.driver = webdriver.Firefox()
        self.driver.get(subject_search)



    def Login(self, username, password):
        input_username = self.driver.find_element_by_css_selector("input[name = 'username']")
        input_username.send_keys(username)

        input_password = self.driver.find_element_by_css_selector("input[name = 'password']")
        input_password.send_keys(password)

        button_login = self.driver.find_element_by_css_selector("button[type = 'submit']")
        button_login.click()

        time.sleep(4)

        button_save_info = self.driver.find_element_by_css_selector("button[class = 'sqdOP yWX7d    y3zKF     ']")
        button_save_info.click()

        time.sleep(3)

        print("prress on button_notification ")
        button_notification = self.driver.find_element_by_css_selector("button[class = 'aOOlW   HoLwm ']")
        button_notification.click()

    def Search(self):
        link = "https://www.instagram.com/{0}/".format(self.id)
        self.driver.get(link)

    def ClickOnFollowing(self):
        WebDriverWait(self.driver, 1000000).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/div'))).click()

    def ClickOnFollwers(self):
        WebDriverWait(self.driver, 1000000).until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div'))).click()

    def GetUsers(self, max):
        f = open("insta_usernames.txt", "w")

        count = 0
        time.sleep(5)
        followersList = self.driver.find_element_by_css_selector('div[role=\'dialog\'] ul')
        # numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))

        followersList.click()
        actionChain = webdriver.ActionChains(self.driver)

        j = 0
        while (count < max):
            try:
                # print("j:",j)
                count_of_users = len(followersList.find_elements_by_css_selector('li'))
                time.sleep(3)

                for i in range(j, count_of_users):
                    user = followersList.find_elements_by_css_selector('li')[i]

                    userLink = user.find_element_by_css_selector('a').get_attribute('href')
                    print("count:", count)
                    print(userLink)
                    f.write(str(userLink))
                    f.write("\n")

                    count += 1
                    if count == max:
                        break


            except Exception as e:
                print(str(e))
                pass
                # actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            j = i + 1
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()


    def main(self):
        self.Login(self.username, self.password)
        time.sleep(2)
        self.Search()
        time.sleep(2)
        self.ClickOnFollwers()
        # self.ClickOnFollowing()
        time.sleep(2)
        self.GetUsers(self.max)


user = "username"
paswrd = "password"

ids = 'hassan_reyvandi'

i = instagram(user, paswrd, ids, 20)
i.main()



