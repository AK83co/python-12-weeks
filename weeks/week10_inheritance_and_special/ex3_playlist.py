"""
Week 10 · Exercise 3: Playlist

Make a Playlist with an add(song) method, support for len(), and a
total_minutes() method. Each song is a tuple of (title, minutes).

Examples:
    p = Playlist()
    p.add(("Song A", 3)); p.add(("Song B", 4))
    len(p)             →  2
    p.total_minutes()  →  7

Check your answer:  python check.py 10 playlist
"""

class Playlist:
    def __init__(self):
        self.songs = []
