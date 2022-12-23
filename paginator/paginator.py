
from paginator.exceptions import PaginatorErrorHelper 
from collections import deque
from typing import Deque
from itertools import islice

class Paginator:
    PAGE_ONE = 1
    DOTS = '...'

    def __init__(self, total_pages: int, current_page: int, boundaries: int, around: int) -> None:
        self.total_pages = total_pages
        self.current_page = current_page
        self.boundaries = boundaries
        self.around = around

        PaginatorErrorHelper(
            total_pages, current_page, boundaries, around
        )._check_pages_range()

    # Methods for Deque treatment
    # The method will avoid duplicated numbers with the next set of pages, using recursion
    def _remove_duplicates(self, pages: Deque, next_pages: Deque) -> Deque:

        # Snippet to avoid trying to find pages in indexes that doesn't exists
        if not pages or not next_pages:
            return pages
        
        last_page = pages[-1]

        if last_page >= next_pages[0]:
            pages.pop()

            return self._remove_duplicates(pages, next_pages)
        else:
            return deque(islice(pages, 0, pages.index(last_page) + 1))

    # The method will remove the pages that surpass the boundaries, as well as the non-positive pages
    def _get_valid_pagination(self, pages: Deque) -> Deque:
        first_page_index = self._get_first_page_index(pages)
        last_page_index = self._get_last_page_index(pages)

        return deque(islice(pages, first_page_index, last_page_index + 1))


    # Method to insert the three dots (...) on correspondent indexes
    def _insert_dots(self, pages: Deque) -> Deque:
        
        indexes_list_to_be_filled = []

        if not pages or pages == deque([0]):
            return indexes_list_to_be_filled

        if pages[0] != self.PAGE_ONE:
            indexes_list_to_be_filled.append(0)

        for i, value in enumerate(pages):
            try:
                # print("i: {}\npages: {}".format(i, pages[i]))
                print("value: {}".format(value))
                if value + 1 != pages[i + 1]:
                    indexes_list_to_be_filled.append(i + 1)
            except IndexError:
                break

        if pages[-1] != self.total_pages:
            indexes_list_to_be_filled.append(len(pages))

        # The reversed method avoid the last number of the middle pages from being transferred to the last set of pages
        return reversed(indexes_list_to_be_filled)



    def _get_first_page_index(self, pages: Deque) -> Deque:
        try:
            return pages.index(self.PAGE_ONE)
        except ValueError:
            return 0

    def _get_last_page_index(self, pages: Deque) -> Deque:
        try:
            return pages.index(self.total_pages)
        except ValueError:
            return self.total_pages
            

    def _get_first_pages(self) -> Deque:
        first_pages = deque(range(self.PAGE_ONE, self.PAGE_ONE + self.boundaries))
        return first_pages

    def _get_middle_pages(self) -> Deque:
        middle_pages = deque([self.current_page])
        for i in range(1, self.around + 1):
            middle_pages.appendleft(self.current_page - i)
            middle_pages.append(self.current_page + i)

        # The call of _get_valid_pagination method here in the middle pages avoid duplicate numbers
        middle_pages = self._get_valid_pagination(middle_pages)
        return middle_pages

    def _get_final_pages(self) -> Deque:
        final_pages = self.total_pages + 1
        final_pages = deque(range(final_pages - self.boundaries, final_pages))

        return final_pages

    


    def _paginate(self):
        first = self._get_first_pages()
        middle = self._get_middle_pages()
        last = self._get_final_pages()

        res = first
        self._remove_duplicates(res, middle)
        
        res += middle
        self._remove_duplicates(res, last)

        res += last

        res = self._get_valid_pagination(res)

        pages_with_dots = self._insert_dots(res)

        for i in pages_with_dots:
            res.insert(i, self.DOTS)

        res = " ".join([str(x) for x in res])

        return res










