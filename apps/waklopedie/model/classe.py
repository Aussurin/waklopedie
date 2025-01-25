from mongoengine import *
from apps.waklopedie.model.spell import Spell


class Classe(Document):
    name = StringField(required=True)
    img = ImageField
    spellbook = ListField(ReferenceField(Spell))
    
def get_class(classname: StringField):
    return Classe.objects(name=classname)