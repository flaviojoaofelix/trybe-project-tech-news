# Requisito 1
import requests
from requests.exceptions import ConnectTimeout, HTTPError
from ratelimit import limits, sleep_and_retry
from parsel import Selector
import re

config = {
    "requests": {
        "headers": {"user-agent": "Fake user-agent"},
        "timeout": 3,
        "rate_limit": {
            "calls": 1,
            "period": 1,
        },
    },
    "selectors": {
        "updates": "h2.entry-title a::attr(href)",
        "next_page_link": "a.next.page-numbers::attr(href)",
        "news": {
            "url": "div::attr(data-share-url)",
            "title": "h1.entry-title::text",
            "timestamp": "li.meta-date::text",
            "writer": "a.url.fn::text",
            "reading_time": "li.meta-reading-time::text",
            "summary": "string(//div[has-class('entry-content')]//p[1])",
            "category": "a.category-style > span.label::text",
        },
    },
}


@sleep_and_retry
@limits(
    calls=config["requests"]["rate_limit"]["calls"],
    period=config["requests"]["rate_limit"]["calls"],
)
def fetch(url: str) -> str:
    try:
        response = requests.get(
            url,
            headers=config["requests"]["headers"],
            timeout=config["requests"]["timeout"],
        )
        response.raise_for_status()
    except (ConnectTimeout, HTTPError, requests.ReadTimeout):
        return None

    return response.text


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)

    return selector.css(config["selectors"]["updates"]).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)

    return selector.css(config["selectors"]["next_page_link"]).get()


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)

    return {
        "url": selector.css(config["selectors"]["news"]["url"]).get(),
        "title": selector.css(config["selectors"]["news"]["title"])
        .get()
        .strip(),
        "timestamp": selector.css(
            config["selectors"]["news"]["timestamp"]
        ).get(),
        "writer": selector.css(config["selectors"]["news"]["writer"]).get(),
        "reading_time": int(
            re.search(
                r"\d+",
                selector.css(
                    config["selectors"]["news"]["reading_time"]
                ).get(),
            ).group()
        ),
        "summary": selector.xpath(config["selectors"]["news"]["summary"])
        .get()
        .strip(),
        "category": selector.css(
            config["selectors"]["news"]["category"]
        ).get(),
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
