from mongoengine import *


class Rarity (Document) :
        nom : StringField
        color : StringField