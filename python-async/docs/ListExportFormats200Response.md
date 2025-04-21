# ListExportFormats200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**List[Links]**](Links.md) |  | [optional] 

## Example

```python
from opendatasoft_explore_async.models.list_export_formats200_response import ListExportFormats200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListExportFormats200Response from a JSON string
list_export_formats200_response_instance = ListExportFormats200Response.from_json(json)
# print the JSON string representation of the object
print(ListExportFormats200Response.to_json())

# convert the object into a dict
list_export_formats200_response_dict = list_export_formats200_response_instance.to_dict()
# create an instance of ListExportFormats200Response from a dict
list_export_formats200_response_from_dict = ListExportFormats200Response.from_dict(list_export_formats200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


