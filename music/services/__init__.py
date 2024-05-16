from openai import OpenAI
import json


class CollaborativeContentFilteringModel:
    def __init__(self, threshold_value, pivot_point, partition_size):
        self.threshold_value = threshold_value
        self.pivot_point = pivot_point
        self.partition_size = partition_size

    def load(self, genres, moods, languages):
        self.genres = genres
        self.moods = moods
        self.languages = languages

    def process(self):
        prompt = "Suggest me 20 songs"
        if self.genres:
            prompt += f" with genres {', '.join(self.genres)}"
        if self.moods:
            prompt += f" and moods {', '.join(self.moods)}"
        if self.languages:
            prompt += f" in {', '.join(self.languages)}"

        prompt += """
            in JSON format. Include a key 'songs' with a list of objects containing:
            - song_name: string
            - album_name: string
            - artist_name: string
            - release_year: 4 digit year
            - ratings: float between 0 and 5

            If any of these values are missing, use random values.
        """

        client = OpenAI()
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=2000
        )

        recommendation = response.dict()['choices'][0]['text']
        return json.loads(recommendation)


class TextFilteringModel:
    def __init__(self, text):
        self.text = text

    def process(self):
        prompt = f"Suggest me 20 songs like {self.text}"

        prompt += f"""
            in JSON format. Include a key 'songs' with a list of objects containing:
            - song_name: string
            - album_name: string
            - artist_name: string
            - release_year: 4 digit year
            - ratings: float between 0 and 5

            If this text {self.text} is not a song name then return an string like 'NotASongError'.
        """

        client = OpenAI()
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=2000
        )

        recommendation = response.dict()['choices'][0]['text']
        print(recommendation)
        return json.loads(recommendation)
