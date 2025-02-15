from reddit_analyzer.agent import RedditAIAnalysisAgent

def main():
    """Main function to run the Reddit AI Analysis Agent."""
    agent = RedditAIAnalysisAgent()
    result = agent.run()
    print(result)

if __name__ == "__main__":
    main() 