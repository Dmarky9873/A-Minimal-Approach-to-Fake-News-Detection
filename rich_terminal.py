"""
    Author: Daniel Markusson

    Assets:
    *    Rich_Terminal (Class):
        -   Constants:
                PAGE_BREAK (`str`): 50 '-' characters in a row with two newlines surrounding it.
                
        -   Methods:
            #   print_ALERT --> None
                    Summary:
                        Prints `s` with the `ALERT` color in the __Colors class.
                    Args:
                        s (`str`): A string to be printed with the `ALERT` color.
                        
            #   print_WARN --> None
                    Summary:
                        Prints `s` with the `MINIMAL` color in the __Colors class.
                    Args:
                        s (`str`): A string to be printed with the `MINIMAL` color.
"""


class Rich_Terminal:
    PAGE_BREAK = "\n\n"

    def __init__(self):
        for i in range(50):
            self.PAGE_BREAK += '-'
        self.PAGE_BREAK += '\n\n'

    def __toString(self, s):
        if type(s) != str:
            s = str(s)
        return s

    # The following functions automatically print the string 's' in the wanted color.
    def print_ALERT(self, s):
        """Prints `s` with the `ALERT` color in the __Colors class.

        Args:
            s (`str`): A string to be printed with the `ALERT` color.
        """
        s = self.__toString(s)
        print(self.__Colors.RED + s + self.__Colors.RESET)

    def print_MINIMAL(self, s):
        """Prints `s` with the `MINIMAL` color in the __Colors class.

        Args:
            s (`str`): A string to be printed with the `MINIMAL` color.
        """

        s = self.__toString(s)
        print(self.__Colors.MINIMAL + s + self.__Colors.RESET)

    def print_WARN(self, s):
        s = self.__toString(s)
        print(self.__Colors.YELLOW + s + self.__Colors.RESET)

    def print_SUCCESS(self, s):
        s = self.__toString(s)
        print(self.__Colors.GREEN + s + self.__Colors.RESET)

    def print_INFO(self, s):
        s = self.__toString(s)
        print(self.__Colors.BLUE + s + self.__Colors.RESET)

    def print_MAJOR(self, s):
        s = self.__toString(s)
        print(self.__Colors.MAJOR + s + self.__Colors.RESET)

    # The following functions return the string 's' in the wanted color (to print along side
    # different colors within the same line).
    def getString_ALERT(self, s):
        s = self.__toString(s)
        return self.__Colors.RED + s + self.__Colors.RESET

    def getString_MINIMAL(self, s):
        s = self.__toString(s)
        return self.__Colors.MINIMAL + s + self.__Colors.RESET

    def getString_WARN(self, s):
        s = self.__toString(s)
        return self.__Colors.YELLOW + s + self.__Colors.RESET

    def getString_SUCCESS(self, s):
        s = self.__toString(s)
        return self.__Colors.GREEN + s + self.__Colors.RESET

    def getString_INFO(self, s):
        s = self.__toString(s)
        return self.__Colors.BLUE + s + self.__Colors.RESET

    def getString_MAJOR(self, s):
        s = self.__toString(s)
        return self.__Colors.MAJOR + s + self.__Colors.RESET

    class __Colors:
        RED = '\033[91m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        BLUE = '\033[94m'
        MAJOR = '\033[97m'
        RESET = '\033[0m'
        MINIMAL = "\033[38;5;242m"


if __name__ == '__main__':
    rt = Rich_Terminal()

    print("This is regular text\n")
    rt.print_MINIMAL("This is minimal text")
    rt.print_ALERT("This is alert text")
    rt.print_WARN("This is warn text")
    rt.print_SUCCESS("This is success text")
    rt.print_INFO("This is info text")
    rt.print_MAJOR("This is major text")

    print('\nu' + rt.getString_MINIMAL('k') + rt.getString_ALERT('u') + rt.getString_WARN('l') +
          rt.getString_SUCCESS('e') + rt.getString_INFO('l') + rt.getString_MAJOR('e'))
