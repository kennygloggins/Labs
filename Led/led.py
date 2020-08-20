led = {
    1: [[" # "], [" # "], [" # "], [" # "], [" # "]],
    2: [["###"], ["  #"], ["###"], ["#  "], ["###"]],
    3: [["###"], ["  #"], ["###"], ["  #"], ["###"]],
    4: [["# #"], ["# #"], ["###"], ["  #"], ["  #"]],
    5: [["###"], ["#  "], ["###"], ["  #"], ["###"]],
    6: [["###"], ["#  "], ["###"], ["# #"], ["###"]],
    7: [["###"], ["  #"], ["  #"], ["  #"], ["  #"]],
    8: [["###"], ["# #"], ["###"], ["# #"], ["###"]],
    9: [["###"], ["# #"], ["###"], ["  #"], ["  #"]],
    0: [["###"], ["# #"], ["# #"], ["# #"], ["###"]],
}


def askForNumber():
    row0, row1, row2, row3, row4 = "", "", "", "", ""
    numlst = []
    num = input("What number would you liked displayed?")
    for number in num:
        numlst.append(led[int(number)])
    for line in numlst:
        row0 += " " + "".join(line[0])
        row1 += " " + "".join(line[1])
        row2 += " " + "".join(line[2])
        row3 += " " + "".join(line[3])
        row4 += " " + "".join(line[4])

    print(row0)
    print(row1)
    print(row2)
    print(row3)
    print(row4)


askForNumber()
