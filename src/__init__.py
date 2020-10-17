import os

dir_path = os.path.dirname(os.path.realpath(__file__))

creds = {"google_ads": dir_path + "/creds/googleads.yaml"}


import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s - %(levelname)s] %(message).5000s')
logging.getLogger('google.ads.google_ads.client').setLevel(logging.INFO)


from google.ads.google_ads.client import GoogleAdsClient
gads_client = GoogleAdsClient.load_from_storage(creds["google_ads"])


