# -*- coding: utf-8 -*-
import pytest

from fixture.entry import Entry
from model.contact import Contact


@pytest.fixture
def ent(request):
    fixture = Entry()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(ent):
        ent.login(username="admin", password="secret")
        ent.create_contact(Contact(first_name="Pavel", middle_name="Ivanovich", surname="Kolosov", avatar="C:\\Users\\slaterr\\Pictures\\avatar.jpg", nickname="Kolos",
                            title="Mr", company_name="Cobelco", address="85, Queen street, Auckland, New Zealand", land_line="+642223334455",
                            mobile="+642223335556", work="+643334246622", fax="+644442221189", email_1="kolos@gmail.com", email_2="kolos@yahoo.com",
                            email_3="kolos@mail.ru", homepage="http://kolos.info", birthday_day="//div[@id='content']/form/select[1]//option[6]",
                            birthday_month="//div[@id='content']/form/select[2]//option[7]", birthday_year="1980",
                            anniversary_day="//div[@id='content']/form/select[3]//option[4]",
                            anniversary_month="//div[@id='content']/form/select[4]//option[2]", anniversary_year="1999",
                            second_address="30 Orakau Avenue, Epsom, Auckland, New Zealand ", land_line_2="+645556667788", notes="Skype ID: kolos1980"))
        ent.logout()

