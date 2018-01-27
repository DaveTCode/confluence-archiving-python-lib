from datetime import datetime
import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class ContentStatusDate:
    """
    This is a particular format of object that is returned over the JSON API
    when any date information is sent about the content status.
    """

    def __init__(self, json):  # type: (Dict[str, Any]) -> None
        self.long_info_as_html = json['longInfoAsHtml']  # type: str
        self.short_info_as_html = json['shortInfoAsHtml']  # type: str

        # TODO - Is this format dependent on the date settings of the confluence instance?
        self.date_formatted = datetime.strptime(json['dateFormatted'], '%b %d, %Y %H:%M')  # type: datetime

    def __str__(self):
        return self.short_info_as_html
