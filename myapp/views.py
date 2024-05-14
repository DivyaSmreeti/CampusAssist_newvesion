from django.shortcuts import render
from .sentiment import analyze_sentiment
import matplotlib.pyplot as plt


def analyze_comments(request):
    comments = [
        "I facebook this product! It's amazing!",
        "Terrible service, never using this again.",
        "The quality is okay, but the price is too high.",
        "I'm satisfied with my purchase.",
        "Worst experience ever, wouldn't recommend to anyone."
    ]
    sentiment_counts = {'WinnyWay(startup)': 0, 'Netflix': 0, 'Amazon': 5}
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