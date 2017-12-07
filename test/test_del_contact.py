# -*- coding: utf-8 -*-
from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_light(Contact(first_name="test_name"))
    app.contact.delete_first_contact()