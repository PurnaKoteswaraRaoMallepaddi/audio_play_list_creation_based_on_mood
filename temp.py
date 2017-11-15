# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from flask import Flask, render_template
import spotipy
import seaborn as sns
import spotipy.util as util
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
import glob
import json
import oauth2 as oauth
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB 
import playsound
#paths_for_songs = list(['C:/Users/purna/Desktop/python frodata science/project/tylor_baby.mp3','C:/Users/purna/Desktop/python frodata science/project/tylor_baby.mp3','C:/Users/purna/Desktop/python frodata science/project/tylor_baby.mp3','C:/Users/purna/Desktop/python frodata science/project/tylor_baby.mp3','C:/Users/purna/Desktop/python frodata science/project/tylor_baby.mp3','C:/Users/purna/Desktop/python frodata science/project/tylor_baby.mp3'])
moods = list(['sad','happy','neutral'])
l = 0
app = Flask(__name__)


@app.route("/<name>")
def index(name):
    consumer_key = 'Va0hCYdY3MnKk5H4ua1jtw9CX'
    consumer_secret = 'HMsVcZPxQMs9xPXcOhJX55rfWQzdsWODO15gOmH4Dn0zFlLxK5'
    access_token = '831922665245913088-Ye3YtqsLRjK2GLB68EaMWgyyt1O91Lo'
    access_token_secret = 'Pw4EFeD0UXw4HXZIWhgVICZQRUmh0Uqo0okbIq0uqVKz4'

    consumer = oauth.Consumer(key=consumer_key,secret=consumer_secret)
    access_token = oauth.Token(key=access_token,secret=access_token_secret)
    client = oauth.Client(consumer,access_token)


    timeline_endpoint = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=	PurnaRao007 &count=1"

    response, data = client.request(timeline_endpoint)
    print('purna')
    tweets = json.loads(data)
    for tweet in tweets:
       P = tweet['text']
       print(P)


    Q = [P]
    stream = pd.read_csv('twitdb.csv')    #THIS CONTAINS THE DATA I GOT FROMTHE TWITTER


    spamset = stream.tweetsad 
 
    bow = CountVectorizer()

    A = bow.fit_transform(spamset)



    X = A.toarray()


    Y = stream.y 

    Z=bow.transform(Q).toarray()
    clf = MultinomialNB()
 
    clf.fit(X, Y)

    l = clf.predict(Z)
    #print(moods[1])
    
    return render_template("index.html", name = moods[l])

@app.route("/purna" , methods = ['POST'])
def purna():
    print('jgsd')
    path = 'C:/Users/purna/Desktop/python frodata science/project/audiowav/'
    allfiles = glob.glob(path + "/*.csv")
    frame = pd.DataFrame()
    list_ = []
    for file_ in allfiles:
        df = pd.read_csv(file_,index_col = None,header = 0)
        list_.append(df)
    frame = pd.concat(list_)
    frame_1 = frame.dropna(axis = 0)
    X = np.array(frame_1.drop(['id','name','uri','artist','lable','tempo','liveness','time_signature','danceability','key','duration_ms','valence','mode','speechiness'],1))


    Y = np.array(frame_1.lable)

    clf = RandomForestClassifier(n_estimators=10)
    clf.fit(X,Y)

    scope = 'user-library-read'
    token = util.prompt_for_user_token(' 21pdfj4labuq4x4od5gbcmkuy ',scope,'7b533ddee532490a9a3b558795219ef1','b9925d3c71504b70b741344da0a00883','http://mysite.com/callback/')
    sp = spotipy.Spotify(auth=token)
    i='https://open.spotify.com/track/2CvOqDpQIMw69cCzWqr5yr','https://open.spotify.com/track/3yfqSUWxFvZELEM4PmlwIR','https://open.spotify.com/track/0wi9VaczZO8tbBwltGiwO5','https://open.spotify.com/track/6LY6qQmguN9HRXieGqZfke','https://open.spotify.com/track/4kgsK0fftHtg9gZOzkU5T2'
    tre=sp.audio_features(i)
    pre = []
    for i in tre:
        aud = [i['energy'],i['instrumentalness'],i['loudness'],i['acousticness']]
        pre.append(int(clf.predict(aud)))
    print(pre)
    print(l)
    pre[0] = 3
    pre[1] = 2
    paths_songs_sorted = []
    paths_song = list(['C:/Users/purna/Desktop/python frodata science/project/tylor_baby.mp3','C:/Users/purna/Desktop/python frodata science/project/OMI.mp3','C:/Users/purna/Desktop/python frodata science/project/OMI.mp3','C:/Users/purna/Desktop/python frodata science/project/2_states.mp3'])
    if l == 0:
        for genre in range(4):
            if pre[genre] == 3 or pre[genre] == 2:
                print('yes')
                paths_songs_sorted.append(paths_song[genre])
    if l == 1:
        for genre in range(4):
            print('no')
            if pre[genre] == 0 or pre[genre] == 1:
                paths_songs_sorted.append(paths_song[genre])

    print(paths_songs_sorted)
    for gre in paths_songs_sorted:
        playsound.playsound(str(gre),True)
    return



if __name__ == "__main__":
    #mood_code = mood_detector()
    #index(mood_code)
    app.run()
    
    