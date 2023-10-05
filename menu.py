#class Menu
class Menu:
    # givens
    def __init__(self):
        self._options = [] # givens

    # given
    def addOption(self, option):
        self._options.append(option) # givens

    def getInput(self):
        while True:
            #concidion to print 1 2 3 4 for the menu options
            for i, option in enumerate(self._options, start=1):
                print(i, option)

            choice = input("Pick a Menu Option from 1-4: ")

            #condition isdigit checking for a string
            if choice.isdigit():
                choice = int(choice)

                #setting a range
                if 1 <= choice <= 4:
                    return choice
            # returnining for either lowers case and upper case
            elif choice == 'q' or choice == 'Q':
                return 'q'

            # when the user enter a wrong input
            print("Invalid input. Please enter a valid option (1-4).")



