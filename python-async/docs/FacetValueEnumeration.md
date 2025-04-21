# FacetValueEnumeration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**count** | **int** |  | [optional] 
**value** | **str** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from opendatasoft_explore_async.models.facet_value_enumeration import FacetValueEnumeration

# TODO update the JSON string below
json = "{}"
# create an instance of FacetValueEnumeration from a JSON string
facet_value_enumeration_instance = FacetValueEnumeration.from_json(json)
# print the JSON string representation of the object
print(FacetValueEnumeration.to_json())

# convert the object into a dict
facet_value_enumeration_dict = facet_value_enumeration_instance.to_dict()
# create an instance of FacetValueEnumeration from a dict
facet_value_enumeration_from_dict = FacetValueEnumeration.from_dict(facet_value_enumeration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


