def insert_song(playlist, song):
    a=playlist.copy(); a.append(song); i=len(a)-2
    while i>=0 and a[i][1]>song[1]:
        a[i+1]=a[i]; i-=1
    a[i+1]=song
    return a

if __name__ == "__main__":
    playlist=[("Intro",120),("Chill Beat",210),("Long Jam",340)]
    updated=insert_song(playlist,("Quick Track",180))
    durations=[s[1] for s in updated]
    assert durations==sorted([120,210,340,180])
    assert ("Quick Track",180) in updated
    print("All test cases passed!")
