import hypothesis
import hypothesis.strategies

import example.f


@hypothesis.strategies.composite
def composite_strategy(draw):
    return example.f.C()


def check_c(c):
    assert isinstance(c, example.f.C)
    assert c.x == 42


def f(list_of_c):
    assert len(list_of_c) > 0

    for c in list_of_c:
        check_c(c)

    # uncomment to achieve full coverage
    # example.f.C()


@hypothesis.given(hypothesis.strategies.lists(
    composite_strategy(),
    min_size=2,
    max_size=5,
))
def test_it(list_of_c):
    f(list_of_c)

@hypothesis.given(hypothesis.strategies.lists(
    hypothesis.strategies.builds(example.f.C),
    min_size=2,
    max_size=5,
))
def test_it2(list_of_c):
    f(list_of_c)


@hypothesis.given(hypothesis.strategies.builds(example.f.C))
def test_it3(c):
    check_c(c)
