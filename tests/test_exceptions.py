from paginator.exceptions import PaginatorError
from paginator.paginator import Paginator

import pytest

import re

def test_all_zero():
    with pytest.raises(PaginatorError, match=re.escape("\n* The current page (0) is out of range of total pages (0). \n- Please try again:\n")):
        p = Paginator(0, 0, 0, 0)
        p.paginate()

def test_current_page_zero():
    with pytest.raises(PaginatorError, match=re.escape("\n* The current page (0) is out of range of total pages (20). \n- Please try again:\n")):
        p = Paginator(20, 0, 0, 0)
        p.paginate()

def test_zero_pages():
    with pytest.raises(PaginatorError, match=re.escape("\n* The current page (1) is out of range of total pages (0). \n- Please try again:\n")):
        p = Paginator(0, 1, 0, 0)
        p.paginate()

def test_current_page_out_of_range():
    with pytest.raises(PaginatorError, match=re.escape("\n* The current page (11) is out of range of total pages (10). \n- Please try again:\n")):
        p = Paginator(10, 11, 2, 2)
        p.paginate()

def test_negative_inputs():
    with pytest.raises(PaginatorError, match=re.escape("\n* The current page (-2) is out of range of total pages (-1). \n- Please try again:\n")):
        p = Paginator(-1, -2, 2, 2)
        p.paginate()

def test_string_as_all_inputs():
    with pytest.raises(TypeError, match="'<' not supported between instances of 'str' and 'int'"):
        p = Paginator('s', 'a', 'a', 's')
        p.paginate()

def test_total_pages_and_around_as_string_inputs():
    with pytest.raises(TypeError, match="'<' not supported between instances of 'str' and 'int'"):
        p = Paginator(10, '1', '2', 4)
        p.paginate()

def test_total_pages_and_current_page_as_string_inputs():
    with pytest.raises(TypeError, match="'<' not supported between instances of 'str' and 'int'"):
        p = Paginator('10', '5', 2, 2)
        p.paginate()

def test_around_and_boundaries_as_string_inputs():
    with pytest.raises(TypeError, match=re.escape(r"unsupported operand type(s) for +: 'int' and 'str'")):
        p = Paginator(10, 5, '2', '2')
        p.paginate()

def test_remove_excessive_pages_out_of_range():
    # The highest possible recursion limit is platform-dependent. https://docs.python.org/3/library/sys.html#sys.setrecursionlimit
    with pytest.raises(RecursionError, match="maximum recursion depth exceeded in comparison"):
        p = Paginator(10, 5, 1000, 1000)
        p.paginate()