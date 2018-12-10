# This file contains some class declarations

# Profile
class Profile(object):
    def __init__(self, name, level, gender, age, hunger, health, weapon, armor):
        self.name = name
        self.level = level
        self.gender = gender
        self.age = age
        self.hunger = hunger
        self.health = health
        self.weapon = weapon
        self.armor = armor

# Storage
class Storage(object):
    def __init__(self, name, volume = 0, item = []):
        self.name = name
        self.volume = volume
        self.item = item

# Base
# storage is a class
class Base(object):
    def __init__(self, name, level, storage):
        self.name = name
        self.level = level
        self.storage = storage

# Bag
class Bag(object):
    def __init__(self, name, volume = 0, item = []):
        self.name = name
        self.volume = volume
        self.item = item
        

