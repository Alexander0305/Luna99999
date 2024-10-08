# Configuration file

# Database settings
DB_FILE = 'luna.db'
DB_TABLE = 'conversations'

# NLP settings
NLP_MODEL = 'rasa'
NLP_LANGUAGE = 'en'

# Speech recognition settings
SR_ENGINE = 'google'
SR_LANGUAGE = 'en-US'

# Voice output settings
VOICE_OUTPUT = True
TTS_ENGINE = 'gtts'

# User authentication settings
AUTH_ENABLED = True
AUTH_USERNAME = 'admin'
AUTH_PASSWORD = 'password'

# Logging settings
LOGGING_ENABLED = True
LOG_FILE = 'luna.log'

# Install required libraries if missing
required_libraries = ['nltk', 'rasa', 'speech_recognition', 'sqlite3', 'gtts', 'playsound']
for lib in required_libraries:
    try:
        __import__(lib)
    except ImportError:
        print(f"Installing {lib}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
