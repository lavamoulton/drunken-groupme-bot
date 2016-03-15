import groupy

groups = groupy.Group.list()
members = groupy.Member.list()
bots = groupy.Bot.list()

for group in groups:
    pass
    # if group.id == "number_here"
        # do something with it

# groupy.Bot.create("name_here", group)