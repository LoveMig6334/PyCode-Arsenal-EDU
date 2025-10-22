while True:
    try:
        element = input("Enter a element: ")
        if isinstance(element, str) and element.replace(".", "", 1).isdigit():
            print("number is not supported, please enter a string")
    except ValueError:
        break

match element.strip():
    case "Fire":
        print("Fire: Strong against Earth")
    case "Water":
        print("Water: Strong against Fire")
    case "Earth":
        print("Earth: Strong against Air")
    case "Air":
        print("Air: Strong against Water")
    case _:
        print("Unknown element")
