def get_operation():
    go = "go"
    while go == "go":
        opp= input("what operation do you want to do?(/,*,-,+)")
        if opp == "/" or opp == "*" or opp == "-" or opp == "+":
            return opp
            go = no
        else:
            print("invalid operation")