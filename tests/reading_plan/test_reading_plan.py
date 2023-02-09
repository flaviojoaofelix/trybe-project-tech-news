from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
from tests.assets.news import NEWS as mocked_news
import pytest

config = {
    "reading": {
        "time": 2,
        "invalid_time": -1,
        "invalid_time_message": "Valor 'available_time'"
        " deve ser maior que zero",
    }
}

# for reading time = 2
mocked_readable = [
    ("noticia_0", 2),
    ("Notícia bacana 2", 1),
    ("noticia_3", 1),
    ("noticia_4", 1),
    ("noticia_5", 1),
    ("noticia_6", 1),
]

# for reading time = 2
mocked_unreadable = [
    ("Notícia bacana", 4),
    ("noticia_7", 7),
    ("noticia_8", 8),
    ("noticia_9", 5),
]


def test_reading_plan_group_news(mocker):
    mocker.patch(
        "tech_news.analyzer.reading_plan.find_news", return_value=mocked_news
    )
    rps_result = ReadingPlanService.group_news_for_available_time(
        config["reading"]["time"]
    )

    assert len(rps_result["readable"]) == len(mocked_readable)
    assert len(rps_result["unreadable"]) == len(mocked_unreadable)

    with pytest.raises(
        ValueError, match=config["reading"]["invalid_time_message"]
    ):
        ReadingPlanService.group_news_for_available_time(
            config["reading"]["invalid_time"]
        )
