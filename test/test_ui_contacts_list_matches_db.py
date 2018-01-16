from model.contact import Contact
from fixture.orm import ORMFixture
import re


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_homepage_contacts_info_assertion_with_db(app):
    ui_contacts = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    db_contacts = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for contact in ui_contacts:
        index = ui_contacts.index(contact)
        contact_from_home_page = ui_contacts[index]
        contact_from_db = db_contacts[index]
        assert clear(contact_from_home_page.first_name) == clear(contact_from_db.first_name)
        assert clear(contact_from_home_page.surname) == clear(contact_from_db.surname)
        assert clear(contact_from_home_page.address) == clear(contact_from_db.address)
        assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(
            contact_from_db)
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(
            contact_from_db)

def clear(s):
    return re.sub("[-() '\n']", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                                map(lambda x: clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.land_line, contact.mobile, contact.work, contact.land_line_2]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None, [contact.email_1, contact.email_2, contact.email_3])))


