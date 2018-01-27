from midori.archiving.models.contentstatus import ContentStatus
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def test_creation_valid_json():
    c = ContentStatus({
        'id': 9597470,
        'lastUpdated': {
            'dateFormatted': 'Jan 26, 2018 10:38',
            'shortInfoAsHtml': '<span title="Jan 26, 2018 10:38">yesterday at 10:38 AM</span> <small>(dat)</small>',
            'longInfoAsHtml': 'yesterday at 10:38 AM <small>(dat on Jan 26, 2018 10:38)</small>'},
        'lastViewed': {
            'dateFormatted': 'Jan 25, 2018 10:05',
            'shortInfoAsHtml': '<span title="Jan 25, 2018 10:05"><b>2</b> days ago</span> <small>(TJW2)</small>',
            'longInfoAsHtml': '<b>2</b> days ago <small>(TJW2 on Jan 25, 2018 10:05)</small>'
        },
        'title': 'A',
        'url': '/display/AS/A+S',
        'hasChildren': True,
        'isHomePage': False,
        'homePage': False,
        'status': {
            'code': 'excluded',
            'summary': 'Excluded',
            'description': 'This page is excluded from lifecycle checks',
            'subDescription': 'by appadmin'}
    })

    assert str(c) == 'A'
    assert c.id == 9597470
    assert c.last_updated.date_formatted.year == 2018
    assert c.last_updated.date_formatted.month == 1
    assert c.last_updated.date_formatted.day == 26
    assert str(c.last_updated) == '<span title="Jan 26, 2018 10:38">yesterday at 10:38 AM</span> <small>(dat)</small>'
