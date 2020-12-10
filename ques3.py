import time
lyrics="Before You Go#Lewis Capaldi#I fell by the wayside, like everyone else#I hate you, I hate you, I hate you#But I was just kidding myself#Our every moment, I start to replace#Cause now that they re gone#All I hear are the words that #I needed to say"
sentence=lyrics.split('#')
l=len(sentence)
for i in range(l):
    time.sleep(1)
    print(sentence[i])