""" String object removeprefix removesuffix """

text = "issue-1234"
print("text = {}".format(text))
print("text.removeprefix('issue-') => {}".format(text.removeprefix("issue-")))
print("text.removeprefix('iss') => {}".format(text.removeprefix("iss")))
print("text.removeprefix('iss-') => {}".format(text.removeprefix("iss-")))
print()
print("text.removesuffix('1234') => {}".format(text.removesuffix("1234")))
print("text.removesuffix('1234') => {}".format(text.removesuffix("-1234")))
print("text.removesuffix('1234') => {}".format(text.removesuffix("iss-1234")))
