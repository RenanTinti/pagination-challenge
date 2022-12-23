class PaginatorError(ValueError):
    ...

class PaginatorErrorHelper:
    PAGE_ONE = 1

    def __init__(self, total_pages: int, current_page: int, boundaries: int, around: int) -> None:
        self.total_pages = total_pages
        self.current_page = current_page
        self.boundaries = boundaries
        self.around = around

    def _check_pages_range(self):
        if self.current_page < self.PAGE_ONE or self.current_page > self.total_pages:
            raise PaginatorError("\n* The current page ({}) is out of range of total pages ({}). \n- Please try again:\n".format(self.current_page, self.total_pages))