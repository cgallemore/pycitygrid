class Region(object):
    type = None
    name = None
    latitude = None
    longitude = None
    default_radius = None

    def __init__(self, data):
        self.type = data.get('type', '')
        self.name = data.get('name', '')
        self.latitude = data.get('latitude')
        self.longitude = data.get('longitude')
        self.default_radius = data.get('default_radius')


class Address(object):
    street = None
    city = None
    state = None
    postal_code = None

    def __init__(self, data):
        self.street = data.get('street', '')
        self.city = data.get('city', '')
        self.state = data.get('state', '')
        self.postal_code = data.get('postal_code', '')


class Expansion(object):
    count = None
    uri = None

    def __init__(self, data):
        self.count = data.get('count', None)
        self.uri = data.get('uri', None)


class Tag(object):
    id = None
    name = None
    primary = False

    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')
        self.primary = data.get('primary', False)


class Location(object):
    id = None
    featured = None
    name = None
    address = None
    neighborhood = None
    latitude = None
    longitude = None
    distance = None
    image = None
    phone_number = None
    fax_number = None
    rating = None
    tagline = None
    profile = None
    website = None
    has_video = None
    has_offers = None
    offers = '' #TODO Not sure if this is a list or not.
    user_review_count = None
    sample_categories = None
    impression_id = None
    expansion = None
    tags = None
    public_id = None

    def __init__(self, data):
        self.id = data.get('id', '')
        self.featured = data.get('featured')
        self.name = data.get('name', '')
        self.address = Address(data.get('address'))
        self.neighborhood = data.get('neighborhood', '')
        self.latitude = data.get('latitude', '')
        self.longitude = data.get('longitude', '')
        self.distance = data.get('distance', '')
        self.image = data.get('image', '')
        self.phone_number = data.get('phone_number', '')
        self.fax_number = data.get('fax_number', '')
        self.rating = data.get('rating', '')
        self.tagline = data.get('tagline', '')
        self.profile = data.get('profile', '')
        self.website = data.get('website', '')
        self.has_video = data.get('has_video', '')
        self.has_offers = data.get('has_offers', '')
        self.offers = data.get('offers', '')
        self.user_review_count = data.get('user_review_count', '')
        self.sample_categories = data.get('sample_categories', '')
        self.impression_id = data.get('impression_id', '')
        self.expansion = Expansion(data.get('expansion'))
        self.tags = [Tag(_t) for _t in data.get('tags', [])]
        self.public_id = data.get('public_id', '')

class SearchResult(object):
    rpp = None
    page = None
    last_hit = None
    first_hit = None
    total_hits = None
    query_id = None
    uri = None
    did_you_mean = None
    regions = []
    locations = None
    histograms = None

    def __init__(self, data):
        result = data.get('results')
        self.rpp = result.get('rpp')
        self.page = result.get('page')
        self.last_hit = result.get('last_hit')
        self.first_hit = result.get('first_hit')
        self.total_hits = result.get('total_hits')
        self.query_id = result.get('query_id')
        self.uri = result.get('uri')
        self.did_you_mean = result.get('did_you_mean', '')
        self.regions = [Region(_r) for _r in result.get('regions', [])]
        self.locations = [Location(_l) for _l in result.get('locations', [])]