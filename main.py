from paginator.paginator import Paginator
from paginator.exceptions import PaginatorError

def input_number(message: str) -> int:

    number = None

    while number == None or number < 0:
        try:
            number = int(input(message))
            if number < 0 or number == None:
                raise ValueError
        except ValueError:
            print("* Please enter a positive number")

    return number

def run():
    total_pages = input_number("- Enter the total of pages: ")
    current_page = input_number("- Enter the current page: ")
    boundaries = input_number("- Insert the boundaries: ")
    around = input_number("- Insert the around pages: ")

    try:
        paginator = Paginator(total_pages, current_page, boundaries, around)
        print(paginator._paginate())

        print("\n")
        run()

    except PaginatorError as e:
        print(e)
        run()
        
if __name__ == '__main__':
    run()