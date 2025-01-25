from mongoengine import *
from apps.waklopedie.model import *
from apps.waklopedie.model.mechanics import elem



class Ligne (Document) :
        ratio = FloatField
        qty = IntField
        effect = StringField(required=True) 
        stat = StringField
        elem = ReferenceField(elem.Elem)
    