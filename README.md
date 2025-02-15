## Reddit GenAI Trend Analysis with ReAct Agent Framework

**Author:** Amanda Milberg, Principal Solutions Engineer @ TitanML

[Presentation Slides](https://docs.google.com/presentation/d/1nar6_2VrRtR7l6HcanoUFAql9l8THs3Ob6LT2PCbYGw/edit?usp=sharing)

🎯 **Main Purpose**:

*   Analyzes posts from a specified subreddit (default: r/technology) to identify and summarize GenAI-related content.
*   Generates professional summaries of AI trends and developments, suitable for sharing with users who want to stay up-to-date on the latest trends.

🔑 **Key Components**:

1.  **Reddit API Integration:** Scrapes relevant posts from a given subreddit using the PRAW library.
2.  **LLM-powered Analysis:** Uses an LLM (via the NVIDIA API) to:
    *   Determine GenAI relevance based on the thread title.
    *   Summarize key themes and content for each relevant article.
    *   Generate a comprehensive trend analysis summary report.

📊 **Process Flow**:

1.  Fetches hot posts from the specified subreddit.
2.  Filters for GenAI-related content using the LLM.
3.  Extracts and summarizes article content using web scraping (BeautifulSoup).
4.  Creates a comprehensive trend analysis summary using the LLM.
5.  Generates a formatted report.

🛠️ **Technologies Used**:

*   PRAW (Reddit API client)
*   NVIDIA API (for the LLM)
*   BeautifulSoup (for web scraping)
*   python-dotenv (for environment variable management)
*   ReAct agent framework (for structured reasoning and action)

_Note: Requires Reddit API credentials and an NVIDIA API key._

## Getting Started

These instructions will guide you through setting up and running the Reddit GenAI Trend Analysis agent.

### Prerequisites

1.  **Python:** Ensure you have Python 3.7 or higher installed.
2.  **Reddit Account and API Credentials:**
    *   You need a Reddit account.
    *   Create a Reddit app:
        *   Go to [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps).
        *   Click "create app" or "create another app".
        *   Name it (e.g., "GenAITrendAnalysis").
        *   Choose the "script" type.
        *   Description: "Reddit trend analysis agent".
        *   Redirect URI: `http://localhost:8080` (this value doesn't matter for this script).
        *   Click "create app".
        *   Note your client ID (under the app name) and client secret.
3.  **NVIDIA API Key:**
    *   Obtain an API key for the NVIDIA API.  You can find information on how to do this on the NVIDIA developer website.

### Installation and Setup

1.  **Clone the Repository (if applicable):** If the code is in a Git repository, clone it:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Create a Virtual Environment (Recommended):**

    ```bash
    python3 -m venv .venv
    .venv\Scripts\Activate.ps1  # On Windows PowerShell
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
   If there is no requirements.txt, install them like so:
    ```bash
    pip install praw openai beautifulsoup4 python-dotenv
    ```

4.  **Create a .env file:**
    *   Create a file named `.env` in the `reddit-analyzer` directory (where `config.py` is located).
    *   Add the following lines, replacing the placeholders with your actual credentials:

    ```
    REDDIT_CLIENT_ID=your_reddit_client_id
    REDDIT_CLIENT_SECRET=your_reddit_client_secret
    REDDIT_USER_AGENT=GenAITrendAnalysis_by_u/your_reddit_username
    NVIDIA_API_KEY=your_nvidia_api_key
    ```

    *   **Important:** Replace `your_reddit_client_id`, `your_reddit_client_secret`, `your_reddit_username`, and `your_nvidia_api_key` with your actual credentials.  The `REDDIT_USER_AGENT` should be a unique string identifying your application; including your Reddit username is good practice.

### Running the Agent

1.  **Navigate to the directory:** Open a terminal or command prompt and navigate to the *outer* `reddit-analyzer` directory (the one that contains `main.py`).

2.  **Run the script:**

    ```bash
    python -m reddit_analyzer.main
    ```

    The `-m` flag ensures that the script is run as a module within the package.

3.  **View the Output:** The script will print its progress to the console, including the final report.

### Configuration

You can customize the agent's behavior by modifying the following variables in `reddit_analyzer/config.py`:

*   `SUBREDDIT`: The subreddit to analyze (default: "technology").
*   `NUM_POSTS`: The number of hot posts to fetch (default: 20).
*   `MODEL_NAME`: The NVIDIA LLM model to use (default: "meta/llama-3.1-405b-instruct").  Make sure this is a model you have access to.
*   `NVIDIA_BASE_URL`: The base URL for the NVIDIA API (default: "https://integrate.api.nvidia.com/v1").

### Troubleshooting

*   **`404 Client Error`:** Double-check your `NVIDIA_API_KEY`, `NVIDIA_BASE_URL`, and `MODEL_NAME` in `config.py` and `.env`.  Ensure you are using the correct model name and that your API key has access to it.
*   **Reddit API Errors:** Verify your Reddit API credentials in `.env`.  Make sure your Reddit app is correctly configured as a "script" type app.
*   **Other Errors:** The script includes retry logic and error handling, but if you encounter persistent issues, examine the error messages for clues.

## Why Use an Agent Framework?

*   Implements the ReAct (Reasoning + Acting) paradigm for more transparent and controlled AI behavior.
*   Provides explicit thinking and action steps for complex tasks.
*   Enables better debugging and monitoring of the AI's decision process.

🧠 **ReAct Framework Benefits**:

1.  **Reasoning Transparency:**
    *   The agent explicitly shows its thinking process before actions.
    *   Helps track decision-making logic.
    *   Makes debugging easier.

2.  **Structured Actions:**
    *   Clear separation between thinking and execution.
    *   Each action has defined inputs and outputs.
    *   Better error handling and recovery.

3.  **Process Monitoring:**
    *   Logs each step of the analysis pipeline.
    *   Tracks success/failure of individual components.
    *   Maintains a history of decisions and actions.

_The agent framework transforms what could be a simple script into a more robust, observable, and maintainable system for AI analysis. The agent approach provides better structure, transparency, and reliability for complex AI tasks compared to a simple main function._

## Why Self-Host? (This section can be adjusted based on your target audience)

🌟 **Key Benefits of Self-Hosting**

1.  **Cost-Effective Performance:**
    *   Reduced operational costs for high-volume processing.
    *   No ongoing API fees or usage limits.

2.  **Privacy & Data Control:**
    *   Complete control over data processing and storage.
    *   No data sharing with external providers.
    *   Compliance with internal security policies.
    *   Ability to air-gap for sensitive applications & sensitive data.

3.  **Deployment Flexibility:**
    *   Run locally on your own infrastructure.
    *   Scale resources based on actual needs.

## Why Deep Seek? (This section is less relevant now that we're using the NVIDIA API)

This section is no longer directly applicable since the code is configured to use the NVIDIA API. You could either remove this section entirely or replace it with a section explaining "Why NVIDIA API?" and list its benefits (e.g., ease of use, performance, etc.).  I'll provide a short replacement section:

## Why NVIDIA API?

1. **Ease of Use:** Simple and consistent API for accessing powerful LLMs.
2. **Performance:** Optimized for fast inference and high throughput.
3. **Scalability:** Easily scale your usage as needed.

_Note: In this demo, we are using the NVIDIA API to access a powerful LLM. The code is designed to be easily adaptable to other OpenAI-compatible APIs if needed._

