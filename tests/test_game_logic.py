from logic_utils import check_guess, update_score, parse_guess, get_range_for_difficulty


# --- check_guess: hints must not be backwards ---

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high_outcome():
    # Bug: was returning "Go HIGHER!" when guess was already too high
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_high_hint_says_lower():
    # Bug: hint was "Go HIGHER!" — should tell player to go LOWER
    _, message = check_guess(60, 50)
    assert "LOWER" in message

def test_guess_too_low_outcome():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_guess_too_low_hint_says_higher():
    # Bug: hint was "Go LOWER!" — should tell player to go HIGHER
    _, message = check_guess(40, 50)
    assert "HIGHER" in message

def test_check_guess_rejects_string_secret():
    # Bug: on even attempts the secret was cast to str, causing lexicographic
    # comparison ("9" > "42" is True). check_guess must always use int comparison.
    # "9" > "42" lexicographically but 9 < 42 numerically — the fix must return Too Low.
    outcome, _ = check_guess(9, 42)
    assert outcome == "Too Low"


# --- update_score: wrong guesses must never award points ---

def test_wrong_guess_loses_points():
    # Bug: on even attempt numbers a Too High outcome awarded +5 points
    score_after = update_score(100, "Too High", attempt_number=2)
    assert score_after == 95  # always -5, never +5

def test_wrong_guess_odd_attempt_loses_points():
    score_after = update_score(100, "Too High", attempt_number=3)
    assert score_after == 95

def test_too_low_loses_points():
    score_after = update_score(100, "Too Low", attempt_number=2)
    assert score_after == 95

def test_win_awards_points():
    # attempt_number=1 → points = 100 - 10*(1+1) = 80
    score_after = update_score(0, "Win", attempt_number=1)
    assert score_after == 80

def test_win_score_minimum_10():
    # Late win should award at least 10 points, never go negative
    score_after = update_score(0, "Win", attempt_number=100)
    assert score_after == 10


# --- get_range_for_difficulty: Easy must not be harder than Normal ---

def test_easy_allows_more_attempts_range():
    # Bug: Easy range was 1-20 and Normal was 1-100, making Easy harder
    easy_low, easy_high = get_range_for_difficulty("Easy")
    normal_low, normal_high = get_range_for_difficulty("Normal")
    easy_range = easy_high - easy_low
    normal_range = normal_high - normal_low
    assert easy_range <= normal_range  # Easy should not cover MORE values than Normal

def test_hard_range_is_widest():
    # Hard should have the largest range (hardest to guess)
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high >= normal_high
    assert hard_high >= easy_high


# --- parse_guess: basic input validation ---

def test_parse_guess_valid():
    ok, value, _ = parse_guess("42")
    assert ok is True
    assert value == 42

def test_parse_guess_empty_string():
    ok, value, _ = parse_guess("")
    assert ok is False
    assert value is None

def test_parse_guess_none():
    ok, _, _ = parse_guess(None)
    assert ok is False

def test_parse_guess_non_numeric():
    ok, _, err = parse_guess("abc")
    assert ok is False
    assert err == "That is not a number."

def test_parse_guess_float_string_truncates():
    ok, value, _ = parse_guess("3.9")
    assert ok is True
    assert value == 3