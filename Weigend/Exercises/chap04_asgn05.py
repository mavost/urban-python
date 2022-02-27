# Python3,mvs, 2017-09-27
# Chapter 4 / Assignment 5
from random import shuffle

charts = []
while True:
    try:
        title = str(input("Enter Song Title:"))
        if not title:
            print("Proceed after data entry stopped.")
            break
        charts.append(title)
    except ValueError:
        print("Proceed after bad entry.")
        break
if not charts:
    print("Terminated - Missing Data.")
    exit()

shuffle(charts)

print("Charts of this week:")
for a, song in enumerate(charts):
    print("Song "+str(a+1)+": " + song)
