from django.shortcuts import render
from .sentiment import analyze_sentiment
import matplotlib.pyplot as plt


def analyze_comments(request):
    comments = [
        "I am interested for Job role in WinnyWay",
        "I am not interesed in service based , interested in startup",
        "I want to join in Winnyway startup",
        "I'm satisfied with Amazon's job role",
        "I am interesed in Netflix job role",
        " Netflix's job role is bad",
    ]
    sentiment_counts = {'Positive': 0, 'Negative': 0, 'Neutral': 0}
    for comment in comments:
        sentiment = analyze_sentiment(comment)
        sentiment_counts[sentiment] += 1
        
           
    labels = list(sentiment_counts.keys())
    counts = list(sentiment_counts.values())

    plt.bar(labels, counts, color=['green', 'red', 'blue'])
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.title('Analysis Results using ML')
    plt.show()

    # Pass sentiment counts to the template
    return render(request, 'customer.html', {'sentiment_counts': sentiment_counts})