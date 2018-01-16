from model.contact import Contact
from fixture.orm import ORMFixture
import random

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app):
    contacts = db.get_contact_list()
    groups = db.get_group_list()
    contact = random.choice(contacts)
    group = random.choice(groups)
    old_group_contacts = db.get_contacts_in_group(group)
    app.contact.add_contact_to_group(contact.id, group.id)
    new_group_contacts = db.get_contacts_in_group(group)
    assert len(old_group_contacts) + 1 == len(new_group_contacts)
    assert sorted(new_group_contacts, key=Contact.id_or_max) == sorted(db.get_contacts_in_group(group), key=Contact.id_or_max)