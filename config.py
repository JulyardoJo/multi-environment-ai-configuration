from dotenv import load_dotenv
import os


# Load configuration dari file .env
load_dotenv()


# Membaca environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

BASE_URL = os.getenv("BASE_URL")

MODEL_NAME = os.getenv("MODEL_NAME")

ENVIRONMENT = os.getenv("ENVIRONMENT")


# Validation configuration

if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY belum dikonfigurasi."
    )


if not BASE_URL:
    raise ValueError(
        "BASE_URL belum dikonfigurasi."
    )


if not MODEL_NAME:
    raise ValueError(
        "MODEL_NAME belum dikonfigurasi."
    )


if not ENVIRONMENT:
    raise ValueError(
        "ENVIRONMENT belum dikonfigurasi."
    )