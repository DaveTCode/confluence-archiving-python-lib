import logging
from midori.archiving.models.contentstatus import ContentStatus
import requests
from typing import List, Tuple

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class ArchivingClient:
    """
    External interface into this library, all calls should be made through
    an instance of this class.

    Note: This class should be used in a context manager (e.g.
    ```with Confluence(...) as c:```
    """

    def __init__(self, base_url, basic_auth):  # type: (str, Tuple[str, str]) -> None
        """
        :param base_url: The URL where the confluence web app is located. e.g. https://mysite.mydomain/confluence
        :param basic_auth: A tuple containing a username/password pair that
        can log into confluence.
        """
        self._base_url = base_url
        self._basic_auth = basic_auth
        self._api_base = '{}/rest/archiving/1.0'.format(self._base_url)
        self._client = None  # type: requests.Session

    def __enter__(self):
        self._client = requests.session()
        self._client.auth = self._basic_auth

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._client:
            self._client.close()

    def get_page_content_status(self, page_id):
        # type: (int) -> ContentStatus
        """
        Get the status of a single page on a confluence instance with the
        archiving plugin installed.

        :param page_id: A confluence page id.
        :return: The status of that page as seen by the archiving plugin.
        """
        url = '{}/content-status/{}'.format(self._api_base, page_id)

        if self._client:
            result = self._client.get(url).json()
        else:
            result = requests.get(url, auth=self._basic_auth).json()

        return ContentStatus(result)

    def get_page_children_content_status(self, page_id):
        # type: (int) -> List[ContentStatus]
        """
        Get the status of all child pages of a given page on a confluence
        instance with the archiving plugin installed.

        :param page_id: A confluence page id.
        :return: The status of all pages as seen by the archiving plugin.
        """
        url = '{}/content-status/{}/children'.format(self._api_base, page_id)

        if self._client:
            results = self._client.get(url).json()
        else:
            results = requests.get(url, auth=self._basic_auth).json()

        return [ContentStatus(r) for r in results]

    def get_content_status_top_level_space_pages(self, space_key):
        # type: (str) -> List[ContentStatus]
        """
        For a given space this returns the content status of all pages below it.

        :param space_key: A confluence space key
        :return: The content status of the top level pages in that space.
        """
        url = '{}/content-status/space/{}/children'.format(self._api_base, space_key)

        if self._client:
            results = self._client.get(url).json()
        else:
            results = requests.get(url, auth=self._basic_auth).json()

        return [ContentStatus(r) for r in results]

    def __str__(self):
        return self._api_base
