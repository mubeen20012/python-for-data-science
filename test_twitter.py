from twitter import analyze_sentiment

def test_positive():
    assert analyze_sentiment("I love programming") == "Positive"

def test_neutral():
    assert analyze_sentiment("It is a chair") == "Neutral"

def test_negative():
    assert analyze_sentiment("I hate bugs") == "Negative" == "Negative"



