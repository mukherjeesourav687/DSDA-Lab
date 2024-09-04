person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# I. Check if person has skills key and print the middle skill
if 'skills' in person:
    middle_index = len(person['skills']) // 2
    print(f"Middle skill: {person['skills'][middle_index]}")

# II. Check if person has 'Python' skill
has_python = 'Python' in person['skills']
print(f"Has Python skill: {has_python}")

# III. Check person's skills and determine
