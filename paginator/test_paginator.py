from paginator.exceptions import PaginatorError
from paginator.paginator import Paginator
import pytest

def test_few_pages():
    p = Paginator(10, 5, 2, 2)
    assert p.paginate() == '1 2 3 4 5 6 7 ... 9 10'

def test_many_pages():
    p = Paginator(568, 213, 2, 5)
    assert p.paginate() == '1 2 ... 208 209 210 211 212 213 214 215 216 217 218 ... 567 568'

def test_lots_of_pages():
    p = Paginator(10000, 2100, 3, 2)
    assert p.paginate() == '1 2 3 ... 2098 2099 2100 2101 2102 ... 9998 9999 10000'

def test_no_boundaries():
    p = Paginator(20, 10, 0, 2)
    assert p.paginate() == '... 8 9 10 11 12 ...'

def test_no_around():
    p = Paginator(20, 10, 2, 0)
    assert p.paginate() == '1 2 ... 10 ... 19 20'

def test_all_one():
    p = Paginator(1, 1, 1, 1)
    assert p.paginate() == '1'

def test_all_five():
    p = Paginator(5, 5, 5, 5)
    assert p.paginate() == '1 2 3 4 5'

def test_dots_in_the_beggining():
    p = Paginator(20, 18, 0, 2)
    assert p.paginate() == '... 16 17 18 19 20'

def test_dots_in_the_end():
    p = Paginator(20, 2, 0, 2)
    assert p.paginate() == '1 2 3 4 ...'

def test_dots_exactly_in_middle():
    p = Paginator(20, 16, 9, 2)
    assert p.paginate() == '1 2 3 4 5 6 7 8 9 ... 12 13 14 15 16 17 18 19 20'

def test_removed_duplicated_pages():
    p = Paginator(20, 10, 10, 10)
    assert p.paginate() == '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20'

def test_remove_pages_out_of_range():
    p = Paginator(10, 5, 15, 15)
    assert p.paginate() == '1 2 3 4 5 6 7 8 9 10'

def test_boundaries_bigger_than_around_first_pages():
    p = Paginator(10, 1, 6, 1)
    assert p.paginate() == '1 2 3 4 5 6 7 8 9 10'

def test_boundaries_bigger_than_around_last_pages():
    p = Paginator(10, 10, 3, 1)
    assert p.paginate() == '1 2 3 ... 8 9 10'


# Exception tests
def test_all_zero():
    with pytest.raises(PaginatorError):
        p = Paginator(0, 0, 0, 0)
        p.paginate()

def test_current_page_zero():
    with pytest.raises(PaginatorError):
        p = Paginator(20, 0, 0, 0)
        p.paginate()

def test_zero_pages():
    with pytest.raises(PaginatorError):
        p = Paginator(0, 1, 0, 0)
        p.paginate()

def test_current_page_out_of_range():
    with pytest.raises(PaginatorError):
        p = Paginator(10, 11, 2, 2)
        p.paginate()

def test_negative_inputs():
    with pytest.raises(PaginatorError):
        p = Paginator(-1, -2, 2, 2)
        p.paginate()

def test_remove_excessive_pages_out_of_range():
    # The highest possible recursion limit is platform-dependent. https://docs.python.org/3/library/sys.html#sys.setrecursionlimit
    with pytest.raises(RecursionError, match="maximum recursion depth exceeded in comparison"):
        p = Paginator(10, 5, 1000, 1000)
        p.paginate()