from mongoengine import *


class Family (Document) :
        nom : StringField
        lvl_cap : int
        icon : ImageField