#This program creates an MCP server that lets an AI search videos from the freeCodeCamp YouTube channel.
from fastmcp import FastMCP
#Tool to read YouTube channel data
import feedparser
import requests

#Create MCP server
mcp = FastMCP(name="MCP server for feed searcher")

#Register a tool
@mcp.tool()
#how many videos to return
def fcc_youtube_search(query: str, max_result: int = 3):
    """Search freecodecamp youtube channel"""
    #Read freeCodeCamp YouTube feed
    url = "https://www.youtube.com/feeds/videos.xml?channel_id=UC8butISFwT-Wl7EV0hUK0BQ"
    
    #feedparser.parse(url) this did not work. YouTube stores list as an XML file.
    # xml = requests.get(url).text - download file ourselves. 
    xml = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=20).text
    #feed = feedparser.parse(xml) - d the file I already downloaded
    feed = feedparser.parse(xml)

    #Empty list to store matching videos
    results = []
    #Converts search text to lowercase
    q = query.lower()

    #Goes through each video in the channel. feed.entries is your list. entry = it is just a variable use to loop through videos.
    for entry in feed.entries:
        #read video title
        title = entry.get("title", "")
        #Does this video title contain the search word
        if q in title.lower():
            results.append({"title": title, "url": entry.get("link", "")})
        if len(results) >= max_result:
            #unlikely to occure
            break

    return results or [{"message": "No video found"}]

if __name__ == "__main__":
    mcp.run(transport="http")
