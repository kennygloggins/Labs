text1 = input("Word:").lower()
text2 = input("String:").lower()

result = True

for i in range(len(text1)):
    if text1[i].count(text1) == text1[i].count(text2):
        continue
    else:
        result = False

print(result)