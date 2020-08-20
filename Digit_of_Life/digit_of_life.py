bday = input("What is your bday(yyyymmdd)?")

def digitOfLife(string, digit=0):
    for i in range(len(string)):
        digit += int(string[i])
    return digit

def test(result):
    if len(str(result)) > 1:
        test(digitOfLife(str(result)))
    else:
        print(result)

test(digitOfLife(bday))