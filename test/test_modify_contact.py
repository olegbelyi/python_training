# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_first_name(app):
        app.contact.modify_first_contact(Contact(first_name="New first name"))


def test_modify_contact_middle_name(app):
         app.contact.modify_first_contact(Contact(middle_name="New middle name"))


def test_modify_contact_surname(app):
         app.contact.modify_first_contact(Contact(surname="New surname"))


def test_modify_contact_avatar(app):
         app.contact.modify_first_contact_avatar(Contact(avatar="C:\\Users\\slaterr\\Pictures\\avatar_2.jpg"))


def test_modify_contact_nickname(app):
         app.contact.modify_first_contact(Contact(nickname="New nickname"))


def test_modify_contact_title(app):
         app.contact.modify_first_contact(Contact(title="Ms"))


def test_modify_contact_company_name(app):
         app.contact.modify_first_contact(Contact(company_name="New company name"))


def test_modify_contact_address(app):
         app.contact.modify_first_contact(Contact(address="New address"))


def test_modify_contact_land_line(app):
         app.contact.modify_first_contact(Contact(land_line="New land line"))


def test_modify_contact_mobile(app):
         app.contact.modify_first_contact(Contact(mobile="New mobile"))


def test_modify_contact_work(app):
         app.contact.modify_first_contact(Contact(work="New work phone"))


def test_modify_contact_fax(app):
         app.contact.modify_first_contact(Contact(fax="New fax"))


def test_modify_contact_email_1(app):
        app.contact.modify_first_contact(Contact(email_1="New email 1"))


def test_modify_contact_email_2(app):
        app.contact.modify_first_contact(Contact(email_2="New email 2"))


def test_modify_contact_email_3(app):
        app.contact.modify_first_contact(Contact(email_3="New email 3"))


def test_modify_contact_homepage(app):
         app.contact.modify_first_contact(Contact(homepage="http://newhome.page"))


def test_modify_contact_birthday(app):
          app.contact.modify_first_contact_birthday(Contact(birthday_day="//div[@id='content']/form/select[1]//option[7]", birthday_month="//div[@id='content']/form/select[2]//option[6]", birthday_year="1999"))


def test_modify_contact_anniversary_date(app):
          app.contact.modify_first_contact_anniversary_date(Contact(anniversary_day="//div[@id='content']/form/select[3]//option[5]", anniversary_month="//div[@id='content']/form/select[4]//option[6]", anniversary_year="1666"))


def test_modify_contact_second_address(app):
          app.contact.modify_first_contact(Contact(second_address="New second address"))


def test_modify_contact_land_line_2(app):
          app.contact.modify_first_contact(Contact(land_line_2="New land line 2"))


def test_modify_contact_notes(app):
          app.contact.modify_first_contact(Contact(notes="New notes"))

