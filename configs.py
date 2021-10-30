import os


class Config(object):
    API_ID = os.environ.get("API_ID", "6701181" )
    API_HASH = os.environ.get("API_HASH", "9df7dd72e31ae336edf34dfdf406b14b" )
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    SESSION_NAME = os.environ.get("SESSION_NAME", "video-merger-bot" )
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1356770286" )
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1356770286" )
    DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
    TIME_GAP = int(os.environ.get("TIME_GAP", 5))
    MAX_VIDEOS = int(os.environ.get("MAX_VIDEOS", 15))
    STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME", "2ab52c1ef915e52f4ee8" )
    STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS", "zwgdM4xjXpsYPAP" )
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://rplayvcbot:1rplay2@cluster0.n7alv.mongodb.net/cluster0?retryWrites=true&w=majority" )
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 1167961858))

    START_TEXT ="""
Hi 👋, I am **COBRA MOVIES** `Video Merge` @videomerge842_bot!
I can Merge Multiple Videos in One Video. Video Formats should be same.
Made by @BullMovies_Team 
"""
    CAPTION = "Video Merged by @{}\n\nMade by @BullMovies_Team"
    PROGRESS = """
Percentage : {0}%
Done: {1}
Total: {2}
Speed: {3}/s
ETA: {4}
"""
