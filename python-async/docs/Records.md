# Records


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | [optional] 
**links** | [**List[Links]**](Links.md) |  | [optional] 
**results** | [**List[Record]**](Record.md) |  | [optional] 

## Example

```python
from opendatasoft_explore_async.models.records import Records

# TODO update the JSON string below
json = "{}"
# create an instance of Records from a JSON string
records_instance = Records.from_json(json)
# print the JSON string representation of the object
print(Records.to_json())

# convert the object into a dict
records_dict = records_instance.to_dict()
# create an instance of Records from a dict
records_from_dict = Records.from_dict(records_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


