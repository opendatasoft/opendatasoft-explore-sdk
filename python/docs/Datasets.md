# Datasets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | [optional] 
**links** | [**List[Links]**](Links.md) |  | [optional] 
**results** | [**List[Dataset]**](Dataset.md) |  | [optional] 

## Example

```python
from opendatasoft_explore.models.datasets import Datasets

# TODO update the JSON string below
json = "{}"
# create an instance of Datasets from a JSON string
datasets_instance = Datasets.from_json(json)
# print the JSON string representation of the object
print(Datasets.to_json())

# convert the object into a dict
datasets_dict = datasets_instance.to_dict()
# create an instance of Datasets from a dict
datasets_from_dict = Datasets.from_dict(datasets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


