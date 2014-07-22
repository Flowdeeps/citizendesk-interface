from .entities.reports import entity as reports
from .entities.twt_searches import entity as twt_searches
from .entities.steps import entity as steps
from .entities.settings_bool import entity as settings_bool
from .entities.settings_int import entity as settings_int
from .entities.settings_string import entity as settings_string
from .entities.coverages import entity as coverages

settings = {
    'SERVER_NAME': 'http://cd2.sourcefabric.net/citizendesk-interface',
    'MONGO_DBNAME': 'citizendesk',
    'X_DOMAINS': "*",
    'X_HEADERS': "Content-Type,If-Match,Authorization",
    'XML': False,
    'BANDWIDTH_SAVER': False,
    'CACHE_CONTROL': 'max-age=0, no-cache',
    'CACHE_EXPIRES': 0,
    'DATE_FORMAT': '%Y-%m-%dT%H:%M:%S+0000', # Superdesk wants this format
    'PAGINATION_DEFAULT': 100,
    'PAGINATION_LIMIT': 200,

    'DOMAIN': {
        'reports': reports,
        'twt_streams': {},
        'twt_filters': {},
        'twt_oauths': {},
        'twt-searches': twt_searches,
        'steps': steps,
        'settings-bool': {},
        'settings-int': {},
        'settings-string': {},
        'citizen_aliases': {},
        'settings-bool': settings_bool,
        'settings-int': settings_int,
        'settings-string': settings_string,
        'coverages': coverages,
    }
}
