from midori.archiving.models.contentstatusdate import ContentStatusDate
import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class ContentStatus:
    """
    Represents the state of a piece of content in confluence as understood
    by the archiving plugin.
    """

    def __init__(self, json):  # type: (Dict[str, Any]) -> None
        self.id = json['id']  # type: int

        if 'title' in json:
            self.title = json['title']  # type: str

        if 'url' in json:
            self.url = json['url']  # type: str

        if 'hasChildren' in json:
            self.has_children = json['hasChildren']  # type: bool

        if 'isHomePage' in json:
            self.is_home_page = json['isHomePage']  # type: bool

        self.last_updated = ContentStatusDate(json['lastUpdated'])  # type: ContentStatusDate
        self.last_viewed = ContentStatusDate(json['lastViewed'])  # type: ContentStatusDate
        self.status_code = json['status']['code']
        self.status_summary = json['status']['summary']
        self.status_description = json['status']['description']
        self.status_sub_description = json['status']['subDescription']

    def __str__(self):
        return self.title
