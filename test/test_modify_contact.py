# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_first_name(app):
        app.session.login(username="admin", password="secret")
        app.contact.modify_first_contact(Contact(first_name="New first name"))
        app.session.logout()


def test_modify_contact_middle_name(app):
         app.session.login(username="admin", password="secret")
         app.contact.modify_first_contact(Contact(middle_name="New middle name"))
         app.session.logout()


def test_modify_contact_surname(app):
         app.session.login(username="admin", password="secret")
         app.contact.modify_first_contact(Contact(surname="New surname"))
         app.session.logout()


def test_modify_contact_avatar(app):
         app.session.login(username="admin", password="secret")
         app.contact.modify_first_contact(Contact(avatar="C:\\Users\\slaterr\\Pictures\\avatar_2.jpg"))
         app.session.logout()


def test_modify_contact_nickname(app):
         app.session.login(username="admin", password="secret")
         app.contact.modify_first_contact(Contact(nickname="New nickname"))
         app.session.logout()


def test_modify_contact_title(app):
         app.session.login(username="admin", password="secret")
         app.contact.modify_first_contact(Contact(title="Ms"))
         app.session.logout()


def test_modify_contact_company_name(app):
         app.session.login(username="admin", password="secret")
         app.contact.modify_first_contact(Contact(company_name="New company name"))
         app.session.logout()


def test_modify_contact_address(app):
         app.session.login(username="admin", password="secret")
         app.contact.modify_first_contact(Contact(address="New address"))
         app.session.logout()


def test_modify_contact_land_line(app):
         app.session.login(username="admin", password="secret")
         app.contact.modify_first_contact(Contact(land_line="New land line"))
         app.session.logout()

def test_modify_contact_mobile(app):
         app.session.login(username="admin", password="secret")
         app.contact.modify_first_contact(Contact(mobile="New mobile"))
         app.session.logout()


def test_modify_contact_work(app):
         app.session.login(username="admin", password="secret")
         app.contact.modify_first_contact(Contact(work="New work phone"))
         app.session.logout()


def test_modify_contact_fax(app):
         app.session.login(username="admin", password="secret")
         app.contact.modify_first_contact(Contact(fax="New fax"))
         app.session.logout()


def test_modify_contact_email_1(app):
        app.session.login(username="admin", password="secret")
        app.contact.modify_first_contact(Contact(email_1="New email 1"))
        app.session.logout()


def test_modify_contact_email_2(app):
        app.session.login(username="admin", password="secret")
        app.contact.modify_first_contact(Contact(email_2="New email 2"))
        app.session.logout()


def test_modify_contact_email_3(app):
        app.session.login(username="admin", password="secret")
        app.contact.modify_first_contact(Contact(email_3="New email 3"))
        app.session.logout()


def test_modify_contact_homepage(app):
         app.session.login(username="admin", password="secret")
         app.contact.modify_first_contact(Contact(homepage="http://newhome.page"))
         app.session.logout()


def test_modify_contact_birthday_day(app):
          app.session.login(username="admin", password="secret")
          app.contact.modify_first_contact(Contact(birthday_day="//div[@id='content']/form/select[1]//option[7]"))
          app.session.logout()


def test_modify_contact_birthday_month(app):
          app.session.login(username="admin", password="secret")
          app.contact.modify_first_contact(Contact(birthday_month="//div[@id='content']/form/select[2]//option[6]"))
          app.session.logout()


def test_modify_contact_birthday_year(app):
          app.session.login(username="admin", password="secret")
          app.contact.modify_first_contact(Contact(birthday_year="1999"))
          app.session.logout()


def test_modify_contact_anniversary_day(app):
          app.session.login(username="admin", password="secret")
          app.contact.modify_first_contact(Contact(anniversary_day="//div[@id='content']/form/select[3]//option[5]"))
          app.session.logout()


def test_modify_contact_anniversary_month(app):
          app.session.login(username="admin", password="secret")
          app.contact.modify_first_contact(Contact(anniversary_month="//div[@id='content']/form/select[4]//option[3]"))
          app.session.logout()


def test_modify_contact_anniversary_year(app):
          app.session.login(username="admin", password="secret")
          app.contact.modify_first_contact(Contact(anniversary_year="1666"))
          app.session.logout()


def test_modify_contact_second_address(app):
          app.session.login(username="admin", password="secret")
          app.contact.modify_first_contact(Contact(second_address="New second address"))
          app.session.logout()


def test_modify_contact_land_line_2(app):
          app.session.login(username="admin", password="secret")
          app.contact.modify_first_contact(Contact(land_line_2="New land line 2"))
          app.session.logout()


def test_modify_contact_notes(app):
          app.session.login(username="admin", password="secret")
          app.contact.modify_first_contact(Contact(notes="New notes"))
          app.session.logout()
