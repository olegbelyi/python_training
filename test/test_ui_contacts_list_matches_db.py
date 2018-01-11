from model.contact import Contact
from fixture.orm import ORMFixture


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_homepage_contacts_info_assertion_with_db(app):
    ui_contacts = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    db_contacts = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for contact in ui_contacts:
        index = ui_contacts.index(contact)
        contact_from_home_page = ui_contacts[index]
        contact_from_db = db_contacts[index]
        #print(contact_from_home_page)
        #print('DB' + str(contact_from_db))
        assert contact_from_home_page.first_name == contact_from_db.first_name
        assert contact_from_home_page.surname == contact_from_db.surname


