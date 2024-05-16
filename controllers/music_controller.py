from services.music_services import MusicServices


class MusicController:
    def suggest_music(self, json_data):
        genres = json_data["genres"]
        moods = json_data["moods"]
        languages = json_data["languages"]
        return MusicServices().suggest_music(genres, moods, languages)

    def search_music(self, json_data):
        text = json_data["text"]
        return MusicServices().search_music(text)
