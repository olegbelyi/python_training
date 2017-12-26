# -*- coding: utf-8 -*-
from model.group import Group
import random
import re


def test_delete_some_group(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    def clean(group):
        return Group(id=group.id, name=clear(group.name.strip()))
    new_groups = map(clean, db.get_group_list())
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

def clear(s):
    return re.sub("  ", " ", s)