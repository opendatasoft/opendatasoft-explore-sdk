# RecordV21


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**links** | [**List[Links]**](Links.md) |  | [optional] 
**field1** | **str** |  | [optional] 
**field2** | **int** |  | [optional] 

## Example

```python
from opendatasoft_explore_async.models.record_v21 import RecordV21

# TODO update the JSON string below
json = "{}"
# create an instance of RecordV21 from a JSON string
record_v21_instance = RecordV21.from_json(json)
# print the JSON string representation of the object
print(RecordV21.to_json())

# convert the object into a dict
record_v21_dict = record_v21_instance.to_dict()
# create an instance of RecordV21 from a dict
record_v21_from_dict = RecordV21.from_dict(record_v21_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


