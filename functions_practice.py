print("-------------------")
# • A function named hello() that prints a greeting to the user.
# This function should accept no arguments and returns nothing.
def hello():
  print("Hi there!")

hello()

print("-------------------")
#A function named pack() that accepts three arguments, and
# returns a single list with the three arguments inside as list elements.
def pack(small, tall, big):
  newList = [small, tall, big]
  return newList

packed_list = pack("apple", "banana", "cherry")
print(packed_list)

print("-------------------")
# A function called eat_lunch().
# This function should accept a list of any length, and
# print out a series of strings that say =>
# "First I eat __" (the first element of the list), and "Next I eat ___"
# (for the following elements in the list). If the list is empty, print
# "My lunchbox is empty!". The function should not return anything.
def eat_lunch(lunch_list):
    # Check if the list is empty
    if len(lunch_list) == 0:
        print("My lunchbox is empty!")
    else:
        # Print the first item
        print(f"First I eat {lunch_list[0]}")
        # Print the rest of the items
        for item in lunch_list[1:]:
            print(f"Next I eat {item}")

eat_lunch(["sandwich", "apple", "cookie"])

eat_lunch([])
