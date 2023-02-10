from tech_news.database import db


# Requisito 10
def top_5_categories():
    data = list(
        db.news.aggregate(
            [
                {"$group": {"_id": "$category", "count": {"$sum": 1}}},
                {"$sort": {"count": -1, "_id": 1}},
                {"$limit": 5},
            ]
        )
    )

    return [item["_id"] for item in data]
