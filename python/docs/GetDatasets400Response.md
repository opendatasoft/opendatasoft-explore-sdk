# GetDatasets400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**error_code** | **str** |  | 

## Example

```python
from opendatasoft_explore.models.get_datasets400_response import GetDatasets400Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatasets400Response from a JSON string
get_datasets400_response_instance = GetDatasets400Response.from_json(json)
# print the JSON string representation of the object
print(GetDatasets400Response.to_json())

# convert the object into a dict
get_datasets400_response_dict = get_datasets400_response_instance.to_dict()
# create an instance of GetDatasets400Response from a dict
get_datasets400_response_from_dict = GetDatasets400Response.from_dict(get_datasets400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


