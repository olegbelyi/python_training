from sys import maxsize

class Contact:

    def __init__(self, first_name=None, middle_name=None, surname=None, id=None,
                 avatar=None, nickname=None, title=None, company_name=None, address=None,
                 land_line=None, mobile=None, work=None, land_line_2=None, all_phones_from_home_page=None, fax=None,
                 email_1=None, email_2=None, email_3=None, all_emails_from_home_page=None,
                 homepage=None, birthday_day=None, birthday_month=None, birthday_year=None,
                 anniversary_day=None, anniversary_month=None, anniversary_year=None, second_address=None, notes=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.surname = surname
        self.avatar = avatar
        self.nickname = nickname
        self.title = title
        self.company_name = company_name
        self.address = address
        self.land_line = land_line
        self.mobile = mobile
        self.work = work
        self.land_line_2 = land_line_2
        self.all_phones_from_home_page = all_phones_from_home_page
        self.fax = fax
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.all_emails_from_home_page = all_emails_from_home_page
        self.homepage = homepage
        self.birthday_day = birthday_day
        self.birthday_month = birthday_month
        self.birthday_year = birthday_year
        self.anniversary_day = anniversary_day
        self.anniversary_month = anniversary_month
        self.anniversary_year = anniversary_year
        self.second_address = second_address
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.first_name, self.surname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
               and self.first_name == other.first_name and self.surname == other.surname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize