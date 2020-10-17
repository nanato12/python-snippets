""" Merge dict """

dict1 = {1: "A"}
dict2 = {2: "B"}

print("dict1 = {}, dict2 = {}".format(dict1, dict2))
print("dict1 | dict2 => {}".format(dict1 | dict2), end="\n\n")

dict1 = {1: "A", 2: "B"}
dict2 = {2: "C"}

print("dict1 = {}, dict2 = {}".format(dict1, dict2))
print("dict1 | dict2 => {}".format(dict1 | dict2), end="\n\n")

set1 = {1, 2, 3}
set2 = {2, 3, 4}

print("set1 = {}, set2 = {}".format(set1, set2))
print("set1 | set2 => {}".format(set1 | set2), end="\n\n")

dict1 = {1: "A"}
print("dict1 = {}".format(dict1))
dict1 |= {2: "B"}
print("dict1 |= {2: 'B'}")
print("dict1 => {}".format(dict1), end="\n\n")

dict1 = {1: "A"}
print("dict1 = {}".format(dict1))
dict1 |= [(2, "B"), (3, "C")]
print("dict1 |= [(2, 'B'), (3, 'C')]")
print("dict1 => {}".format(dict1), end="\n\n")
