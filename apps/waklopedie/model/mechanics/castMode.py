from mongoengine import *


class CastMode (Document) :
        nom : StringField
        img : ImageField
        illustration : ImageField