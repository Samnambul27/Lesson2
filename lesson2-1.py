my_list = [6, 'str', -78, False, (-1 + 5), 3.14, False,
           {1: 'names', 6: 'Ivan'}]
for i, item in enumerate(my_list, 1):
    print(f"{i}) {item} - {type(item)}")


