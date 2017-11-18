# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import Contact
def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)

    def open_homepage(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        self.open_homepage(wd)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def create_contact(self, wd, contact):
        # init contact creation
         wd.find_element_by_link_text("add new").click()
         # fill contact form
         wd.find_element_by_name("firstname").click()
         wd.find_element_by_name("firstname").clear()
         wd.find_element_by_name("firstname").send_keys(contact.first_name)
         wd.find_element_by_name("middlename").click()
         wd.find_element_by_name("middlename").clear()
         wd.find_element_by_name("middlename").send_keys(contact.middle_name)
         wd.find_element_by_name("lastname").click()
         wd.find_element_by_name("lastname").clear()
         wd.find_element_by_name("lastname").send_keys(contact.surname)
         wd.find_element_by_name("photo").send_keys(contact.avatar)
         wd.find_element_by_name("nickname").click()
         wd.find_element_by_name("nickname").clear()
         wd.find_element_by_name("nickname").send_keys(contact.nickname)
         wd.find_element_by_name("theform").click()
         wd.find_element_by_name("title").click()
         wd.find_element_by_name("title").clear()
         wd.find_element_by_name("title").send_keys(contact.title)
         wd.find_element_by_name("theform").click()
         wd.find_element_by_name("company").click()
         wd.find_element_by_name("company").clear()
         wd.find_element_by_name("company").send_keys(contact.company_name)
         wd.find_element_by_css_selector("body").click()
         wd.find_element_by_name("address").click()
         wd.find_element_by_name("address").clear()
         wd.find_element_by_name("address").send_keys(contact.address)
         wd.find_element_by_name("home").click()
         wd.find_element_by_name("home").clear()
         wd.find_element_by_name("home").send_keys(contact.land_line)
         wd.find_element_by_name("mobile").click()
         wd.find_element_by_name("mobile").clear()
         wd.find_element_by_name("mobile").send_keys(contact.mobile)
         wd.find_element_by_name("work").click()
         wd.find_element_by_name("work").clear()
         wd.find_element_by_name("work").send_keys(contact.work)
         wd.find_element_by_name("fax").click()
         wd.find_element_by_name("fax").clear()
         wd.find_element_by_name("fax").send_keys(contact.fax)
         wd.find_element_by_name("email").click()
         wd.find_element_by_name("email").clear()
         wd.find_element_by_name("email").send_keys(contact.email_1)
         wd.find_element_by_name("theform").click()
         wd.find_element_by_name("email2").click()
         wd.find_element_by_name("email2").clear()
         wd.find_element_by_name("email2").send_keys(contact.email_2)
         wd.find_element_by_name("email3").click()
         wd.find_element_by_name("email3").clear()
         wd.find_element_by_name("email3").send_keys(contact.email_3)
         wd.find_element_by_name("homepage").click()
         wd.find_element_by_name("homepage").clear()
         wd.find_element_by_name("homepage").send_keys(contact.homepage)
         if not wd.find_element_by_xpath(contact.birthday_day).is_selected():
                wd.find_element_by_xpath(contact.birthday_day).click()
         if not wd.find_element_by_xpath(contact.birthday_month).is_selected():
                wd.find_element_by_xpath(contact.birthday_month).click()
         wd.find_element_by_name("byear").click()
         wd.find_element_by_name("byear").clear()
         wd.find_element_by_name("byear").send_keys(contact.birthday_year)
         wd.find_element_by_name("theform").click()
         if not wd.find_element_by_xpath(contact.anniversary_day).is_selected():
                wd.find_element_by_xpath(contact.anniversary_day).click()
         if not wd.find_element_by_xpath(contact.anniversary_month).is_selected():
                wd.find_element_by_xpath(contact.anniversary_month).click()
         wd.find_element_by_name("ayear").click()
         wd.find_element_by_name("ayear").clear()
         wd.find_element_by_name("ayear").send_keys(contact.anniversary_year)
         wd.find_element_by_name("theform").click()
         wd.find_element_by_name("address2").click()
         wd.find_element_by_name("address2").clear()
         wd.find_element_by_name("address2").send_keys(contact.second_address)
         wd.find_element_by_name("phone2").click()
         wd.find_element_by_name("phone2").clear()
         wd.find_element_by_name("phone2").send_keys(contact.land_line_2)
         wd.find_element_by_name("notes").click()
         wd.find_element_by_name("notes").clear()
         wd.find_element_by_name("notes").send_keys(contact.notes)
         # submit contact creation
         wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_add_contact(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.create_contact(wd, Contact(first_name="Pavel", middle_name="Ivanovich", surname="Kolosov", avatar="C:\\Users\\slaterr\\Pictures\\avatar.jpg", nickname="Kolos",
                            title="Mr", company_name="Cobelco", address="85, Queen street, Auckland, New Zealand", land_line="+642223334455",
                            mobile="+642223335556", work="+643334246622", fax="+644442221189", email_1="kolos@gmail.com", email_2="kolos@yahoo.com",
                            email_3="kolos@mail.ru", homepage="http://kolos.info", birthday_day="//div[@id='content']/form/select[1]//option[6]",
                            birthday_month="//div[@id='content']/form/select[2]//option[7]", birthday_year="1980",
                            anniversary_day="//div[@id='content']/form/select[3]//option[4]",
                            anniversary_month="//div[@id='content']/form/select[4]//option[2]", anniversary_year="1999",
                            second_address="30 Orakau Avenue, Epsom, Auckland, New Zealand ", land_line_2="+645556667788", notes="Skype ID: kolos1980"))
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
