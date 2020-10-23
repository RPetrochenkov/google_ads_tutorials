import os
import json

# my local directory is right now
src_path = os.path.dirname(os.path.realpath(__file__))

dir_path = os.path.join(src_path, '..')

# credentials dictonary
creds = {"google_ads": dir_path + "/creds/googleads.yaml"}


if not os.path.isfile(creds["google_ads"]):
    raise FileExistsError("File doesn't exists. Please create folder src/creds and put googleads.yaml file there. ")

resources = {"config": dir_path + "/config/config.json"}


# This logging allows to see additional information on debugging
import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s - %(levelname)s] %(message).5000s')
logging.getLogger('google.ads.google_ads.client').setLevel(logging.INFO)


# Initialize the google_ads client
from google.ads.google_ads.client import GoogleAdsClient
gads_client = GoogleAdsClient.load_from_storage(creds["google_ads"])

# Initialize all global configurations
config = json.load(open(resources["config"], "r"))

