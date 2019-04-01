blue_eyes = {'Olivia', 'Harry', 'Lily', 'Jack', 'Amelia'}
blond_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua'}
smell_hcn = {'Harry', 'Amelia'}
taste_ptc = {'Harry', 'Amelia', 'Lily', 'Lola'}
o_blood = {'Lily', 'Joshua', 'Mia', 'Olivia'}
b_blood = {'Amelia', 'Jack'}
a_blood = {'Harry'}
ab_blood = {'Joshua', 'Lola'}

# To find people with blue eyes or blond hair or both
a = blue_eyes.union(blond_hair)

# blue eyes and blond hair
b = blue_eyes.intersection(blond_hair)

# To identify people who have blond hair but not blue eyes
c = blond_hair.difference(blue_eyes)

# To identify people who have blue eyes but not blond hair
d = blue_eyes.difference(blond_hair)

# To find people who have blond hair or blue eyes but not both
e = blond_hair.symmetric_difference(blue_eyes)

f = smell_hcn.issubset(blond_hair)
g = taste_ptc.issuperset(smell_hcn)

h = o_blood.isdisjoint(a_blood)
if __name__ == '__main__':
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f, g, h)
