# Project: Playlist Manager
# Author:  Noah Klaus
# Date:    05/13/23

# START - Imports
import random
import time
# STOP  - Imports



# START - Functions
    # The function "clearTerminal" is a function that prints a bunch of blank strings to clear the terminal
def clearTerminal():
    for i in range(20):
        print("")

    # The function "playListManager" is the menu used to navigate through the list of songs returned by the playlist function
def playListManager(songIndex):
    # The "songList" is a list that holds the songs that will be used in your playlist manager
    songList = ["Avalon", "Warning", "Gimme the Loot", "GOSHA", "Jus better", "12 Stout Street"]
    # An internal variable used to keep track of the current song that you're playing
    internalSongIndex = songIndex

    # The print statements below serve as the basis for the 'menu' for the playlist manager
    print("===================================")
    print("| Python Playlist Manager")
    print("|")
    print("| Current Index: " + str(internalSongIndex))
    print("| Current Song: " + songList[internalSongIndex])
    print("|")
    print("| Options:")
    print("|          A) Skip Forward")
    print("|          B) Skip Backwards")
    print("|          C) Shuffle")
    print("|")
    # This line below gets input from the user by prompting them
    userInput = input("Input:")

    # If statement for skipping forward
    if (userInput == "A" or userInput == "a"):
        # TO DO
        pass
    # If statement for skipping backwards
    elif (userInput == "B" or userInput == "b"):
        # TO DO
        pass
    # If statement for shuffling
    elif (userInput == "C" or userInput == "c"):
        # TO DO
        pass
    # Else statement to catch bad user inputs
    else:
        clearTerminal()
        print("BAD RESPONSE, TRY AGAIN...")
        time.sleep(3)
        clearTerminal()

    # Re-calls the function so that the menu persists
    playListManager(internalSongIndex)
# STOP - Functions



# Initial function call, arbitrarily called to the index of 0 (the first song)
playListManager(0)