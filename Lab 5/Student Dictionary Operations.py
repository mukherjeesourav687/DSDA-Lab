student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 21,
    'marital_status': 'Single',
    'skills': ['Python', 'C++'],
    'country': 'UK',
    'city': 'London',
    'address': '123 Baker Street'
}

# I. Get the length of the student dictionary
print(f"Length of student dictionary: {len(student)}")

# II. Get the value of skills and check data type
skills = student.get('skills')
print(f"Skills: {skills}, Type: {type(skills)}")

# III. Modify the skills values by adding skills
student['skills'].extend(['Java', 'SQL'])

# IV. Get the dictionary keys as a list
keys = list(student.keys())
print(f"Keys: {keys}")

# V. Get the dictionary values as a list
values = list(student.values())
print(f"Values: {values}")

# VI. Change the dictionary to a list of tuples
items = list(student.items())
print(f"Dictionary items: {items}")

# VII. Delete one of the items in the dictionary
del student['address']

# VIII. Delete the dictionary
del student
