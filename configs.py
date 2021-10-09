import os


class Config(object):
    API_ID = os.environ.get("API_ID", "7434892" )
    API_HASH = os.environ.get("API_HASH", "b645623710413894a1c0e084450876e2" )
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Rplay-video-merger-bot)
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001576361605" )
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001576361605" )
    DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
    TIME_GAP = int(os.environ.get("TIME_GAP", 5))
    MAX_VIDEOS = int(os.environ.get("MAX_VIDEOS", 5))
    STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME", "2ab52c1ef915e52f4ee8" )
    STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS", "zwgdM4xjXpsYPAP" )
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://rplayvcbot:1rplay2@cluster0.n7alv.mongodb.net/cluster0?retryWrites=true&w=majority" )
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 1990460616))

    START_TEXT = """
Hi Unkil, I am Video Merge Bot!
I can Merge Multiple Videos in One Video. Video Formats should be same.
Made by @AbirHasan2005
"""
    CAPTION = "Video Merged by @{}\n\nMade by @AbirHasan2005"
    PROGRESS = """
Percentage : {0}%
Done: {1}
Total: {2}
Speed: {3}/s
ETA: {4}
"""
