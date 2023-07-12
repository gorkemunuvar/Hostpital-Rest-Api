from ..enums import Lang


def get_lang(params: dict) -> Lang:
    """Returns which languages client wants from the db
       for given query parameter <lang>"""
    if params.__contains__('lang'):
        if params['lang'].lower() == 'kk':
            return Lang.KK
    return Lang.RU
