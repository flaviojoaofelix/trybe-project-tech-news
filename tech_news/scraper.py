# Requisito 1
import requests
from requests.exceptions import ConnectTimeout, HTTPError
from ratelimit import limits, sleep_and_retry
from parsel import Selector

config = {
    "requests": {
        "headers": {"user-agent": "Fake user-agent"},
        "timeout": 3,
        "rate_limit": {
            "calls": 1,
            "period": 1,
        },
    },
    "selectors": {"updates": "h2.entry-title a::attr(href)"},
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
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)

    return selector.css(config["selectors"]["updates"]).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
