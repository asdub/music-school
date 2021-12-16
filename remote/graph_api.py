from django.conf import settings

import json
import logging

import requests
from requests.api import request
import msal


# Optional logging
# logging.basicConfig(level=logging.DEBUG)
def one_drive(request):
    config = json.load(open('onedrive_parameters.json'))

    # Create a preferably long-lived app instance which maintains a token cache.
    app = msal.ConfidentialClientApplication(
        config["client_id"], authority=config["authority"],
        client_credential=config["secret"],
        # token_cache=...  # Default cache is in memory only.
                        # You can learn how to use SerializableTokenCache from
                        # https://msal-python.rtfd.io/en/latest/#msal.SerializableTokenCache
        )

    # The pattern to acquire a token looks like this.
    result = None

    # Firstly, looks up a token from cache
    # Since we are looking for token for the current app, NOT for an end user,
    # notice we give account parameter as None.
    result = app.acquire_token_silent(config["scope"], account=None)
    endpoint = config['endpoint'] + "/" + settings.MSUSER + "/drive/items/" + request + "/children"

    if not result:
        logging.info("No suitable token exists in cache. Let's get a new one from AAD.")
        result = app.acquire_token_for_client(scopes=config["scope"])

    if "access_token" in result:
        # Calling graph using the access token
        graph_data = requests.get(  # Use token to call downstream service
            endpoint,
            headers={'Authorization': 'Bearer ' + result['access_token']}, 
        ).json()
        return graph_data
    else:
        logging.info(result.get("error"))
        logging.info(result.get("error_description"))
        logging.info(result.get("correlation_id"))  # You may need this when reporting a bug
