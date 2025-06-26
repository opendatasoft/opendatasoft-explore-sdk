# Dataset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**List[Links]**](Links.md) |  | [optional] 
**dataset_id** | **str** |  | [optional] 
**dataset_uid** | **str** |  | [optional] [readonly] 
**attachments** | [**List[DatasetAttachmentsInner]**](DatasetAttachmentsInner.md) |  | [optional] 
**has_records** | **bool** |  | [optional] 
**data_visible** | **bool** |  | [optional] 
**features** | **List[str]** | A map of available features for a dataset, with the fields they apply to.  | [optional] 
**metas** | **object** |  | [optional] 
**fields** | [**List[DatasetFieldsInner]**](DatasetFieldsInner.md) |  | [optional] 

## Example

```python
from opendatasoft_explore_async.models.dataset import Dataset

# TODO update the JSON string below
json = "{}"
# create an instance of Dataset from a JSON string
dataset_instance = Dataset.from_json(json)
# print the JSON string representation of the object
print(Dataset.to_json())

# convert the object into a dict
dataset_dict = dataset_instance.to_dict()
# create an instance of Dataset from a dict
dataset_from_dict = Dataset.from_dict(dataset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


