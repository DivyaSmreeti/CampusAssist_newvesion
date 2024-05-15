from nltk.sentiment.vader import SentimentIntensityAnalyzer

def analyze_sentiment(comment):
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(comment)
    compound_score = score['compound']
    if compound_score >= 0.05:
        return 'Positive'
    elif compound_score <= -0.05:
        return 'Negative'
    else:
       return 'Neutral'