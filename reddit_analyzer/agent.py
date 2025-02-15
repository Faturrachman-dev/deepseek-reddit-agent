import praw
from openai import OpenAI
from .clients import initialize_reddit_client, initialize_llm_client
from .utils import extract_article_content
from .config import SUBREDDIT, NUM_POSTS, MODEL_NAME
import json

class RedditAIAnalysisAgent:
    """Agent to analyze Reddit trends using ReAct reasoning and OpenAI LLM"""

    def __init__(self):
        self.reddit = initialize_reddit_client()
        self.llm = initialize_llm_client()
        self.thought_history = []

        # Check if initialization was successful
        if self.reddit is None or self.llm is None:
            raise ValueError("Failed to initialize Reddit or LLM client. Check credentials.")

    def think(self, thought: str):
        """Adds a thought to the thought history."""
        self.thought_history.append(thought)
        print(f"🤔 THINKING: {thought}")

    def act(self, action: str, result: str):
        """Records an action and its result."""
        self.thought_history.append(f"🎯 ACTION: {action}\n📝 RESULT: {result}")
        print(f"🎯 ACTION: {action}\n📝 RESULT: {result}")

    def analyze_genai_relevance(self, title: str) -> dict:
        """Analyze if title is GenAI-related using LLM, returning JSON directly."""

        system_prompt = """You are a helpful AI assistant. Determine if the given article title relates to Generative AI.

        Return a JSON object in the following format:
        {
            "is_genai_related": true/false,
            "relevance_type": "direct/indirect/none",
            "reasoning": "Your reasoning here..."
        }
        """
        try:
            response = self.llm.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": title}
                ],
                temperature=0.2,
                top_p=0.7,
                max_tokens=200
            )
            response_text = response.choices[0].message.content

            # Extract JSON by finding braces
            start = response_text.find('{')
            end = response_text.rfind('}') + 1  # +1 to include the closing brace
            if start == -1 or end == -1:
                raise json.JSONDecodeError("No valid JSON object found", response_text, 0)
            json_str = response_text[start:end]
            json_data = json.loads(json_str)

        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON returned from LLM: {response_text}\nError Detail: {e}")
            json_data = {"is_genai_related": False, "relevance_type": "none", "reasoning": ""}
        except Exception as e: # Catch API errors here
            print(f"Error in GenAI relevance: {e}")
            json_data = {"is_genai_related": False, "relevance_type": "none", "reasoning": ""}

        return json_data # Return the dictionary directly

    def summarize_trend(self, title: str, content: str) -> str:
        """Summarize the content of a GenAI-related trend."""
        if not content:
            return "Error: Could not retrieve article content."

        prompt = f"""Summarize the following article, focusing on aspects related to Generative AI:\n
Title: {title}\n
Content:\n{content[:4000]}...\n  
""" #limit the context length

        try:
            response = self.llm.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.4,
                max_tokens=500
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error during summarization: {e}")
            return "Error: Could not summarize the article."

    def create_email_summary(self, trends_list: list) -> str:
        """Create a high-level summary suitable for an email."""
        if not trends_list:
            return "No GenAI trends found in the current batch."

        summary_prompt = "Create a concise summary of the following Generative AI trends:\n\n"
        for trend in trends_list:
            summary_prompt += f"- **{trend['title']}**: {trend['relevance_reasoning']}\n  Summary: {trend['summary']}\n\n"

        summary_prompt += "Provide an overall assessment of the current GenAI trends."

        try:
            response = self.llm.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "user", "content": summary_prompt}
                ],
                temperature=0.3,
                max_tokens=1000
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error creating email summary: {e}")
            return "Error: Could not create email summary."

    def get_reddit_trends(self):
        """Fetches and analyzes Reddit trends."""
        self.think(f"Fetching Reddit trends for analysis")
        subreddit = self.reddit.subreddit(SUBREDDIT)
        posts = list(subreddit.hot(limit=NUM_POSTS))
        print(f"📊 Fetching posts from r/{SUBREDDIT}...")
        self.act(f"Fetching {NUM_POSTS} most popular threads:", "")

        genai_trends = []
        for post in posts:
            print("=" * 50)
            print(post.title)

            relevance = self.analyze_genai_relevance(post.title)

            if relevance["is_genai_related"]:
                print(f"GenAI Relevance: {relevance['is_genai_related']}")
                self.act(f"📖 Reading Article Details at {post.url}", "")
                content = extract_article_content(post.url)

                if content:
                    summary = self.summarize_trend(post.title, content)
                    trend_data = {
                        "title": post.title,
                        "url": post.url,
                        "summary": summary,
                        "relevance_reasoning": relevance["reasoning"]
                    }
                    genai_trends.append(trend_data)
                    print(f"✅ Summarization complete for {len(genai_trends)} trends")
            else:
                print(f"GenAI Relevance: {relevance['is_genai_related']}")

        return genai_trends

    def run(self):
        """Main agent execution loop."""
        print("🤖 Initializing Reddit AI Analysis Agent...\n")
        print("🚀 STARTING REDDIT AI TREND ANALYSIS")
        print("=" * 50)

        if not self.reddit or not self.llm:
            print("❌ Initialization failed. Check your credentials and API keys.")
            return

        self.think("Starting Reddit AI trend analysis")
        print("📡 INITIALIZING CLIENTS...")

        genai_trends = self.get_reddit_trends()

        if genai_trends:
            self.think("Creating high level email summary for overall GenAI trends found")
            final_report = self.create_email_summary(genai_trends)
            self.act("Create analysis", f"✅ Analysis complete for {len(genai_trends)} trends")
        else:
            self.act("Analyze trends", "⚠️ No relevant trends found")
            final_report = "No GenAI trends found in the current batch."

        print("=" * 50)
        self.think("Analysis complete, final report generated")
        print("\n✅ ANALYSIS COMPLETE")
        print("=" * 50)
        print("\nFinal report has been generated in the response.")
        return final_report 