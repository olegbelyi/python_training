from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_homepage(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_homepage()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        self.add_avatar(contact)
        self.change_birth_date(contact)
        self.change_anniversary_date(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def create_light(self, contact):
        # creation of a contact without avatar and dates
        wd = self.app.wd
        self.open_homepage()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("lastname", contact.surname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company_name)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.land_line)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email_1)
        self.change_field_value("email2", contact.email_2)
        self.change_field_value("email3", contact.email_3)
        self.change_field_value("homepage", contact.homepage)
        # self.change_birth_date(contact)
        self.change_field_value("byear", contact.birthday_year)
        # self.change_anniversary_date(contact)
        self.change_field_value("ayear", contact.anniversary_year)
        self.change_field_value("address2", contact.second_address)
        self.change_field_value("phone2", contact.land_line_2)
        self.change_field_value("notes", contact.notes)


    def change_anniversary_date(self, contact):
        wd = self.app.wd
        if not wd.find_element_by_xpath(contact.anniversary_day).is_selected():
            wd.find_element_by_xpath(contact.anniversary_day).click()
        if not wd.find_element_by_xpath(contact.anniversary_month).is_selected():
            wd.find_element_by_xpath(contact.anniversary_month).click()

    def modify_first_contact_anniversary_date(self, contact):
        wd = self.app.wd
        self.select_first_contact()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        if not wd.find_element_by_xpath(contact.anniversary_day).is_selected():
            wd.find_element_by_xpath(contact.anniversary_day).click()
        if not wd.find_element_by_xpath(contact.anniversary_month).is_selected():
            wd.find_element_by_xpath(contact.anniversary_month).click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.anniversary_year)
        wd.find_element_by_name("update").click()

    def change_birth_date(self, contact):
        wd = self.app.wd
        if not wd.find_element_by_xpath(contact.birthday_day).is_selected():
            wd.find_element_by_xpath(contact.birthday_day).click()
        if not wd.find_element_by_xpath(contact.birthday_month).is_selected():
            wd.find_element_by_xpath(contact.birthday_month).click()

    def modify_first_contact_birthday(self, contact):
        wd = self.app.wd
        self.select_first_contact()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        if not wd.find_element_by_xpath(contact.birthday_day).is_selected():
            wd.find_element_by_xpath(contact.birthday_day).click()
        if not wd.find_element_by_xpath(contact.birthday_month).is_selected():
            wd.find_element_by_xpath(contact.birthday_month).click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birthday_year)
        wd.find_element_by_name("update").click()

    def add_avatar(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("photo").send_keys(contact.avatar)

    def modify_first_contact_avatar(self, contact):
        wd = self.app.wd
        self.select_first_contact()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        wd.find_element_by_name("photo").send_keys(contact.avatar)
        wd.find_element_by_name("update").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_homepage()
        self.select_first_contact()
        # open modification form
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd = self.app.wd

    def delete_first_contact(self):
         wd = self.app.wd
         self.open_homepage()
         self.select_first_contact()
         # submit deletion
         wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
         wd.switch_to_alert().accept()
         self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_homepage()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache=None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_homepage()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                td_value = element.find_elements_by_tag_name("td")
                text1 = td_value[2].text
                text2 = td_value[1].text
                # print (text1 + " " + text2)
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(first_name=text1, surname=text2, id=id))

        return list (self.contact_cache)