# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import re


def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_light(Contact(first_name="test_name"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact.first_name = "New first name"
    contact.surname="New surname"
    index = old_contacts.index(contact)
    app.contact.modify_contact_by_id(contact.id, contact)
    assert len(old_contacts) == len(db.get_contact_list())
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    def clean(contact):
        return Contact(id=contact.id, first_name=clear(contact.first_name.strip()),
                       surname=clear(contact.surname.strip()))
    new_contacts = map(clean, db.get_contact_list())
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

def clear(s):
        return re.sub("  ", " ", s)




#def test_modify_contact_middle_name(app):
#    if app.contact.count() == 0:
#        app.contact.create_light(Contact(first_name="test_name"))
#    app.contact.modify_first_contact(Contact(middle_name="New middle name"))


#def test_modify_contact_surname(app):
#    if app.contact.count() == 0:
#        app.contact.create_light(Contact(first_name="test_name"))
#   old_contacts = app.contact.get_contact_list()
#    contact = Contact(first_name="New first name")
#    contact.id = old_contacts[0].id
#    app.contact.modify_first_contact(contact)
#    assert len(old_contacts) == app.contact.count()
#    new_contacts = app.contact.get_contact_list()
#    old_contacts[0] = contact
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_contact_avatar(app):
#    if app.contact.count() == 0:
#        app.contact.create_light(Contact(first_name="test_name"))
#    app.contact.modify_first_contact_avatar(Contact(avatar="C:\\Users\\slaterr\\Pictures\\avatar_2.jpg"))


#def test_modify_contact_nickname(app):
#    if app.contact.count() == 0:
#        app.contact.create_light(Contact(first_name="test_name"))
#    app.contact.modify_first_contact(Contact(nickname="New nickname"))


#def test_modify_contact_title(app):
#    if app.contact.count() == 0:
#        app.contact.create_light(Contact(first_name="test_name"))
#    app.contact.modify_first_contact(Contact(title="Ms"))


#def test_modify_contact_company_name(app):
#    if app.contact.count() == 0:
#        app.contact.create_light(Contact(first_name="test_name"))
#    app.contact.modify_first_contact(Contact(company_name="New company name"))


#def test_modify_contact_address(app):
#    if app.contact.count() == 0:
#        app.contact.create_light(Contact(first_name="test_name"))
#    app.contact.modify_first_contact(Contact(address="New address"))


#def test_modify_contact_land_line(app):
#    if app.contact.count() == 0:
#        app.contact.create_light(Contact(first_name="test_name"))
#    app.contact.modify_first_contact(Contact(land_line="New land line"))


#def test_modify_contact_mobile(app):
#    if app.contact.count() == 0:
#        app.contact.create_light(Contact(first_name="test_name"))
#    app.contact.modify_first_contact(Contact(mobile="New mobile"))


#def test_modify_contact_work(app):
#    if app.contact.count() == 0:
#        app.contact.create_light(Contact(first_name="test_name"))
#         app.contact.modify_first_contact(Contact(work="New work phone"))


#def test_modify_contact_fax(app):
#    if app.contact.count() == 0:
#        app.contact.create_light(Contact(first_name="test_name"))
#    app.contact.modify_first_contact(Contact(fax="New fax"))


#def test_modify_contact_email_1(app):
#    if app.contact.count() == 0:
#        app.contact.create_light(Contact(first_name="test_name"))
#    app.contact.modify_first_contact(Contact(email_1="New email 1"))


#def test_modify_contact_email_2(app):
#    if app.contact.count() == 0:
#        app.contact.create_light(Contact(first_name="test_name"))
#    app.contact.modify_first_contact(Contact(email_2="New email 2"))


#def test_modify_contact_email_3(app):
#    if app.contact.count() == 0:
#        app.contact.create_light(Contact(first_name="test_name"))
#    app.contact.modify_first_contact(Contact(email_3="New email 3"))


#def test_modify_contact_homepage(app):
#    if app.contact.count() == 0:
#        app.contact.create_light(Contact(first_name="test_name"))
#    app.contact.modify_first_contact(Contact(homepage="http://newhome.page"))


#def test_modify_contact_birthday(app):
#    if app.contact.count() == 0:
#        app.contact.create_light(Contact(first_name="test_name"))
#    app.contact.modify_first_contact_birthday(Contact(birthday_day="//div[@id='content']/form/select[1]//option[7]", birthday_month="//div[@id='content']/form/select[2]//option[6]", birthday_year="1999"))


#def test_modify_contact_anniversary_date(app):
#    if app.contact.count() == 0:
#        app.contact.create_light(Contact(first_name="test_name"))
#    app.contact.modify_first_contact_anniversary_date(Contact(anniversary_day="//div[@id='content']/form/select[3]//option[5]", anniversary_month="//div[@id='content']/form/select[4]//option[6]", anniversary_year="1666"))


#def test_modify_contact_second_address(app):
#    if app.contact.count() == 0:
#        app.contact.create_light(Contact(first_name="test_name"))
#    app.contact.modify_first_contact(Contact(second_address="New second address"))


#def test_modify_contact_land_line_2(app):
#    if app.contact.count() == 0:
#        app.contact.create_light(Contact(first_name="test_name"))
#    app.contact.modify_first_contact(Contact(land_line_2="New land line 2"))


#def test_modify_contact_notes(app):
#    if app.contact.count() == 0:
#        app.contact.create_light(Contact(first_name="test_name"))
#    app.contact.modify_first_contact(Contact(notes="New notes"))

