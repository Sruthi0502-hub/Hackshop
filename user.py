def binary_search_game(low, high):
    print("Welcome to the Guessing Game!")
    print(f"Think of a number between {low} and {high}, and I will try to guess it.")
    input("Press Enter when you're ready...")
    
    while low <= high:
        guess = (low + high) // 2  # Find the middle number
        print(f"My guess is: {guess}")
        
        feedback = input("Is this your number? (yes/higher/lower): ").strip().lower()
        
        if feedback == "yes":
            print(f"Hooray! I guessed your number: {guess}")
            break
        elif feedback == "higher":
            low = guess + 1  # The number is higher, so adjust the lower bound
        elif feedback == "lower":
            high = guess - 1  # The number is lower, so adjust the upper bound
        else:
            print("Invalid input! Please respond with 'yes', 'higher', or 'lower'.")
    
    print("Thanks for playing!")

# Start the game with a range from 1 to 100
binary_search_game(1, 100)
