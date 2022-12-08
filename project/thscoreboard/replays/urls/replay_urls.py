from django.urls import path

from replays.views import create_replay
from replays.views import index
from replays.views import replay_list
from replays.views import user
from replays.views import view_replay


urlpatterns = [
    path('', index.index, name='index'),
    path('upload', create_replay.upload_file, name='upload_file'),
    path('publish/<int:temp_replay_id>', create_replay.publish_replay),
    path('publish/<str:game_id>', create_replay.publish_replay_no_file),
    path('user/<str:username>', user.user_page),
    path('<str:game_id>', replay_list.game_scoreboard),
    path('<str:game_id>/d<int:difficulty>', replay_list.game_scoreboard),
    path('<str:game_id>/d<int:difficulty>/<str:shot_id>', replay_list.game_scoreboard),
    path('<str:game_id>/<int:replay_id>', view_replay.replay_details),
    path('<str:game_id>/<int:replay_id>/edit', view_replay.edit_replay),
    path('<str:game_id>/<int:replay_id>/download', view_replay.download_replay),
    path('<str:game_id>/<int:replay_id>/delete', view_replay.delete_replay),
]
