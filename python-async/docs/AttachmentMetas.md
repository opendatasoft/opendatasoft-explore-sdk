# AttachmentMetas


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mime_type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from opendatasoft_explore_async.models.attachment_metas import AttachmentMetas

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentMetas from a JSON string
attachment_metas_instance = AttachmentMetas.from_json(json)
# print the JSON string representation of the object
print(AttachmentMetas.to_json())

# convert the object into a dict
attachment_metas_dict = attachment_metas_instance.to_dict()
# create an instance of AttachmentMetas from a dict
attachment_metas_from_dict = AttachmentMetas.from_dict(attachment_metas_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


