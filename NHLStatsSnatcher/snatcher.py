import requests

class Snatcher:
    def __init__(self):
        self.base_url = "https://api-web.nhle.com/v1/"
        self.rest_url = "https://api.nhle.com/stats/rest/en/"
    
    def construct_url(self, endpoint, base=True):
        """Construct the full URL for the given endpoint."""
        if not base:
            url = self.rest_url
        else:
            url = self.base_url
        return f"{url}{endpoint}"

    def get_data(self, endpoint, base=True):
        """Fetch data from the given endpoint."""
        url = self.construct_url(endpoint, base=base)
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError if the response contains an HTTP error status code.
        return response.json()

