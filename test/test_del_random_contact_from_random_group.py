from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random
import time

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_del_contact_from_group(app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    groups = db.get_group_list()
    group = random.choice(groups)
    if len(db.get_contact_list()) == 0:
            app.contact.create_light(Contact(first_name="test_name"))
    if len(db.get_contacts_in_group(group)) == 0:
        contacts = db.get_contact_list()
        contact = random.choice(contacts)
        app.contact.add_contact_to_group(contact.id, group.id)
    contacts_in_group = db.get_contacts_in_group(group)
    contact_in_group = random.choice(contacts_in_group)
    old_group_contacts = db.get_contacts_in_group(group)
    app.contact.del_contact_from_group(contact_in_group.id, group.id)
    new_group_contacts = db.get_contacts_in_group(group)
    old_group_contacts.remove(contact_in_group)
    assert len(old_group_contacts) == len(new_group_contacts)
    assert sorted(new_group_contacts, key=Contact.id_or_max) == sorted(db.get_contacts_in_group(group),
                                                                       key=Contact.id_or_max)




