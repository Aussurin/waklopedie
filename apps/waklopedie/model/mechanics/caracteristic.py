from mongoengine import *


class caracteristic (Document) :
        nom : StringField
        icon : ImageField