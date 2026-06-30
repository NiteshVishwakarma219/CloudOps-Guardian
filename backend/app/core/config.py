from dotenv import load_dotenv
import os

load_dotenv()

class Settings:

    AWS_REGION = os.getenv(
        "AWS_REGION"
    )

    DATABASE_URL = os.getenv(
        "DATABASE_URL"
    )

settings = Settings()