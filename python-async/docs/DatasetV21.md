# DatasetV21


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**List[Links]**](Links.md) |  | [optional] 
**dataset_id** | **str** |  | [optional] 
**dataset_uid** | **str** |  | [optional] [readonly] 
**attachments** | [**List[DatasetV21AttachmentsInner]**](DatasetV21AttachmentsInner.md) |  | [optional] 
**has_records** | **bool** |  | [optional] 
**data_visible** | **bool** |  | [optional] 
**features** | **List[str]** | A map of available features for a dataset, with the fields they apply to.  | [optional] 
**metas** | **object** |  | [optional] 
**fields** | [**List[DatasetV21FieldsInner]**](DatasetV21FieldsInner.md) |  | [optional] 

## Example

```python
from opendatasoft_explore_async.models.dataset_v21 import DatasetV21

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetV21 from a JSON string
dataset_v21_instance = DatasetV21.from_json(json)
# print the JSON string representation of the object
print(DatasetV21.to_json())

# convert the object into a dict
dataset_v21_dict = dataset_v21_instance.to_dict()
# create an instance of DatasetV21 from a dict
dataset_v21_from_dict = DatasetV21.from_dict(dataset_v21_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


