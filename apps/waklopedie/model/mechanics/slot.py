from mongoengine import *


class Slot (Document) :
        nom : StringField
        icon : ImageField