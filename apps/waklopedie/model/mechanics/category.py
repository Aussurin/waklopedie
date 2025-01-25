from mongoengine import *


class Category (Document) :
        nom : StringField
        icon : ImageField