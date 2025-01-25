from mongoengine import *


class Aoe (Document) :
        nom : StringField
        img : ImageField
        illustration : ImageField