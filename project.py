me = [
    'hannah',
    'murder for a jar of red rum',
    'mom',
    'seagull',
    'tomato',
    'no lemon, no melon',
    'some men interpret nine memos',
    'madam'
]
print(me)
for word in me:
    rev = word[::-1]
    if word == rev:
        print("yes, it's a palindrome")
    else:
        print("no, it's not a palindrome")