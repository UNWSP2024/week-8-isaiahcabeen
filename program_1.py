def initials_generator(personsName):
    personsInitials = ""
    name_parts = personsName.split()

    for name in name_parts:
        personsInitials += name[0].upper() + '. '

    return personsInitials.strip()

personsName = input('Enter the users first, middle, and last name: ')
initials = initials_generator(personsName)
print(initials)
