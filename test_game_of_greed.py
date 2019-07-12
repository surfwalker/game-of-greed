from game_of_greed import track_scores


def test_init_track_scores():
    assert track_scores

# non scoring roll should return 0

def test_zilch():
    expected = 0
    actual = track_scores(['2', '3', '4', '6'])
    assert actual == expected

# rolls with various number of 1s should return correct score

def test_ones():
    assert track_scores([1]) == 100
    
