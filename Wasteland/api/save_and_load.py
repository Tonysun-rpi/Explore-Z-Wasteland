# TODO: This S/L api uses txt files for the time being, should use databases in the future

# questions: what's in the save_file?
# save_file is a dictionary contains the following keys:
# profile, bag, base, and storage
# They are all "class", but bag and storage contains a list(need to keep the position of items)

# what's in the profile?
# name, level, gender, age, hunger, health, weapon, armor

# what's in the base?
# name, level, storage

# what's in the bag?
# name, volume, items(list)

# what's in the storage?
# name, volume, items(list)


# save_file: the object that contains all the information
# filename: filename for save file
def save(save_file, filename):
    #f = open(save_file, "w") 
    #f.write(save_file)
	pass


# save_file: the object that contains all the information
# filename: filename for save file
def load(save_file, filename):
	pass
