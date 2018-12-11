from api.class_declaration import Profile, Storage, Base, Bag
# TODO: This S/L api uses txt files for the time being, should use databases in the future



# questions: what's in the save_file?
# save_file is a dictionary contains the following keys:
# profile, bag, base, and storage
# They are all "class", but bag and storage contains a list(need to keep the position of items)

# what's in the profile?
# name, level, gender, age, hunger, health, attack, armor

# what's in the base?
# name, level, storage

# what's in the bag?
# name, volume, items(list)

# what's in the storage?
# name, volume, items(list)

# save_file: the object that contains all the information
# filename: filename for save file

def save(save_file, filename):
	f = open(filename, "w") 
	for i in save_file.keys():
		#f.write(i)
		for j in save_file[i]:
			#if the class is profile
			if (i == "P"):
				f.write("Profile: ")
				f.write(j.name+" ")
				f.write("{} ".format(j.level))
				f.write("{} ".format(j.gender))
				f.write("{} ".format(j.age))
				f.write("{} ".format(j.hunger))
				f.write("{} ".format(j.health))
				f.write("{} ".format(j.attack))
				f.write("{} ".format(j.armor))
				f.write("\n")
			#if the class is base
			if (i == "Bs"):
				f.write("Base: ")
				f.write(j.name+" ")
				f.write("{} ".format(j.level))
				#if the class is storage
				f.write(j.storage.name + " ")	
				f.write("{} ".format(j.storage.volume))	
				f.write("{} ".format(j.storage.item))
				f.write("\n")
					
			#if the class is storage
			if (i == "S"):
				f.write("Storage: ")
				f.write(j.name+" ")
				f.write("{} ".format(j.volume))
				f.write("{} ".format(j.item))
				f.write("\n")

			#if the class is bag
			if (i == "Bg"):
				f.write("Bag: ")
				f.write(j.name+" ")
				f.write("{} ".format(j.volume))
				f.write("{} ".format(j.item))
				f.write("\n")



# save_file: the object that contains all the information
# filename: filename for save file

def load(save_file, filename):
	f = open(filename, "r")
	content = f.read().splitlines()
	for i in content:
		partial = i.split(" ")
		#print(partial)
		#if Profile
		if (partial[0] == "Profile:"):
			profile = Profile(partial[1], partial[2], partial[3], partial[4], partial[5], partial[6], partial[7], partial[8])
			save_file["P"].append(profile)

		#if Storage
		if (partial[0] == "Storage:"):
			storage = Storage(partial[1], partial[2], partial[3])
			save_file["S"].append(storage)

		#if Base
		if (partial[0] == "Base:"):
			storage = Storage(partial[3], partial[4], partial[5])
			base = Base(partial[1], partial[2], storage)
			save_file["Bs"].append(base)

		#if Bag
		if (partial[0] == "Bag:"):
			bag = Bag(partial[1], partial[2], partial[3])
			save_file["Bg"].append(bag)






# testing
profile = Profile("try_profile", 10, 1, 5, 0, 100, 10, 10)
storage = Storage("try_storage", 1, [])
base = Base("try_base", 10, storage)
bag = Bag("try_bag", 1, [])

save_file = {"P": [profile], "S": [storage], "Bs": [base], "Bg": [bag]}
load_file = {"P": [], "S": [], "Bs": [], "Bg": []}
#save(save_file, "try1.txt")
load(load_file, "try1.txt")
