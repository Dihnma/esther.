"""
1. Take an input asking the user to enter score
2. Return A if the user's score is 70 and above
3. Return B if the user's score is between 60 and 69 (inclusive)
4. Return C if the user's score is between 50 and 59 (inclusive)
5. Return D if the user's score is between 40 and 49 (inclusive)
6. Return E if the user's score is between 30 and 39 (inclusive)
7. Return F if less than 30
"""


score = float(input("Enter your score: "))

                      
if score >= 70 and score <= 100:
    print("Grade: A")
elif score >= 60 and score < 70:
    print("grade B")
elif score >= 50 and score < 60:
    print("grade C")
elif score >= 40 and score < 50:
    print("grade D")
elif score >= 30 and score < 40:
    print("grade E")
elif score > 0 and score < 30:
    print("Grade F")    


else:
    print(f"invalid score {score}\nMust be btwn 0 and 100")