from peewee import Model, CharField


class BaseModel(Model):
    class Meta:
        database = database


# the user model specifies its fields (or columns) declaratively, like django
class Item(BaseModel):
    name = CharField(unique=True)
    type = CharField()
    abilities = CharField()
    properties = CharField()
    level = CharField()
    remort = CharField()
    value = CharField()
    weight = CharField()
    armor = CharField()
    effects = CharField()
    prevents = CharField()
