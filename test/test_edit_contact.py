# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.edit(Contact(first_name="Anton", middle_name="Antonovich", surname="Antonov", avatar="C:\\Users\\slaterr\\Pictures\\avatar_2.jpg", nickname="Anton",
                                   title="Mr", company_name="WF", address="666, Devil street, Auckland, New Zealand", land_line="+666666666666",
                                   mobile="+666666666666", work="+66666666666", fax="+666666666666", email_1="666@gmail.com", email_2="666@yahoo.com",
                                   email_3="666@mail.ru", homepage="http://666.info", birthday_day="//div[@id='content']/form/select[1]//option[7]",
                                   birthday_month="//div[@id='content']/form/select[2]//option[6]", birthday_year="1999",
                                   anniversary_day="//div[@id='content']/form/select[3]//option[5]",
                                   anniversary_month="//div[@id='content']/form/select[4]//option[3]", anniversary_year="1666",
                                   second_address="666, Demon Avenue, Auckland, New Zealand ", land_line_2="+666666666666", notes="Skype ID: 666"))
        app.session.logout()