
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "500"))

DEVS = list(map(int, os.getenv("DEVS", "7763380474").split()))

API_ID = int(os.getenv("API_ID", "13777245"))

API_HASH = os.getenv("API_HASH", "625d95334e22b3566dd223bbccfc3223")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8008800937:AAFw3J-fr0Kcf5Y4ZlV6Pl489eI6ShTI3rs")

OWNER_ID = int(os.getenv("OWNER_ID", "7763380474"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002419662880").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://Ipanndongok:Ipanndongok@ipanndongok.bg7xf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", " -1002419662880"))
