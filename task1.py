
names = [['Alice', 'Bob', 'Charlie'],
         ['David', 'Eve', 'Frank'],
         ['Grace', 'Heidi', 'Ivan'],
         ['judy',  'Ken', 'Laura']
]


get_name = input("Enter name:")
for Names in names:
    for name in Names:
        if get_name == name:
            names.pop([0][0])
            print("Alice remove")
            print(names)
            break
        else:
            new_name = input("Enter new name:")
            names.append(new_name)
            print("goods")
            print(names)
            break



