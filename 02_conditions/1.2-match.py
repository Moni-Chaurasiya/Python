day=4
match day:
    case 6 | 4:
        print("Saturday or Thursday")
    case 7:
        print("Sunday")
    case _:
        print("Not matched")