import numpy as np

mi_casa = np.array([1, 21, 2, 4, 6, 87, 3])
su_casa = mi_casa


# same id in memory
print(id(mi_casa), " equal ", id(mi_casa))
print(mi_casa is su_casa)
print(mi_casa == su_casa)


# not same id in memory
tree_house = np.array([1, 21, 2, 4, 6, 87, 3])
print(mi_casa is tree_house)
print(mi_casa == tree_house)


# views : a shallow copy
farm_house = tree_house.view()
# farm_house.shape(2, 4)
print("farm house : ", farm_house)
print("tree house : ", tree_house)


# deep copies for manipulating the old array reference
dog_house = np.copy(tree_house)
dog_house[1] = -100
print(dog_house)

# views create different references from same ids
# copy creates different ids and also references
