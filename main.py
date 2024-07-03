from menu import display_menu, process_choice

def main():
    continue_program = True
    while continue_program:
        display_menu()
        choice = int(input("Enter your choice: "))
        process_choice(choice)
        
        user_response = input("Do you want to perform another calculation? (yes/no): ")
        if user_response.lower() != "yes":
            continue_program = False

    print("Thank you for using the Black-Scholes Option Pricing program!")

if __name__ == "__main__":
    main()
