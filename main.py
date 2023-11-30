import os

def display_menu():
    print("----- Japanese Learning Tools -----")
    print("1. Character Mapper")
    print("2. Other Tool (To be implemented)")
    print("3. Exit")

def execute_tool(tool_number):
    if tool_number == 1:
        os.system("python mapper/mapper.py")
    elif tool_number == 2:
        # Add implementation for other tool
        print("Other tool is not implemented yet.")
    elif tool_number == 3:
        print("Exiting the program.")
        exit()
    else:
        print("Invalid choice. Please enter a valid option.")

def main():
    while True:
        display_menu()
        choice = input("Enter the number of the tool you want to use: ")

        try:
            tool_number = int(choice)
            execute_tool(tool_number)
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
