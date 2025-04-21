import opendatasoft_explore

import os
from pprint import pprint

# Defining the host is optional and defaults to https://documentation-resources.opendatasoft.com/api/explore/v2.1
# See configuration.py for a list of all supported configuration parameters.
configuration = opendatasoft_explore.Configuration(
    host = "https://documentation-resources.opendatasoft.com/api/explore/v2.1"
)


# Enter a context with an instance of the API client
with opendatasoft_explore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opendatasoft_explore.CatalogApi(api_client)

    try:
        # List datasets
        datasets = api_instance.get_datasets(limit=20)
    except opendatasoft_explore.ApiException as e:
        print("Exception when calling CatalogApi->get_datasets: %s\n" % e)
    else:
        for dataset in datasets.results:
            print(dataset.dataset_id)