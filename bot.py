from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class BadooBot():
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def login(self):
        self.driver.get('https://badoo.com/signin/')
        login_passw = self.driver.find_elements_by_class_name(
            'text-field__input')
        login_passw[0].clear()
        login_passw[0].send_keys('v.chelyadin2015@yandex.ru')
        login_passw[1].clear()
        login_passw[1].send_keys('Vlad756166vlad')
        sign_in = self.driver.find_element_by_name('post')
        sign_in.click()
        time.sleep(5)

    def like(self):
        like = self.driver.find_element_by_xpath(
            "//div[contains(@class,'js-profile-header-vote-yes js-profile-header-vote')]")
        like.click()
        time.sleep(0.5)

    def dislike(self):
        dislike = self.driver.find_element_by_xpath(
            "//div[contains(@class,'js-profile-header-vote-yes js-profile-header-vote')]")
        dislike.click()
        time.sleep(0.5)

    def close_pop(self):
        close_pop = self.driver.find_element_by_xpath(
            "//div[contains(@class,'btn btn--monochrome js-chrome-pushes-deny')]")
        close_pop.click()
        time.sleep(0.5)

    def close_x(self):
        close_x = self.driver.find_element_by_xpath(
            "//div[contains(@class,'icon icon--white js-ovl-close')]")
        close_x.click()
        time.sleep(1)

    def close_match(self):
        pass
        # close_match = self.driver.find_element_by_id()
        # close_match.click()
        # time.sleep(1)

    def send_hello(self):
        pass
        # message_line = self.driver.find_element_by_id()
        # message_line.clear()
        # message_line.send_keys('Привет :)')

    def auto_like(self):
        while True:
            try:
                self.like()
            except Exception:
                try:
                    self.close_pop()
                except Exception:
                    try:
                        self.close_x()
                    except Exception:
                        try:
                            self.send_hello()
                            self.close_match()
                        except Exception:
                            assert "Расширить критерии поиска" in self.driver.body
                            break
        print('DONE!!!')


# if __name__ == '__main__':
bot = BadooBot()
bot.login()
bot.auto_like()
print()
