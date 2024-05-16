from marshmallow import Schema
from marshmallow.fields import String, List


class SuggestMusicRequest(Schema):
    genres = List(String(), required=True)
    moods = List(String(), required=True)
    languages = List(String(), required=True)


class SearchMusicRequest(Schema):
    text = String(required=True)
