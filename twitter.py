from textblob import TextBlob

def analyze_sentiment(tweet):
    blob = TextBlob(tweet)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity == 0:
        return "Neutral"
    else:
        return "Negative"

def main():
    tweet = input("Tweet: ").strip()
    if not tweet:
        print("Kindly enter your tweet.")
        return
    print(analyze_sentiment(tweet))

if __name__ == '__main__':
    main()
