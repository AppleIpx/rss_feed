import feedparser

from rss_feed.post.utils.actions_with_db import delete_all_posts_from_db, save_posts_to_db
from rss_feed.post.utils.validaters import validate_text, validate_date


class RssReader:
    def __init__(self, rss_url):
        self.rss_url = rss_url

    def fetch_entries(self):
        """Считывает записи из RSS-ленты."""
        feed = feedparser.parse(self.rss_url)
        return feed.entries


def prepare_data_for_db() -> None:
    """Function that prepares data for db"""

    # rss_url = "https://www.google.ru/alerts/feeds/11383541103172355775/14671559717323292828"
    rss_url = "https://www.google.ru/alerts/feeds/11383541103172355775/7429273892975475712" # dogs

    rss_reader = RssReader(rss_url)
    delete_all_posts_from_db()

    entries = rss_reader.fetch_entries()
    for entry in  entries:
        news_item = {
            'name': validate_text(entry.title),
            'short_description': validate_text(text=entry.summary),
            "link": entry.link,
            'created_at': validate_date(input_date=entry.get('published', '')),
            'updated_at': validate_date(input_date=entry.get('updated', '')),
        }
        save_posts_to_db(data=news_item)
