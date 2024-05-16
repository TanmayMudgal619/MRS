from dataclasses import dataclass


@dataclass
class Song:
    song_name: str
    album_name: str
    artist_name: str
    release_year: int
    ratings: float
