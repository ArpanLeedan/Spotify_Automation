def detect(statement):
    from textblob import TextBlob

    # input statement
    # create a TextBlob object
    blob = TextBlob(statement)

    # get sentiment polarity and subjectivity
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    # define emotion based on polarity and subjectivity
    if polarity > 0 and subjectivity > 0.5:
        emotion = "joyful"
    elif polarity > 0 and subjectivity <= 0.5:
        emotion = "happy"
    elif polarity == 0 and subjectivity > 0.5:
        emotion = "neutral"
    elif polarity == 0 and subjectivity < 0.1:
        emotion = "frustrated"
    elif polarity < 0 and subjectivity > 0.5:
        emotion = "angry"
    else:
        emotion = "sad"

    from spotify_use import spotify
    spotify(emotion)
