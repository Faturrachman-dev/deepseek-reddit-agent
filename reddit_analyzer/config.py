import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

REDDIT_CREDS = {
    "client_id": os.getenv("REDDIT_CLIENT_ID"),
    "client_secret": os.getenv("REDDIT_CLIENT_SECRET"),
    "user_agent": os.getenv("REDDIT_USER_AGENT"),
}

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")
NVIDIA_BASE_URL = "https://integrate.api.nvidia.com/v1"  # Ensure base URL is correct
MODEL_NAME = "meta/llama-3.1-405b-instruct"  # Use the correct model name
SUBREDDIT = "technology"
NUM_POSTS = 20 