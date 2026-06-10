name = input("Enter your name: ").strip().title()

match name:
    case "Harry":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
        
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
        
    case _:
        print("who goes you") 