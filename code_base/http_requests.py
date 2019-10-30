#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests
import sys


class SampleHTTPRequests(object):
    """@description: class with implementations of HTTP requests for test project
       @author: vlipinskyy"""
    # API endpoints:
    API_URL = "https://marketingapi.wheelsup.com/api/initial-data/"

    # Params dict, critical for successful API call
    PARAMS = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) "
                            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}

    def __init__(self):
        self.http_requests = requests

    def get_request(self):

        # sending get request and returning the response as response object
        try:
            r = requests.get(url=self.API_URL, params=self.PARAMS)
        except requests.exceptions.Timeout:
            print "Failed to access endpoint due to timeout."
        except requests.exceptions.TooManyRedirects:
            print "Too many redirects occurred."
        except requests.exceptions.RequestException as e:
            print "Critical issue found, respective stacktrace below: {0}".format(e)
            sys.exit(1)

        return r