from model.contact import Contact
import re
import time


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
        self.open_homepage()
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

    def modify_first_contact(self, new_group_data):
        self.modify_contact_by_index(0, new_group_data)
        self.contact_cache = None

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_homepage()
        self.select_contact_by_index(index)
        # open modification form
        wd.find_elements_by_xpath("(//table[@id='maintable']//img[@alt='Edit'])")[index].click()
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.open_homepage()
        self.select_contact_by_id(id)
        # open modification form
        wd.find_element_by_xpath('//a[@href="edit.php?id=%s"]' %id).click()
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)
        self.contact_cache = None

    def delete_contact_by_index(self, index):
         wd = self.app.wd
         self.open_homepage()
         self.select_contact_by_index(index)
         # submit deletion
         wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
         wd.switch_to_alert().accept()
         self.open_homepage()
         self.contact_cache = None

    def delete_contact_by_id(self, id):
         wd = self.app.wd
         self.open_homepage()
         self.select_contact_by_id(id)
         # submit deletion
         wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
         wd.switch_to_alert().accept()
         self.open_homepage()
         self.contact_cache = None

    def select_contact_by_index(self, index):
         wd = self.app.wd
         wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
         wd = self.app.wd
         wd.find_element_by_css_selector("input[value='%s']" % id).click()

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
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                first_name = cells[2].text
                surname = cells[1].text
                address = cells[3].text
                all_emails = cells[4].text
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(first_name=first_name, surname=surname, id=id,
                                                  all_phones_from_home_page=all_phones, address=address,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_homepage()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_homepage()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        surname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        land_line = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        land_line_2 = wd.find_element_by_name("phone2").get_attribute("value")
        email_1 = wd.find_element_by_name("email").get_attribute("value")
        email_2 = wd.find_element_by_name("email2").get_attribute("value")
        email_3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(first_name=first_name, surname=surname, address=address, id=id,
                       land_line=land_line, mobile=mobile, work=work, land_line_2=land_line_2,
                       email_1=email_1, email_2=email_2, email_3=email_3 )

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        if re.search("H:", text) is None:
            land_line = None
        else:
            land_line = re.search("H: (.*)", text).group(1)
        if re.search("M:", text) is None:
            mobile = None
        else:
            mobile = re.search("M: (.*)", text).group(1)
        if re.search("W:", text) is None:
            work = None
        else:
            work = re.search("W: (.*)", text).group(1)
        if re.search("P:", text) is None:
            land_line_2 = None
        else:
            land_line_2 = re.search("P: (.*)", text).group(1)
        return Contact(land_line=land_line, mobile=mobile, work=work, land_line_2=land_line_2)

    def add_contact_to_group(self, contact_id, group_id):
        wd = self.app.wd
        self.open_homepage()
        self.select_contact_by_id(contact_id)
        # select a group to add contact to
        wd.find_element_by_css_selector("select[name='to_group']>option[value='%s']" % group_id).click()
        wd.find_element_by_name("add").click()
        self.open_homepage()
        self.contact_cache = None



    def del_contact_from_group(self, contact_id, group_id):
        wd = self.app.wd
        self.open_homepage()
        wd.find_element_by_css_selector("select[name='group']>option[value='%s']" % group_id).click()
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name("remove").click()
        self.open_homepage()
        self.contact_cache = None