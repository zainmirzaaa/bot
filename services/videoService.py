import os
import random
import shutil

VIDEO_EXTENSIONS = (".mp4", ".mov", ".webm")


def get_random_video(folder):
    if not os.path.isdir(folder):
        return None
    videos = [f for f in os.listdir(folder) if f.endswith(VIDEO_EXTENSIONS)]
    if not videos:
        return None
    return os.path.join(folder, random.choice(videos))


def mark_as_sent(video_path, sent_folder):
    os.makedirs(sent_folder, exist_ok=True)
    shutil.move(video_path, os.path.join(sent_folder, os.path.basename(video_path)))