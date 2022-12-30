from paginator.paginator import Paginator
from collections import deque

import pytest

@pytest.fixture()
def paginator():
    return Paginator(current_page=1, total_pages=1, boundaries=0, around=0)


@pytest.mark.parametrize("pages, next_pages, expected", [
        (deque([1, 2, 3]), deque([3]), deque([1, 2])),
        (deque([1, 2, 3]), deque([]), deque([1, 2, 3])),
        (deque([1, 2]), deque([3]), deque([1, 2])),
        (deque([]), deque([3]), deque([]))
])
def test__remove_duplicates(
    paginator: Paginator, pages: int, next_pages: deque, expected: deque
):
    result = paginator._remove_duplicates(pages, next_pages)

    assert result == expected


@pytest.mark.parametrize("total_pages, pages, expected", [
    (10, deque([-1, 0, 1, 2]), deque([1, 2])),
    (10, deque([9, 10, 11, 12]), deque([9, 10])),
    (3, deque([-1, 0, 1, 2, 3, 4]), deque([1, 2, 3]))
])
def test__get_valid_pagination(paginator: Paginator, total_pages: int, pages: deque, expected: deque):
    paginator.total_pages = total_pages
    
    result = paginator._get_valid_pagination(pages)

    assert result == expected


@pytest.mark.parametrize("pages, indexes_list_to_be_filled", [
    (deque([1, 10]), [1]),
    (deque([1, 2, 9, 10]), [2]),
    (deque([1, 5, 6, 10]), [3, 1]),
    (deque([1, 4, 10]), [2, 1])
])
def test__insert_dots(paginator: Paginator, pages: deque, indexes_list_to_be_filled: list):
    paginator.total_pages = 10

    result = paginator._insert_dots(pages)

    assert list(result) == indexes_list_to_be_filled


@pytest.mark.parametrize("pages, expected", [
    (deque([1, 2, 3]), 0),
    (deque([3, 4, 5]), 0),
    (deque([10]), 0)
])
def test__get_first_page_index(paginator: Paginator, pages: deque, expected: int):
    result = paginator._get_first_page_index(pages)

    assert result == expected


@pytest.mark.parametrize("pages, expected", [
    (deque([1, 2, 3, 4, 5]), 4),
    (deque([3, 4, 5]), 2),
    (deque([2, 3, 4, 5]), 3)
])
def test__get_last_page_index(paginator: Paginator, pages: deque, expected: int):
    paginator.total_pages = 5

    result = paginator._get_last_page_index(pages)

    assert result == expected


@pytest.mark.parametrize("boundaries, expected", [
        (1, deque([1])),
        (2, deque([1, 2])),
        (3, deque([1, 2, 3]))
])
def test__get_first_pages(paginator: Paginator, boundaries: int, expected: deque):
    paginator.boundaries = boundaries

    result = paginator._get_first_pages()

    assert result == expected


@pytest.mark.parametrize("current_page, around, expected", [
        (5, 2, deque([3, 4, 5, 6, 7])),
        (5, 1, deque([4, 5, 6])),
        (7, 3, deque([4, 5, 6, 7, 8, 9, 10])),
        (3, 2, deque([1, 2, 3, 4, 5])),
])
def test__get_middle_pages(paginator: Paginator, current_page: int, around: int, expected: deque):
    paginator.around = around
    paginator.current_page = current_page
    paginator.total_pages = 10

    result = paginator._get_middle_pages()

    assert result == expected


@pytest.mark.parametrize("pages, boundaries, expected", [
        (10, 1, deque([10])),
        (10, 2, deque([9, 10])),
        (10, 3, deque([8, 9, 10])),
])
def test__get_final_pages(paginator: Paginator, pages: deque, boundaries: int, expected: deque):
    paginator.boundaries = boundaries
    paginator.total_pages = 10

    result = paginator._get_final_pages()

    assert result == expected