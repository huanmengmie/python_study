# -*- coding:UTF-8 -*-
import json

from pymediainfo import MediaInfo

import subprocess
import re
import os

print(os.path.join(os.path.dirname(__file__), "movie.mp4"))
media_info = MediaInfo.parse("movie.mp4")
for track in media_info.tracks:
    if track.track_type == 'Video':
        print(dir(track))
        print(track.__dict__)
        print(track.bit_rate, track.bit_rate_mode, track.codec, track.duration)
