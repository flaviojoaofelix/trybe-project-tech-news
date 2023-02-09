# Requisito 7
from tech_news.database import search_news


def search_by_title(title: str):
    query = {"title": {"$regex": title, "$options": "i"}}

    return [(item["title"], item["url"]) for item in search_news(query)]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
