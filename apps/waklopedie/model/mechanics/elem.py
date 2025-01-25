from mongoengine import *


class Elem (Document) :
        nom : StringField
        icon_m : ImageField
        icon_r : ImageField