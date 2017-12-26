# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create_light(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert old_contacts == new_contacts
    def clean(contact):
        return Contact(id=contact.id, first_name=contact.first_name.strip(), surname=contact.surname.strip())
    new_contacts = map(clean, db.get_contact_list())
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)




#def test_add_contact(app):
 #       app.contact.create(Contact(first_name="Pavel", middle_name="Ivanovich", surname="Kolosov", avatar="C:\\Users\\slaterr\\Pictures\\avatar.jpg", nickname="Kolos",
  #                                 title="Mr", company_name="Cobelco", address="85, Queen street, Auckland, New Zealand", land_line="+642223334455",
   #                                mobile="+642223335556", work="+643334246622", fax="+644442221189", email_1="kolos@gmail.com", email_2="kolos@yahoo.com",
    #                               email_3="kolos@mail.ru", homepage="http://kolos.info", birthday_day="//div[@id='content']/form/select[1]//option[6]",
     #                              birthday_month="//div[@id='content']/form/select[2]//option[7]", birthday_year="1980",
      #                             anniversary_day="//div[@id='content']/form/select[3]//option[4]",
       #                            anniversary_month="//div[@id='content']/form/select[4]//option[2]", anniversary_year="1999",
        #                           second_address="30 Orakau Avenue, Epsom, Auckland, New Zealand ", land_line_2="+645556667788", notes="Skype ID: kolos1980"))
