from mongoengine import *
from apps.waklopedie.model.ligne import Ligne
from apps.waklopedie.model.mechanics import needTarget,castMode,aoe


class Spell(Document):
    name = StringField(required=True)
    ap = IntField
    mp = IntField
    wp = IntField
    range_min = IntField(required=True)
    range_max = IntField(required=True)
    los = BooleanField(required=True)
    need_target = ReferenceField(needTarget.NeedTarget)
    cast_mode = ReferenceField(castMode.CastMode)
    aoe = ReferenceField(aoe.Aoe)
    unlock = IntField
    lignes = ListField(ReferenceField(Ligne))
    img : ImageField