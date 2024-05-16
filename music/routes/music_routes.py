from flask_smorest import Blueprint
from flask.views import MethodView
from flask import render_template

from controllers.music_controller import MusicController
from helpers.token_validator import not_signed_in
from schemas.music_schema import SuggestMusicRequest, SearchMusicRequest


blp = Blueprint("Music", __name__)


@blp.route("/")
class DashboardRoute(MethodView):
    @not_signed_in
    def get(self):
        return render_template('index.html')



@blp.route("/search")
class DashboardRoute(MethodView):
    @not_signed_in
    def get(self):
        return render_template('search.html')


@blp.route("/get-recommendation")
class MusicSuggestionRoute(MethodView):
    @not_signed_in
    @blp.arguments(SuggestMusicRequest)
    def post(self, music_data):
        return MusicController().suggest_music(music_data)


@blp.route("/search")
class MusicSearchRoute(MethodView):
    @not_signed_in
    @blp.arguments(SearchMusicRequest)
    def post(self, music_data):
        return MusicController().search_music(music_data)
