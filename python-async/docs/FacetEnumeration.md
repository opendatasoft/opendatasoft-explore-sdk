# FacetEnumeration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**facets** | [**List[FacetValueEnumeration]**](FacetValueEnumeration.md) |  | [optional] 

## Example

```python
from opendatasoft_explore_async.models.facet_enumeration import FacetEnumeration

# TODO update the JSON string below
json = "{}"
# create an instance of FacetEnumeration from a JSON string
facet_enumeration_instance = FacetEnumeration.from_json(json)
# print the JSON string representation of the object
print(FacetEnumeration.to_json())

# convert the object into a dict
facet_enumeration_dict = facet_enumeration_instance.to_dict()
# create an instance of FacetEnumeration from a dict
facet_enumeration_from_dict = FacetEnumeration.from_dict(facet_enumeration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


