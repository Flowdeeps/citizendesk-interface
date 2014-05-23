from .entities.reports import entity as reports

settings = {
    'MONGO_DBNAME': 'citizendesk',
    'X_DOMAINS': "*",
    'X_HEADERS': "Content-Type",

    'DOMAIN': {
        'reports': reports,
        'twt_streams': {},
        'twt_filters': {},
        'twt_oauths': {},
        'steps': {},
        'settings-bool': {},
        'settings-int': {},
        'settings-string': {}
    }
}
