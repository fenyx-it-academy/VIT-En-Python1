first_name = input('Enter you first name: ')
last_name = input('Enter you last name: ')
box_length = len(first_name + ' ' + last_name) + 2
print('*' * box_length + '\n*' + first_name + ' ' + last_name + '*\n' + '*' * box_length)
