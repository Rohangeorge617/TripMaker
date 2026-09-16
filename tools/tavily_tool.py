from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def tavily_search(query):
    response = client.search(
        query = query,
        limit = 5
        )
    results = []

    for x, y in enumerate(response['results'], 1):
        title = y.get("title", "UNKNOWN")
        url = y.get("url", "UNKNOWN")
        snippet = y.get("content", "").strip()

        if len(snippet) > 400:
            snippet = snippet[:400].rsplit(" ", 1)[0] + "..."
        results.append(f"{x}. {title}\n   {url}\n  {snippet}")
    
    return "\n\n".join(results)


