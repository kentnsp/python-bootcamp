color_input = input("Enter traffic color: ")

match color_input:
    case "green" | "GREEN" | "Green":
        print("Go")
    case "yellow" | "YELLOW" | "Yellow":
        print("wait")
    case "red" | "RED" | "Red":
        print("stop")
    case _:
        print("Malfunction")

