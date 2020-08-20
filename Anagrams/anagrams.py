text1 = input("Please enter the first word:").lower()
text2 = input("Please enter the second word:").lower()
lst1 = []
lst2 = []
for i in range(len(text1)):
    lst1.append(text1[i])
for i in range(len(text2)):
    lst2.append(text2[i])
lst1.sort()
lst2.sort()
if lst1 == lst2:
    print('Yes')
else:
    print('No')
