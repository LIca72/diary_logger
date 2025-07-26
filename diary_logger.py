try:
    thought = input("Enter your thought: ")

    with open("diary.txt", "a") as file:
        file.write(thought + "\n")
        print("Your thought has been saved to diary.txt")

except Exception as e:
    print("Something went wrong while saving your thought:", e)

finally:
    print("Program finished.")
