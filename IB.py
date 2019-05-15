from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import getpass

#   This bot is for expanding your reach on Instagram and building a strong
#   network. After prompting you for your username and password,
#   you can add as many hashtags as you would like, and the script will like
#   its most recent and top photos, staying under a total of 1000 liked
#   posts. I didn't create a follow feature because I personally don't care
#   for gaining more followers, I'm just looking for other accounts to interact
#   with.

class InstagramBot:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()

        #   loop verifies correct username and password

        login_success = False
        while not login_success:
            time.sleep(2)
            username_elem = driver.find_element_by_xpath("//input[@name='username']")
            password_elem = driver.find_element_by_xpath("//input[@name='password']")
            username_input = raw_input("username: ")
            password_input = getpass.getpass(prompt='password: ')
            username_elem.send_keys(username_input)
            password_elem.send_keys(password_input)
            password_elem.send_keys(Keys.RETURN)
            time.sleep(2)
            try:
                login_error = driver.find_element_by_id('slfErrorAlert')
                print login_error
                print('incorrect username or password. trying again')
                driver.refresh()
            except Exception as e:
                login_success = True
                print('login successful')

        #       close notifications popup

        try:
            popup_button = driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']")
            popup_button.click()
        except Exception as e:
            pass
        time.sleep(2)

    def like_photo(self, hashtag, limit):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)

        # click through pictures to like them

        pic_href = driver.find_element_by_tag_name('a')
        pic_href.click()
        time.sleep(2)
        count = 0
        while count < limits:
            try:
                driver.find_element_by_xpath("//span[@aria-label='Like']").click()
                print('liked pic #' + str(count))
                count += 1
                time.sleep(36)
            except Exception as e:
                time.sleep(2)
            continue_link = driver.find_element_by_link_text('Next')
            continue_link.click()
            time.sleep(2)
        print('liked ' + str(limits) + ' pictures in #' + hashtag)



IG = InstagramBot()
IG.login()
hashtag_input = raw_input("hashtags (separate w/commas): ")
hashtags = [x.strip() for x in hashtag_input.split(',')]
limits = 1000 / len(hashtags)
for hashtag in hashtags:
    print('liking ' + str(limits) + ' pictures in #' + hashtag)
    IG.like_photo(hashtag, limits)
print('finished liking pictures')
IG.closeBrowser()
