# Use list data type to store the questions and their correct answers
# discuss the final amount the person is taking home after playing the game
questions = ["Who is known as the \"Iron Man of India\"?",
             "What is the national animal of India?",
             "Which country is known as the \"Land of the Rising Sun\"?",
             "Who painted the famous artwork \"Mona Lisa\"?",
             "Which planet is the largest in our solar system?"
             ]
options = [
    ["a. Mahatma Gandhi", "b. Subhash Chandra Bose", "c. Sardar Vallabhbhai Patel", "d. Jawaharlal Nehru"],
    ["a. Lion", "b. Tiger", "c. Elephant", "d. Peacock"],
    ["a. China", "b. Japan", "c. South Korea", "d. Vietnam"],
    ["a. Leonardo da Vinci", "b. Vincent van Gogh", "c. Pablo Picasso", "d. Michelangelo"],
    ["a. Mercury","b. Venus","c. Jupiter", "d. Saturn"]
]

answers = [2, 1, 1, 0, 2]

price_amount = [5000, 10000, 15000, 20000, 25000]

total_questions = len(questions)
current_question = 0
current_prize = 0

print("Welcome to Koun Banega Crorepati")

while current_question < total_questions:
    print("\nQuestion", current_question + 1, ":", questions[current_question])
    for option in options[current_question]:
        print(option)
    answer = input("Enter the answer(a, b, c, d): ")
    match answer:
        case "a":
            selected_answer = 0
        case "b":
            selected_answer = 1
        case "c":
            selected_answer = 2
        case "d":
            selected_answer = 3
        case _:
            print("Invalid Option")
            continue
    if selected_answer == answers[current_question]:
        current_prize += price_amount[current_question]
        print("Correct Answer!")
        print(f"Congratulations!, You won Rs.{current_prize}")
        current_question += 1
    else:
        print("Wrong answer!, Better luck next time")
        print("Game over! You won Rs.", current_prize)
        break









