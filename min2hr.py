# using this to calculate for habit tracking
response = input("Would you like to calculate minutes (m) only or hours and minutes (hm) ")

if response == "m":
    minutes = int(input("How many minutes? "))
    decimalhours = minutes / 60
    print(decimalhours)
elif response == "hm":
    minutes = int(input("How many minutes? "))
    decimalhours = minutes / 60
    hours = int(input("How many hours? "))
    total = hours + decimalhours
    print(total)
