from model.group import Group
import random
import re

def test_modify_group_name(app, db, check_ui):
        if len(db.get_group_list()) == 0:
                app.group.create(Group(name="test"))
        old_groups = db.get_group_list()
        group = random.choice(old_groups)
        group.name = "New group"
        index = old_groups.index(group)
        app.group.modify_group_by_id(group.id, group)
        assert len(old_groups) == app.group.count()
        new_groups = db.get_group_list()
        old_groups[index] = group
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        def clean(group):
                return Group(id=group.id, name=clear(group.name.strip()))
        new_groups = map(clean, db.get_group_list())
        if check_ui:
                assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

def clear(s):
        return re.sub("  ", " ", s)


#def test_modify_group_header(app):
#        if app.group.count() == 0:
#                app.group.create(Group(name="test"))
#        old_groups = app.group.get_group_list()
#        group = Group(header="New header")
#        group.id = old_groups[0].id
#        app.group.modify_first_group(group)
#        assert len(old_groups) == app.group.count()
#        new_groups = app.group.get_group_list()
#        old_groups[0] = group
#        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_group_footer(app):
#        if app.group.count() == 0:
#                app.group.create(Group(name="test"))
#        old_groups = app.group.get_group_list()
#        group = Group(footer="New footer")
#        group.id = old_groups[0].id
#        app.group.modify_first_group(group)
#        assert len(old_groups) == app.group.count()
#        new_groups = app.group.get_group_list()
#        old_groups[0] = group
#        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)