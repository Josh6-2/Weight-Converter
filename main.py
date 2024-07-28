while True:
    weight = int(input("Weight: "))
    weightconv = input("(K)g or (L)bs: ")

    if weightconv.upper() == "L":
        converted = weight * 0.45
        print("Weight in Kgs: " + str(converted))
    elif weightconv.upper() == "K":
        converted = weight / 0.45
        print("Weight in Lbs: " + str(converted))
    else:
        print("There has been an error in the code. Please enter K for Kgs or L for Lbs.")