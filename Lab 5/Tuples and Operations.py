# Creating tuples
fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'potato', 'spinach')
animal_products = ('milk', 'eggs', 'cheese')

# I. Join the three tuples
food_stuff_tp = fruits + vegetables + animal_products
print(f"food_stuff_tp: {food_stuff_tp}")

# II. Convert tuple to list
food_stuff_lt = list(food_stuff_tp)
print(f"food_stuff_lt: {food_stuff_lt}")

# III. Slice out the middle item(s)
middle_index = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    middle_items = food_stuff_lt[middle_index-1:middle_index+1]
else:
    middle_items = food_stuff_lt[middle_index:middle_index+1]
print(f"Middle item(s): {middle_items}")

# IV. Slice out the first three and the last three items
print(f"First three items: {food_stuff_lt[:3]}")
print(f"Last three items: {food_stuff_lt[-3:]}")

# V. Delete the tuple completely
del food_stuff_tp
