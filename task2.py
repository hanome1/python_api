from task1 import check_word

def test_word(word_good, word_bad):
    print(word_good, word_bad)
    assert word_good in check_word(word_bad)