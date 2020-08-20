text = input("Check if it's a palidrome:").lower()
text = text.replace(' ', '')
def palidromeCheck(text):
    for i in range(len(text)):
        if text[i] != text[-(i+1)]:
            return False
    return True

result = palidromeCheck(text)
if not result:
    print('Nope')
else:
    print('Yes')
