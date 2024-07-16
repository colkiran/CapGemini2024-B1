
class TooTiny(Exception):
    pass

class TooYoung(Exception):
    pass

class TooOld(Exception):
    pass


age = 105

try:
    if age < 6:
        raise TooTiny("The person is too very tiny to cast a vote")
    elif age < 18:
        raise TooYoung("The perspn is too young to cast a vote")
    elif age > 100:
        raise TooOld("The person is too very old to cast a vote")
    else:
        print("You can cast ypur valuable vote....")
except TooTiny as t:
    print("Exception Occured......")
    print(t)
except TooYoung as y:
    print("Exception Occured......")
    print(y)
except TooOld as o:
    print("Exception Occured......")
    print(o)
finally:
    print("Completed the task of voting......")