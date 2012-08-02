from citygrid import CityGridException
import requests

class CityGrid(object):
    endpoint = 'http://api.citygridmedia.com/content/places/v2'
    publisher = None

    def __init__(self, publisher):
        self.publisher = publisher

    def _get(self, url, params):
        return requests.get(url, params=params)

class Places(CityGrid):
    def __init__(self, publisher):
        super(Places, self).__init__(publisher)
        self.where_endpoint = '%s/search/where'
        self.latlon_endpoint = '%s/searh/latlon'

    def where(self, where, format_='json', **kwargs):
        if 'type' or 'what' not in kwargs:
            raise CityGridException('Must provide one of type_ or what.')

        return self._get(self.where_endpoint, dict(where=where, format=format_,
                                                   **kwargs))

    def latlon(self, lat, long, format_='json', **kwargs):
        if 'type' or 'what' not in kwargs:
            raise CityGridException('Must provide one of type_ or what.')

        return self._get(self.latlon_endpoint, dict(lat=lat, lon=long,
                                                    format=format_, **kwargs))