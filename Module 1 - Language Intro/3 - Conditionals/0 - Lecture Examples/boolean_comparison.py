random = generate_random_number(0,100)

for p in range(0, 10):
    if random < 50:
        print("The number is less than 50")
    elif random == 50:
        print("The number is equal to 50")
    else:
        print("The number is greater than 50")
