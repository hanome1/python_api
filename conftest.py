import pytest

@pytest.fixture()
def word_good():
    return 'колбаса'

@pytest.fixture()
def word_bad():
    return 'калбаса'

 