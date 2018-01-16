# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import re


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_light(Contact(first_name="test_name"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    def clean(contact):
        return Contact(id=contact.id, first_name=clear(contact.first_name.strip()),
                       surname=clear(contact.surname.strip()))
    new_contacts = map(clean, db.get_contact_list())
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

def clear(s):
    return re.sub("  ", " ", s)