# GetDatasets429Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errorcode** | **float** |  | 
**reset_time** | **str** |  | 
**limit_time_unit** | **str** |  | 
**call_limit** | **float** |  | 
**error** | **str** |  | 

## Example

```python
from opendatasoft_explore_async.models.get_datasets429_response import GetDatasets429Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatasets429Response from a JSON string
get_datasets429_response_instance = GetDatasets429Response.from_json(json)
# print the JSON string representation of the object
print(GetDatasets429Response.to_json())

# convert the object into a dict
get_datasets429_response_dict = get_datasets429_response_instance.to_dict()
# create an instance of GetDatasets429Response from a dict
get_datasets429_response_from_dict = GetDatasets429Response.from_dict(get_datasets429_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


