it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# I. Find the length of the set it_companies
print(f"Length of it_companies: {len(it_companies)}")

# II. Add 'Twitter' to it_companies
it_companies.add('Twitter')

# III. Insert multiple IT companies at once
it_companies.update(['TCS', 'Infosys'])
print(f"it_companies after adding: {it_companies}")

# IV. Remove one company from the set
it_companies.remove('Facebook')

# V. Difference between remove and discard
# remove() raises an error if the element is not found, while discard() does not.

# 4. Set Operations with A and B
# I. Join A and B
union_set = A.union(B)
print(f"A union B: {union_set}")

# II. Find A intersection B
intersection_set = A.intersection(B)
print(f"A intersection B: {intersection_set}")

# III. Is A subset of B
is_subset = A.issubset(B)
print(f"Is A subset of B: {is_subset}")

# IV. Are A and B disjoint sets
are_disjoint = A.isdisjoint(B)
print(f"Are A and B disjoint: {are_disjoint}")

# V. Join A with B and B with A
A.update(B)
print(f"A after joining B: {A}")
B.update(A)
print(f"B after joining A: {B}")

# VI. Symmetric difference between A and B
sym_diff = A.symmetric_difference(B)
print(f"Symmetric difference between A and B: {sym_diff}")

# VII. Delete sets
del A, B
