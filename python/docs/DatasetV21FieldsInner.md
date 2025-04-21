# DatasetV21FieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**annotations** | **object** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from opendatasoft_explore.models.dataset_v21_fields_inner import DatasetV21FieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetV21FieldsInner from a JSON string
dataset_v21_fields_inner_instance = DatasetV21FieldsInner.from_json(json)
# print the JSON string representation of the object
print(DatasetV21FieldsInner.to_json())

# convert the object into a dict
dataset_v21_fields_inner_dict = dataset_v21_fields_inner_instance.to_dict()
# create an instance of DatasetV21FieldsInner from a dict
dataset_v21_fields_inner_from_dict = DatasetV21FieldsInner.from_dict(dataset_v21_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


