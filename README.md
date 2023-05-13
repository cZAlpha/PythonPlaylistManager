# PythonPlaylistManager
A Python adaptation of a simple terminal-based playlist manager. 

In this project, you will use data structures in order to make a working 
playlist manager. This will involve also using different uses of variables and 
python packages in order to complete set goals (which will mainly include finishing if statements).

# What am I supposed to do be doing?
Put simply, there are 3 if statements inside of the "playListManager" function. You are to make them functional by 
looking at the menu's response and user input section and deducing what to do. If you get stuck or want to check
your work, there is an "answer.txt" file with the answers on it. More specifically, I will list below what each
if statement / user input should do.

### Skipping forward (A)
If the user inputs "A" or "a", the song currently playing should be incremented by one. If you're at the last song
in the playlist, it should loop back to the beginning.

### Skipping backwards (B)
If the user inputs "B" or "b", the song currently playing should be decrimented by one. If you're at the first song
in the playlist, it should loop back to the end of the playlist.

### Shuffling (C)
If the user inputs "C" or "c", the current song should be a random song chosen from the playlist. In other words, you
should use the "random" python package to generate a random integer between 0 and the length of the playlist.