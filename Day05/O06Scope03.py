
def outerFun():
    gname = "Jordan"        # local variable

    def innerFun():
        nonlocal gname          # local variables can be coverted to                            nonlocal

        gname = "Micheal " + gname     # modify

        print("Hello World")
        print(f"Greetings {gname}")

    innerFun()
    print(f"After :{gname}")


outerFun()

