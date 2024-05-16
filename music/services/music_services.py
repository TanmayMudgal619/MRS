from . import CollaborativeContentFilteringModel, TextFilteringModel
from uuid import uuid4


class MusicServices:
    def suggest_music(self, genres, moods, languages):
        filteringModel = CollaborativeContentFilteringModel(
            threshold_value=20,
            pivot_point=49.76,
            partition_size=50
        )

        filteringModel.load(genres, moods, languages)
        return filteringModel.process()

    def search_music(self, text):
        filteringModel = TextFilteringModel(text)
        return filteringModel.process()
