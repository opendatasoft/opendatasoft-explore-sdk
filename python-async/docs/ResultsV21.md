# ResultsV21


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | [optional] 
**links** | [**List[Links]**](Links.md) |  | [optional] 
**results** | [**List[RecordV21]**](RecordV21.md) |  | [optional] 

## Example

```python
from opendatasoft_explore_async.models.results_v21 import ResultsV21

# TODO update the JSON string below
json = "{}"
# create an instance of ResultsV21 from a JSON string
results_v21_instance = ResultsV21.from_json(json)
# print the JSON string representation of the object
print(ResultsV21.to_json())

# convert the object into a dict
results_v21_dict = results_v21_instance.to_dict()
# create an instance of ResultsV21 from a dict
results_v21_from_dict = ResultsV21.from_dict(results_v21_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


