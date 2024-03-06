from django.test import TestCase

# Create your tests here.

# def variant(self):
#     s = ["m", "l", "xl", "xxl"]
#     c = ["red", "green", "blue", "black"]
#
# list_1 = [1, 2, 3, 4, 5, 6, 1]
# list_2 = ["a", "c", "d", "x", "q", "w"]
#
# list_1.remove(2)
# print(list_1)
# print(50 * "-")
# list_2.remove("a")
# print(list_2)
# print(list_1.count(1))
# print(50 * "-")
Dict_1 = {
    "name": "ahmed",
    "age": 29,
    "address": "sidebishr"
}
print(Dict_1.setdefault("gender", "male"))
print(Dict_1)