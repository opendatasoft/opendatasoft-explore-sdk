# DatasetAttachmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mimetype** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from opendatasoft_explore.models.dataset_attachments_inner import DatasetAttachmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetAttachmentsInner from a JSON string
dataset_attachments_inner_instance = DatasetAttachmentsInner.from_json(json)
# print the JSON string representation of the object
print(DatasetAttachmentsInner.to_json())

# convert the object into a dict
dataset_attachments_inner_dict = dataset_attachments_inner_instance.to_dict()
# create an instance of DatasetAttachmentsInner from a dict
dataset_attachments_inner_from_dict = DatasetAttachmentsInner.from_dict(dataset_attachments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


