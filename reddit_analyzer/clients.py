import praw
from openai import OpenAI
from .config import REDDIT_CREDS, NVIDIA_API_KEY, NVIDIA_BASE_URL
from .utils import retry

@retry
def initialize_reddit_client():
    """Initializes the Reddit client, retrying on failure."""
    try:
        reddit = praw.Reddit(**REDDIT_CREDS)
        # Test the connection *after* creating the object:
        try:
            reddit.user.me()  # This will raise an exception if auth fails
        except praw.exceptions.PRAWException as e:
            print(f"Reddit authentication failed: {e}")
            return None  # Return None if authentication fails
        return reddit
    except Exception as e:
        print(f"Error initializing Reddit client: {e}")
        return None

@retry
def initialize_llm_client():
    """Initializes the LLM client with retries."""
    try:
        llm = OpenAI(
            base_url=NVIDIA_BASE_URL,
            api_key=NVIDIA_API_KEY
        )
        return llm
    except Exception as e:
        print(f"Error initializing LLM client: {e}")
        return None 