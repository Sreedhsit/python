fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]


fruits.update(more_fruits)
fruits.add("banana2")
print(fruits)

if "banana" in fruits:
    print('Hurry')