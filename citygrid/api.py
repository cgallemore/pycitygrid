import json
from citygrid.models import SearchResult
import requests
from citygrid import CityGridException

class CityGrid(object):
    endpoint = 'http://api.citygridmedia.com/content/places/v2'
    publisher = None

    def __init__(self, publisher):
        self.publisher = publisher

    def _get(self, url, params):
        params = dict(format='json', publisher=self.publisher, **params)
        _r = requests.get(url, params=params)
        return SearchResult(json.loads(_r.text))

class Places(CityGrid):
    def __init__(self, publisher):
        super(Places, self).__init__(publisher)
        self.where_endpoint = '%s/search/where' % self.endpoint
        self.latlon_endpoint = '%s/searh/latlon' % self.endpoint

    def where(self, where, **kwargs):
        if 'type' not in kwargs and 'what' not in kwargs:
            raise CityGridException('Must provide one of type_ or what.')

        return self._get(self.where_endpoint, dict(where=where, **kwargs))

    def latlon(self, lat, long, **kwargs):
        if 'type' or 'what' not in kwargs:
            raise CityGridException('Must provide one of type_ or what.')

        return self._get(self.latlon_endpoint, dict(lat=lat, lon=long, **kwargs))