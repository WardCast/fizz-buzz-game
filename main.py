def is_correct(user_input, correct_answer):
    if user_input.lower() == correct_answer:
        return True
    elif str(correct_answer) == user_input:
        return True
    else:
        return False


def get_correct_answer(fizz_num, buzz_num, current_num):
    if current_num % fizz_num == 0 and current_num % buzz_num == 0:
        return "fizzbuzz"
    if current_num % fizz_num == 0:
        return "fizz"
    if current_num % buzz_num == 0:
        return "buzz"
    else:
        return current_num

# Setting preferences
fizz_num = input("\nEnter what you want fizz to be > ")
buzz_num = input("Enter what you want buzz to be >  ")
lives = input("Enter number the number of lives you want (Options: |1| |2| |3|) > ")

while lives not in "123":
    lives = input("Please enter a valid value: ")

# Rules
print(f"""\nIf the number is {fizz_num} or is a multiple of {fizz_num}, enter \"Fizz\"
If the number is {buzz_num} or is a multiple of {buzz_num}, enter \"Buzz\"
If the number is a multiple of both {fizz_num} and {buzz_num}, enter \"FizzBuzz\"
If the number is none of the above, enter the current number""")

current_lives = int(lives)
alive = True
current_num = 1
while alive:
    print("")
    print(current_num)
    user_answer = input("Enter your answer >  ")
    correct_answer = get_correct_answer(int(fizz_num), int(buzz_num), current_num)
    
    if is_correct(user_answer, correct_answer):
        current_num += 1
    else:
        current_lives -= 1
        print(f"\nLives left: {current_lives}/{lives}")
        if current_lives < 1:
            print("You lost - (insert unhelpfully sympathetic comment)\n")
            alive = False

