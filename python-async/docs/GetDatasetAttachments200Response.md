# GetDatasetAttachments200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**List[Links]**](Links.md) |  | [optional] 
**attachments** | [**List[Attachment]**](Attachment.md) |  | [optional] 

## Example

```python
from opendatasoft_explore_async.models.get_dataset_attachments200_response import GetDatasetAttachments200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatasetAttachments200Response from a JSON string
get_dataset_attachments200_response_instance = GetDatasetAttachments200Response.from_json(json)
# print the JSON string representation of the object
print(GetDatasetAttachments200Response.to_json())

# convert the object into a dict
get_dataset_attachments200_response_dict = get_dataset_attachments200_response_instance.to_dict()
# create an instance of GetDatasetAttachments200Response from a dict
get_dataset_attachments200_response_from_dict = GetDatasetAttachments200Response.from_dict(get_dataset_attachments200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


