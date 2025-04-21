# ResultsDatasetV21


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | [optional] 
**links** | [**List[Links]**](Links.md) |  | [optional] 
**results** | [**List[DatasetV21]**](DatasetV21.md) |  | [optional] 

## Example

```python
from opendatasoft_explore.models.results_dataset_v21 import ResultsDatasetV21

# TODO update the JSON string below
json = "{}"
# create an instance of ResultsDatasetV21 from a JSON string
results_dataset_v21_instance = ResultsDatasetV21.from_json(json)
# print the JSON string representation of the object
print(ResultsDatasetV21.to_json())

# convert the object into a dict
results_dataset_v21_dict = results_dataset_v21_instance.to_dict()
# create an instance of ResultsDatasetV21 from a dict
results_dataset_v21_from_dict = ResultsDatasetV21.from_dict(results_dataset_v21_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


