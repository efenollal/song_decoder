#!/usr/bin/python

'''
 Implementation of song decoder exercise
 The objective of the function is to clean the 
 lyrics passed by eliminating the WUB string and
 return the cleaned string
'''


def song_decoder(song):
    return " ".join(song.replace('WUB', ' ').split())


print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))
