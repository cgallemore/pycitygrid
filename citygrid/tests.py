import json
import os
import unittest
from citygrid.models import SearchResult

class ModelTests(unittest.TestCase):
    def setUp(self):
        super(ModelTests, self).setUp()

        path = os.path.join(os.getcwd(), 'citygrid', 'places_sample.json')
        with open(path) as f:
            self.data = f.read()

    def test_search_result(self):
        result = SearchResult(json.loads(self.data))
        self.assertEquals(result.rpp, 20)
        self.assertEquals(result.page, 1)
        self.assertEquals(result.last_hit, 20)
        self.assertEquals(result.first_hit, 1)
        self.assertEquals(result.total_hits, 22)
        self.assertIsNone(result.query_id)
        self.assertEquals(result.uri, 'http://api.citygridmedia.com/search/places/v2/search/where?has_offers=false&type=movietheater&format=json&page=1&rpp=20&histograms=false&where=90045&publisher=test&region_type=circle')
        self.assertIsNone(result.did_you_mean)
        self.assertEquals(len(result.regions), 1)
        self.assertEquals(len(result.locations), 20)

        # Validate region
        region = result.regions[0]
        self.assertEquals(region.type, 'postal_code')
        self.assertEquals(region.name, '90045')
        self.assertEquals(region.latitude, 33.953182)
        self.assertEquals(region.longitude, -118.400197)
        self.assertEquals(region.default_radius, 3.28)

        # Validate one location
        location = result.locations[0]
        self.assertEquals(location.id, 11538789)
        self.assertFalse(location.featured)
        self.assertEquals(location.name, 'The Bridge Cinema De Lux')
        self.assertEquals(location.address.street, '6081 Center Drive')
        self.assertEquals(location.address.city, 'Los Angeles')
        self.assertEquals(location.address.state, 'CA')
        self.assertEquals(location.address.postal_code, '90045')
        self.assertEquals(location.neighborhood, 'West LA, Westchester')
        self.assertEquals(location.latitude, 33.9781)
        self.assertEquals(location.longitude, -118.3928)
        self.assertIsNone(location.distance)
        self.assertIsNone(location.image)
        self.assertEquals(location.phone_number, '3105683375')
        self.assertIsNone(location.fax_number)
        self.assertEquals(location.rating, 8)
        self.assertIsNone(location.tagline)
        self.assertEquals(location.profile, 'http://losangeles.citysearch.com/profile/11538789/los_angeles_ca/the_bridge_cinema_de_lux.html')
        self.assertIsNone(location.website)
        self.assertFalse(location.has_video)
        self.assertFalse(location.has_offers)
        self.assertIsNone(location.offers)
        self.assertEquals(location.user_review_count, 39)
        self.assertEquals(location.sample_categories, 'IMAX Theaters, Movie Theaters, MasterCard, Visa, Gift Certificate')
        self.assertEquals(location.impression_id, '000b000000d25b68f605994d2d918c0d6f89c3568b')
        self.assertIsNone(location.expansion.count)
        self.assertIsNone(location.expansion.uri)
        self.assertEquals(location.public_id, 'the-bridge-cinema-de-lux-los-angeles')
        self.assertEquals(len(location.tags), 5)

        # Validate one tag
        tag = location.tags[0]
        self.assertEquals(tag.id, 162)
        self.assertEquals(tag.name, 'IMAX Theaters')
        self.assertFalse(tag.primary)

