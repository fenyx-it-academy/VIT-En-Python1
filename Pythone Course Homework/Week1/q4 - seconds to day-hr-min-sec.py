initial_seconds = int(input('Enter the number of seconds you want to convert: '))
days = initial_seconds // 86400
remainder = initial_seconds % 86400
hours = remainder // 3600
remainder = remainder % 3600
minutes = remainder // 60
remainder = remainder % 60
seconds = remainder
print(f"That is, {days} Days, {hours} Hours, {minutes} Minutes, {seconds} Seconds")
