""" Postponed Evaluation of Annotations Becomes Default """

# int.bit_count()
num1 = 1
print("num1 = {}".format(num1))
print("num1.bit_count() => {}".format(num1.bit_count()))

num1 = 10
print("num1 = {}".format(num1))
print("num1.bit_count() => {}".format(num1.bit_count()))

num1 = 100
print("num1 = {}".format(num1))
print("num1.bit_count() => {}".format(num1.bit_count()))

from types import MappingProxyType

dict1 = dict()
mappingProxy = MappingProxyType(dict1)
print(type(dict1.items()) is type(mappingProxy.items()))
print(mappingProxy.items().mapping is dict1)

# zip(*iterables, strict=False)
list1 = list(zip(("a", "b", "c"), (1, 2, 3), strict=True))
print("list1 = list(zip(('a', 'b', 'c'), (1, 2, 3), strict=True))")
print("list1 => {}".format(list1))
