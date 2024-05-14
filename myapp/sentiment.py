from nltk.sentiment.vader import SentimentIntensityAnalyzer

def analyze_sentiment(comment):
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(comment)
    compound_score = score['compound']
    if compound_score >= 0.05:
        return 'WinnyWay(startup)'
    elif compound_score <= -0.05:
        return 'Netflix'
    else:
       return 'Amazon'