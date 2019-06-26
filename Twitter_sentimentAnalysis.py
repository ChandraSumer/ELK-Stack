#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import flask
import textblob
app=flask.Flask(__name__)
@app.route('/sentiment',methods=['POST'])
def sentiment_analysis():
    tweet_text=flask.request.json["submit"]
    tweet_text_str=str(tweet_text)
    tweet_score=textblob.TextBlob(tweet_text_str).sentiment.polarity
    if tweet_score < 0:
        sentiment = "negative"
    elif tweet_score == 0:
        sentiment = "neutral"
    else:
        sentiment = "positive"
    return flask.jsonify(sentiment)
if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
    


# In[ ]:




