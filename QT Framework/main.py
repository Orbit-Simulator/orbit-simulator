import aws_sql_conn

line = '---------------'
app_name = "Orbit Simulator"
version = "version 0.0.1-alpha"


def top_screen():
    print(f'\n')
    print(app_name.center(21, "-"))
    print(version.center(21, "-"))
    print(f'\n')


def main_menu():
    print(f'Press [1] to Login\n')
    print(f'Press [2] to Register\n')
    print(f'Press [3] to visit the GitHub repo\n')
    print(f'Press [x] to exit the app\n')

    user_input = input("Make your choice:")
    if user_input == '1':
        pass
    elif user_input == '2':
        pass
    elif user_input == '3':
        pass
    else:
        main_menu()

top_screen()
main_menu()
