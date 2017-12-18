# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Contact(first_name=random_string("first_name", 15), surname=random_string("surname", 15))
    for i in range(5)
]
@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
        old_contacts = app.contact.get_contact_list()
        app.contact.create_light(contact)
        assert len(old_contacts) + 1 == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_add_contact(app):
 #       app.contact.create(Contact(first_name="Pavel", middle_name="Ivanovich", surname="Kolosov", avatar="C:\\Users\\slaterr\\Pictures\\avatar.jpg", nickname="Kolos",
  #                                 title="Mr", company_name="Cobelco", address="85, Queen street, Auckland, New Zealand", land_line="+642223334455",
   #                                mobile="+642223335556", work="+643334246622", fax="+644442221189", email_1="kolos@gmail.com", email_2="kolos@yahoo.com",
    #                               email_3="kolos@mail.ru", homepage="http://kolos.info", birthday_day="//div[@id='content']/form/select[1]//option[6]",
     #                              birthday_month="//div[@id='content']/form/select[2]//option[7]", birthday_year="1980",
      #                             anniversary_day="//div[@id='content']/form/select[3]//option[4]",
       #                            anniversary_month="//div[@id='content']/form/select[4]//option[2]", anniversary_year="1999",
        #                           second_address="30 Orakau Avenue, Epsom, Auckland, New Zealand ", land_line_2="+645556667788", notes="Skype ID: kolos1980"))
