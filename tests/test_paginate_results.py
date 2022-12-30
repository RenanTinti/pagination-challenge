from paginator.paginator import Paginator


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

def test_two_pages_with_dots_in_the_beggining():
    p = Paginator(2, 2, 0, 0)
    assert p.paginate() == '... 2'

def test_two_pages_with_dots_in_the_end():
    p = Paginator(2, 1, 0, 0)
    assert p.paginate() == '1 ...'

def test_one_boundarie_and_one_around_beggining():
    p = Paginator(10, 2, 1, 1)
    assert p.paginate() == '1 2 3 ... 10'

def test_one_boundarie_and_one_around_end():
    p = Paginator(10, 9, 1, 1)
    assert p.paginate() == '1 ... 8 9 10'

def test_a_single_middle_page():
    p = Paginator(10, 5, 0, 0)
    assert p.paginate() == '... 5 ...'

def test_big_interval():
    p = Paginator(1000, 500, 0, 0)
    assert p.paginate() == '... 500 ...'

def test_short_interval():
    p = Paginator(3, 1, 1, 0)
    assert p.paginate() == '1 ... 3'

def test_few_pages_with_excessive_boundaries_and_around():
    p = Paginator(5, 1, 500, 500)
    assert p.paginate() == '1 2 3 4 5'