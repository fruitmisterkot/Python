from typing import List
from typing import Tuple


class Account:
    nickname = ""

    def __init__(self, nickname: str):
        if (not nickname):
            raise AttributeError('Please provide a nickname')
        self.nickname = nickname


class Track:
    _name = ""
    likes = 0

    def __init__(self, name: str):
        """
        Track must have name
        >>> Track(None)
        Traceback (most recent call last):
        ...
        AttributeError: Please provide track name
        """
        if (not name):
            raise AttributeError('Please provide track name')
        self._name = name

    @property
    def name(self):
        """
        Returns track name
        >>> Track("somename").name
        'somename'

        You cant rename track
        >>> Track("whatever").name = 'new_name'
        Traceback (most recent call last):
        ...
        AttributeError: property 'name' of 'Track' object has no setter
        """
        return self._name

    def __repr__(self):
        return f"Track:Name: {self._name}"


class Album:
    __tracks = []
    __name = ""

    def __init__(self, name: str, tracks: List[Track]):
        """
        Album must contain at least one track
        >>> Album("123", [])
        Traceback (most recent call last):
        ...
        AttributeError: Album must contain at least one track

        Album must have name
        >>> Album(None, [Track("123")])
        Traceback (most recent call last):
        ...
        AttributeError: Provide name for album
        """
        if (not name):
            raise AttributeError('Provide name for album')
        if (len(tracks) == 0):
            raise AttributeError('Album must contain at least one track')

        self.__tracks = tracks
        self.__name = name

    def __repr__(self):
        return f"Album: Name:{self.__name} Tracks: {','.join([repr(x) for x in self.__tracks])}"


class Listener(Account):
    __favorite_tracks = []

    def __init__(self, nickname: str):
        super().__init__(nickname)

    @property
    def favorite_tracks(self) -> Tuple[Track]:
        return tuple(self.__favorite_tracks)

    def like_track(self, track: Track):
        """Add track to favorites
        You cant like track twice
        >>> track = Track('1')
        >>> listener = Listener('somename')
        >>> listener.like_track(track)
        >>> listener.like_track(track)
        >>> track.likes == 1
        True
        """
        if track not in self.__favorite_tracks:
            self.__favorite_tracks.append(track)
            track.likes += 1

    def dislike_track(self, track: Track):
        """Add track to favorites
        You cant unlike not liked track
        >>> track = Track('1')
        >>> listener = Listener('somename')
        >>> listener.dislike_track(track)
        >>> track.likes == 0
        True
        """
        if track in self.__favorite_tracks:
            self.__favorite_tracks.remove(track)
            track.likes -= 1


class Singer(Account):
    __albums = []

    def __init__(self, nickname: str):
        super().__init__(nickname)

    def publish_album(self, name: str, tracks: List[Track]) -> Album:
        """Adds new album for singer

        >>> Singer("Test").publish_album("somealbum", [Track('1'), Track('2')])
        Album: Name:somealbum Tracks: Track:Name: 1,Track:Name: 2

        """
        album = Album(name, tracks)
        self.__albums.append(album)
        return album

    @property
    def albums(self):
        return tuple(self.__albums)

    def __repr__(self):
        return f"Singer:Name:{self.nickname} Albums:{','.join([repr(x) for x in self.albums])}"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
