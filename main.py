import os

def display_menu(menu_options):
    print("----- Japanese Learning Tools -----")
    for idx, (tool_name, _) in enumerate(menu_options, start=1):
        print(f"{idx}. {tool_name}")
    print(f"{len(menu_options) + 1}. Exit")

def execute_tool(tool_path):
    if tool_path.lower() == 'exit':
        print("Exiting the program.")
        exit()
    else:
        os.system(f"python {tool_path}")

def load_menu_options(file_path):
    menu_options = []
    with open(file_path, 'r') as file:
        for line in file:
            name, path = map(str.strip, line.split(':'))
            menu_options.append((name, path))
    return menu_options

def main():
    script_dir = os.path.dirname(__file__)
    tools_file = os.path.join(script_dir, "lesson_list.txt")
    menu_options = load_menu_options(tools_file)

    while True:
        display_menu(menu_options)
        choice = input("Enter the number of the tool you want to use: ")

        try:
            tool_number = int(choice)
            if 1 <= tool_number <= len(menu_options) + 1:
                selected_tool = menu_options[tool_number - 1][1]
                execute_tool(selected_tool)
            else:
                print("Invalid choice. Please enter a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
