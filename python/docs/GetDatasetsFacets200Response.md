# GetDatasetsFacets200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**List[Links]**](Links.md) |  | [optional] 
**facets** | [**List[FacetEnumeration]**](FacetEnumeration.md) |  | [optional] 

## Example

```python
from opendatasoft_explore.models.get_datasets_facets200_response import GetDatasetsFacets200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatasetsFacets200Response from a JSON string
get_datasets_facets200_response_instance = GetDatasetsFacets200Response.from_json(json)
# print the JSON string representation of the object
print(GetDatasetsFacets200Response.to_json())

# convert the object into a dict
get_datasets_facets200_response_dict = get_datasets_facets200_response_instance.to_dict()
# create an instance of GetDatasetsFacets200Response from a dict
get_datasets_facets200_response_from_dict = GetDatasetsFacets200Response.from_dict(get_datasets_facets200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


