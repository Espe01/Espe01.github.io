import os
import menu

#givens
def run_bash_cmd(some_choice):
    print('-' * 80, '\n')
    print('You entered #', some_choice)
    if (some_choice == 1):
        print('The available memory is ')
        os.system('free -tmh')
    elif (some_choice == 2):
        print('The current network connections include: ')
        os.system('netstat -an | grep -i Estab | cut -d \':\' -f 2,3 | gawk \'{print $2}\' | grep [0-9] | uniq')
    elif (some_choice == 3):
        print('Available file space is: ')
        os.system('df -h | grep \'Filesystem\|root\'')


def main():
    #looping till user press q to quit
    while True:
        # menu options
        mainMenu = menu.Menu()
        mainMenu.addOption("Check available memory")
        mainMenu.addOption("View network connections")
        mainMenu.addOption("Display free RAM and swap")
        mainMenu.addOption("Quit")

        # collect input from menu
        choice = mainMenu.getInput()

        # set condition to print goodbye
        if choice == 4:
            print("Goodbye!")

        # set condition to break
        if choice == 'Q' or choice =='q':
            break
        # it passes user choice as a function
        run_bash_cmd(choice)





if __name__ == "__main__":
    main()

