# -*- coding: utf-8 -*-
from model.group import Group
import re


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert old_groups == new_groups
    def clean(group):
        return Group(id=group.id, name=clear(group.name.strip()))
    new_groups = map(clean, db.get_group_list())
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

def clear(s):
    return re.sub("  ", " ", s)