import logging
import json

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2


class Client(object):

    """Netuitive Rest Api Client for agent data ingest.

    Posts Element data to Netuitive Cloud

    Args:
        url: The URL for the Netuitive Cloud API
        api_keys: The API key provided by your Netuitive Cloud Data Source

    """

    def __init__(self, url='https://api.app.netuitive.com/ingest',
                 api_key='apikey'):

        if url.endswith('/'):
            url = url[:-1]

        self.url = url
        self.api_key = api_key
        self.dataurl = self.url + '/' + self.api_key
        self.eventurl = self.dataurl.replace('/ingest/', '/ingest/events/', 1)

    # these should probably return true on success

    def post(self, element):
        payload = json.dumps([element], default=lambda o: o.__dict__)
        logging.debug(payload)
        try:
            headers = {'Content-Type': 'application/json'}
            request = urllib2.Request(
                self.dataurl, data=payload, headers=headers)
            resp = urllib2.urlopen(request)
            logging.debug("Response code: %d", resp.getcode())
            resp.close()

            return(True)

        except Exception as e:
            logging.exception(
                'error posting payload to api ingest endpoint (%s): %s',
                self.dataurl, e)

    def post_event(self, event):
        payload = json.dumps([event], default=lambda o: o.__dict__)
        logging.debug(payload)
        try:
            headers = {'Content-Type': 'application/json'}
            request = urllib2.Request(
                self.eventurl, data=payload, headers=headers)
            resp = urllib2.urlopen(request)
            logging.debug("Response code: %d", resp.getcode())
            resp.close()

            return(True)

        except Exception as e:
            logging.exception(
                'error posting payload to api ingest endpoint (%s): %s',
                self.eventurl, e)
