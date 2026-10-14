from pathlib import Path

API_ID= 37308659
API_HASH = 'b584091d4e41997b60fcaebfa298f4ed'
OWNER_ID = 6096638678
COMMAND_PATTERNS = [
    r'^\.startrp(?:\s+.*)?$',
    r'^\.unrp(?:\s+.*)?$',
    r'^\.list$',
    r'^\.clearrp$',
    r'^\.chatid$',
    r'^\.pickmeon$',
    r'^\.pickmeoff$',
    r'^\.photo(?:\s+.*)?$',
    r'^\.menu$',
    r'^\.id$',
]
BASE_DIR = Path(__file__).resolve().parent
PHRASES_FILE = BASE_DIR / "phrases.txt"
PHOTOS_DIR = BASE_DIR / "photos"

