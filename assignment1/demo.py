import  as st
import random

# Function to start the guessing game
def guessing_game():
    # Set up the session state to store the number to guess and attempts
    if 'number_to_guess' not in st.session_state:
        st.session_state.number_to_guess = random.randint(1, 100)
        st.session_state.attempts = 0

    # Display title and instructions
    st.title("Guess the Number Game!")
    st.write("I have selected a random number between 1 and 100. Try to guess it!")

    # User input for guess
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

    # Button to submit guess
    if st.button("Submit Guess"):
        if guess < st.session_state.number_to_guess:
            st.session_state.attempts += 1
            st.write("Too low! Try again.")
        elif guess > st.session_state.number_to_guess:
            st.session_state.attempts += 1
            st.write("Too high! Try again.")
        else:
            st.session_state.attempts += 1
            st.write(f"Congratulations! You guessed the number {st.session_state.number_to_guess} in {st.session_state.attempts} attempts.")
            st.session_state.number_to_guess = random.randint(1, 100)  # Reset the game with a new number
            st.session_state.attempts = 0  # Reset attempts for the new game

    # Display the number of attempts
    st.write(f"Attempts: {st.session_state.attempts}")

# Run the guessing game function
guessing_game()
