import time
lyrics="You were the popular one, the popular chick,#Standing on the field with your pretty pompons#Now you're working at the movie selling popular corn#I could have been a mess but I never went wrong#'Cause I'm putting down my story in a popular song"
sentence=lyrics.split('#')
l=len(sentence)
for i in range(l):
    time.sleep(1)
    print(sentence[i])
