from fastapi import APIRouter, Depends
import feedparser
import re

router = APIRouter(tags=["Intelligence"])

def clean_html(text):
    return re.sub("<.*?>", "", text)

@router.get("/world-news", summary="Get Top Global News")
def world_news():
    url = "https://feeds.bbci.co.uk/news/world/rss.xml"
    feed = feedparser.parse(url)

    top = feed.entries[0]

    summary = clean_html(top.summary)

    return {
        "title": top.title,
        "summary": summary[:300],
        "link": top.link
    }