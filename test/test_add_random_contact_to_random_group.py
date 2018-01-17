from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, db_ORM):
    if len(db_ORM.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(db_ORM.get_contact_list()) == 0:
        app.contact.create_light(Contact(first_name="test_name"))
    contacts = db_ORM.get_contact_list()
    groups = db_ORM.get_group_list()
    contact = random.choice(contacts)
    group = random.choice(groups)
    old_group_contacts = db_ORM.get_contacts_in_group(group)
    app.contact.add_contact_to_group(contact.id, group.id)
    new_group_contacts = db_ORM.get_contacts_in_group(group)
    assert len(old_group_contacts) + 1 == len(new_group_contacts)
    assert sorted(new_group_contacts, key=Contact.id_or_max) == sorted(db_ORM.get_contacts_in_group(group), key=Contact.id_or_max)