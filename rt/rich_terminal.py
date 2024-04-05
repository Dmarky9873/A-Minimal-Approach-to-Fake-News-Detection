"""
    Author: Daniel Markusson

    Assets:
    *    Rich_Terminal (Class):
        -   Constants:
                PAGE_BREAK (`str`): 50 '-' characters in a row with two newlines surrounding it.
                
        -   Methods:
            #   print_ALERT --> None
                    Summary:
                        Prints `s` with the `ALERT` color in the __colors class.
                    Args:
                        s (`str`): A string to be printed with the `ALERT` color.
                        
            #   print_WARN --> None
                    Summary:
                        Prints `s` with the `MINIMAL` color in the __colors class.
                    Args:
                        s (`str`): A string to be printed with the `MINIMAL` color.
"""


class RichTerminal:
    """Class to house all of the Rich_Terminal functions.
    """
    page_break = "\n\n"

    __colors = {
        "RED": '\033[91m',
        "GREEN":  '\033[92m',
        "YELLOW": '\033[93m',
        "BLUE": '\033[94m',
        "MAJOR": '\033[97m',
        "RESET": '\033[0m',
        "MINIMAL": "\033[38;5;242m"
    }

    def __init__(self):
        for _ in range(50):
            self.page_break += '-'
        self.page_break += '\n\n'

    def __to_string(self, s):
        if isinstance(s, str):
            s = str(s)
        return s

    # The following functions automatically print the string 's' in the wanted color.
    def print_alert(self, s):
        """Prints `s` with the `ALERT` color in the __colors class.

        Args:
            s (`str`): A string to be printed with the `ALERT` color.
        """
        s = self.__to_string(s)
        print(self.__colors["RED"] + s + self.__colors["RESET"])

    def print_minimal(self, s):
        """Prints `s` with the `MINIMAL` color in the __colors class.

        Args:
            s (`str`): A string to be printed with the `MINIMAL` color.
        """

        s = self.__to_string(s)
        print(self.__colors["MINIMAL"] + s + self.__colors["RESET"])

    def print_warn(self, s):
        """Prints `s` with the `WARN` color in the __colors class.

        Args:
            s (`str`): A string to be printed with the `MINIMAL` color.
        """
        s = self.__to_string(s)
        print(self.__colors["YELLOW"] + s + self.__colors["RESET"])

    def print_success(self, s):
        """Prints `s` with the `SUCCESS` color in the __colors class.

        Args:
            s (`str`): A string to be printed with the `MINIMAL` color.
        """
        s = self.__to_string(s)
        print(self.__colors["GREEN"] + s + self.__colors["RESET"])

    def print_info(self, s):
        """Prints `s` with the `INFO` color in the __colors class.

        Args:
            s (`str`): A string to be printed with the `MINIMAL` color.
        """
        s = self.__to_string(s)
        print(self.__colors["BLUE"] + s + self.__colors["RESET"])

    def print_major(self, s):
        """Prints `s` with the `MAJOR` color in the __colors class.

        Args:
            s (`str`): A string to be printed with the `MINIMAL` color.
        """
        s = self.__to_string(s)
        print(self.__colors["MAJOR"] + s + self.__colors["RESET"])

    # The following functions return the string 's' in the wanted color (to print along side
    # different colors["within"] the same line).
    def get_string_alert(self, s):
        """Returns a string `s` with the `ALERT` color in the __colors class.

        Args:
            s (`str`): A string to be printed with the `MINIMAL` color.
        """
        s = self.__to_string(s)
        return self.__colors["RED"] + s + self.__colors["RESET"]

    def get_string_minimal(self, s):
        """Returns a string `s` with the `MINIMAL` color in the __colors class.

        Args:
            s (`str`): A string to be printed with the `MINIMAL` color.
        """
        s = self.__to_string(s)
        return self.__colors["MINIMAL"] + s + self.__colors["RESET"]

    def get_string_warn(self, s):
        """Returns a string `s` with the `WARN` color in the __colors class.

        Args:
            s (`str`): A string to be printed with the `MINIMAL` color.
        """
        s = self.__to_string(s)
        return self.__colors["YELLOW"] + s + self.__colors["RESET"]

    def get_string_success(self, s):
        """Returns a string `s` with the `SUCCESS` color in the __colors class.

        Args:
            s (`str`): A string to be printed with the `MINIMAL` color.
        """
        s = self.__to_string(s)
        return self.__colors["GREEN"] + s + self.__colors["RESET"]

    def get_string_info(self, s):
        """Returns a string `s` with the `MINIMAL` color in the __colors class.

        Args:
            s (`str`): A string to be printed with the `MINIMAL` color.
        """
        s = self.__to_string(s)
        return self.__colors["BLUE"] + s + self.__colors["RESET"]

    def get_string_major(self, s):
        """Returns a string `s` with the `MINIMAL` color in the __colors class.

        Args:
            s (`str`): A string to be printed with the `MINIMAL` color.
        """
        s = self.__to_string(s)
        return self.__colors["MAJOR"] + s + self.__colors["RESET"]


def main():
    """Main function to be ran when the file is ran.
    """
    rt = RichTerminal()

    print("This is regular text\n")
    rt.print_minimal("This is minimal text")
    rt.print_alert("This is alert text")
    rt.print_warn("This is warn text")
    rt.print_success("This is success text")
    rt.print_info("This is info text")
    rt.print_major("This is major text")

    print('\nu' + rt.get_string_minimal('k') + rt.get_string_alert('u') + rt.get_string_warn('l') +
          rt.get_string_success('e') + rt.get_string_info('l') + rt.get_string_major('e'))


if __name__ == '__main__':
    main()
