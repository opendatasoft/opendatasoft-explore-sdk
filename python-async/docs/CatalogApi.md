# opendatasoft_explore_async.CatalogApi

All URIs are relative to *http://PLACEHOLDER_SCHEME://PLACEHOLDER_HOST/api/explore/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_catalog_csv**](CatalogApi.md#export_catalog_csv) | **GET** /catalog/exports/csv | Export a catalog in CSV
[**export_catalog_dcat**](CatalogApi.md#export_catalog_dcat) | **GET** /catalog/exports/dcat{dcat_ap_format} | Export a catalog in RDF/XML (DCAT)
[**export_datasets**](CatalogApi.md#export_datasets) | **GET** /catalog/exports/{format} | Export a catalog
[**get_dataset**](CatalogApi.md#get_dataset) | **GET** /catalog/datasets/{dataset_id} | Show dataset information
[**get_datasets**](CatalogApi.md#get_datasets) | **GET** /catalog/datasets | Query catalog datasets
[**get_datasets_facets**](CatalogApi.md#get_datasets_facets) | **GET** /catalog/facets | List facet values
[**list_export_formats**](CatalogApi.md#list_export_formats) | **GET** /catalog/exports | List export formats


# **export_catalog_csv**
> export_catalog_csv(delimiter=delimiter, list_separator=list_separator, quote_all=quote_all, with_bom=with_bom)

Export a catalog in CSV

Export a catalog in CSV (Comma Separated Values). Specific parameters are described here

### Example

* Api Key Authentication (apikey):

```python
import opendatasoft_explore_async
from opendatasoft_explore_async.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://PLACEHOLDER_SCHEME://PLACEHOLDER_HOST/api/explore/v2.1
# See configuration.py for a list of all supported configuration parameters.
configuration = opendatasoft_explore_async.Configuration(
    host = "http://PLACEHOLDER_SCHEME://PLACEHOLDER_HOST/api/explore/v2.1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
async with opendatasoft_explore_async.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opendatasoft_explore_async.CatalogApi(api_client)
    delimiter = ; # str | Sets the field delimiter of the CSV export (optional) (default to ;)
    list_separator = ',' # str | Sets the separator character used for multivalued strings (optional) (default to ',')
    quote_all = False # bool | Set it to true to force quoting all strings, i.e. surrounding all strings with quote characters (optional) (default to False)
    with_bom = True # bool | Set it to true to force the first characters of the CSV file to be a Unicode Byte Order Mask (0xFEFF). It usually makes Excel correctly open the output CSV file without warning. **Warning:** the default value of this parameter is `false` in v2.0 and `true` starting with v2.1 (optional) (default to True)

    try:
        # Export a catalog in CSV
        await api_instance.export_catalog_csv(delimiter=delimiter, list_separator=list_separator, quote_all=quote_all, with_bom=with_bom)
    except Exception as e:
        print("Exception when calling CatalogApi->export_catalog_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delimiter** | **str**| Sets the field delimiter of the CSV export | [optional] [default to ;]
 **list_separator** | **str**| Sets the separator character used for multivalued strings | [optional] [default to &#39;,&#39;]
 **quote_all** | **bool**| Set it to true to force quoting all strings, i.e. surrounding all strings with quote characters | [optional] [default to False]
 **with_bom** | **bool**| Set it to true to force the first characters of the CSV file to be a Unicode Byte Order Mask (0xFEFF). It usually makes Excel correctly open the output CSV file without warning. **Warning:** the default value of this parameter is &#x60;false&#x60; in v2.0 and &#x60;true&#x60; starting with v2.1 | [optional] [default to True]

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a file |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**429** | Too many requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_catalog_dcat**
> export_catalog_dcat(dcat_ap_format, include_exports=include_exports, use_labels_in_exports=use_labels_in_exports)

Export a catalog in RDF/XML (DCAT)

Export a catalog in RDF/XML described with DCAT (Data Catalog Vocabulary). Specific parameters are described here

### Example

* Api Key Authentication (apikey):

```python
import opendatasoft_explore_async
from opendatasoft_explore_async.models.enum_format_datasets import EnumFormatDatasets
from opendatasoft_explore_async.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://PLACEHOLDER_SCHEME://PLACEHOLDER_HOST/api/explore/v2.1
# See configuration.py for a list of all supported configuration parameters.
configuration = opendatasoft_explore_async.Configuration(
    host = "http://PLACEHOLDER_SCHEME://PLACEHOLDER_HOST/api/explore/v2.1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
async with opendatasoft_explore_async.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opendatasoft_explore_async.CatalogApi(api_client)
    dcat_ap_format = 'dcat_ap_format_example' # str | 
    include_exports = opendatasoft_explore_async.EnumFormatDatasets() # EnumFormatDatasets | Sets the datasets exports exposed in the DCAT export. By default, all exports are exposed. (optional)
    use_labels_in_exports = True # bool | If set to `true`, this parameter will make distributions output the label of each field rather than its name. This parameter only applies on distributions that contain a list of the fields in their output (e.g., CSV, XLSX). (optional) (default to True)

    try:
        # Export a catalog in RDF/XML (DCAT)
        await api_instance.export_catalog_dcat(dcat_ap_format, include_exports=include_exports, use_labels_in_exports=use_labels_in_exports)
    except Exception as e:
        print("Exception when calling CatalogApi->export_catalog_dcat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dcat_ap_format** | **str**|  | 
 **include_exports** | [**EnumFormatDatasets**](.md)| Sets the datasets exports exposed in the DCAT export. By default, all exports are exposed. | [optional] 
 **use_labels_in_exports** | **bool**| If set to &#x60;true&#x60;, this parameter will make distributions output the label of each field rather than its name. This parameter only applies on distributions that contain a list of the fields in their output (e.g., CSV, XLSX). | [optional] [default to True]

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a file |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**429** | Too many requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_datasets**
> export_datasets(format, select=select, where=where, order_by=order_by, group_by=group_by, limit=limit, offset=offset, refine=refine, exclude=exclude, lang=lang, timezone=timezone)

Export a catalog

Export a catalog in the desired format.

### Example

* Api Key Authentication (apikey):

```python
import opendatasoft_explore_async
from opendatasoft_explore_async.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://PLACEHOLDER_SCHEME://PLACEHOLDER_HOST/api/explore/v2.1
# See configuration.py for a list of all supported configuration parameters.
configuration = opendatasoft_explore_async.Configuration(
    host = "http://PLACEHOLDER_SCHEME://PLACEHOLDER_HOST/api/explore/v2.1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
async with opendatasoft_explore_async.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opendatasoft_explore_async.CatalogApi(api_client)
    format = 'format_example' # str | 
    select = 'select_example' # str | Examples: - `select=size` - Example of select, which only return the \"size\" field. - `select=size * 2 as bigger_size` - Example of a complex expression with a label, which returns a new field named \"bigger_size\" and containing the double of size field value. - `select=dataset_id, fields` - Example of a select in catalog ODSQL query to only retrieve dataset_id and schema of datasets.  A select expression can be used to add, remove or change the fields to return. An expression can be:   - a wildcard ('*'): all fields are returned.   - A field name: only the specified field is returned.   - An include/exclude function: All fields matching the include or exclude expression are included or excluded. This expression can contain wildcard.   - A complex expression. The result of the expression is returned. A label can be set for this expression, and in that case, the field will be named after this label. (optional)
    where = 'where_example' # str | A `where` filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) and lots of other functions to perform complex and precise search operations.  For more information, see [Opendatasoft Query Language (ODSQL)](<https://help.opendatasoft.com/apis/ods-explore-v2/#section/Opendatasoft-Query-Language-(ODSQL)/Where-clause>) reference documentation. (optional)
    order_by = 'order_by_example' # str | Example: `order_by=sum(age) desc, name asc`  A comma-separated list of field names or aggregations to sort on, followed by an order (`asc` or `desc`).  Results are sorted in ascending order by default. To sort results in descending order, use the `desc` keyword. (optional)
    group_by = 'group_by_example' # str | Example: `group_by=city_field as city`  A group by expression defines a grouping function for an aggregation. It can be:  - a field name: group result by each value of this field  - a range function: group result by range  - a date function: group result by date  It is possible to specify a custom name with the 'as name' notation. (optional)
    limit = -1 # int | Number of items to return in export.  Use -1 (default) to retrieve all records  (optional) (default to -1)
    offset = 0 # int | Index of the first item to return (starting at 0).  To use with the `limit` parameter to implement pagination.  **Note:** the maximum value depends on the type of query, see the note on `limit` for the details  (optional) (default to 0)
    refine = 'refine_example' # str | Example: `refine=modified:2020` - Return only the value `2020` from the `modified` facet.  A facet filter used to limit the result set. Using this parameter, you can refine your query to display only the selected facet value in the response.  Refinement uses the following syntax: `refine=<FACETNAME>:<FACETVALUE>`  For date, and other hierarchical facets, when refining on one value, all second-level values related to that entry will appear in facets enumeration. For example, after refining on the year 2019, the related second-level month will appear. And when refining on August 2019, the third-level day will appear.  **`refine` must not be confused with a `where` filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.** (optional)
    exclude = 'exclude_example' # str | Examples: - `exclude=city:Paris` - Exclude the value `Paris` from the `city` facet. Facets enumeration will display `Paris` as `excluded` without any count information. - `exclude=modified:2019/12` - Exclude the value `2019/12` from the `modified` facet. Facets enumeration will display `2020` as `excluded` without any count information.  A facet filter used to exclude a facet value from the result set. Using this parameter, you can filter your query to exclude the selected facet value in the response.  `exclude` uses the following syntax: `exclude=<FACETNAME>:<FACETVALUE>`  **`exclude` must not be confused with a `where` filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.** (optional)
    lang = 'lang_example' # str | A language value.  If specified, the `lang` value override the default language, which is \"fr\". The language is used to format string, for example in the `date_format` function. (optional)
    timezone = 'UTC' # str | Set the timezone for datetime fields.  Timezone IDs are defined by the [Unicode CLDR project](https://github.com/unicode-org/cldr). The list of timezone IDs is available in [timezone.xml](https://github.com/unicode-org/cldr/blob/master/common/bcp47/timezone.xml). (optional) (default to 'UTC')

    try:
        # Export a catalog
        await api_instance.export_datasets(format, select=select, where=where, order_by=order_by, group_by=group_by, limit=limit, offset=offset, refine=refine, exclude=exclude, lang=lang, timezone=timezone)
    except Exception as e:
        print("Exception when calling CatalogApi->export_datasets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **select** | **str**| Examples: - &#x60;select&#x3D;size&#x60; - Example of select, which only return the \&quot;size\&quot; field. - &#x60;select&#x3D;size * 2 as bigger_size&#x60; - Example of a complex expression with a label, which returns a new field named \&quot;bigger_size\&quot; and containing the double of size field value. - &#x60;select&#x3D;dataset_id, fields&#x60; - Example of a select in catalog ODSQL query to only retrieve dataset_id and schema of datasets.  A select expression can be used to add, remove or change the fields to return. An expression can be:   - a wildcard (&#39;*&#39;): all fields are returned.   - A field name: only the specified field is returned.   - An include/exclude function: All fields matching the include or exclude expression are included or excluded. This expression can contain wildcard.   - A complex expression. The result of the expression is returned. A label can be set for this expression, and in that case, the field will be named after this label. | [optional] 
 **where** | **str**| A &#x60;where&#x60; filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) and lots of other functions to perform complex and precise search operations.  For more information, see [Opendatasoft Query Language (ODSQL)](&lt;https://help.opendatasoft.com/apis/ods-explore-v2/#section/Opendatasoft-Query-Language-(ODSQL)/Where-clause&gt;) reference documentation. | [optional] 
 **order_by** | **str**| Example: &#x60;order_by&#x3D;sum(age) desc, name asc&#x60;  A comma-separated list of field names or aggregations to sort on, followed by an order (&#x60;asc&#x60; or &#x60;desc&#x60;).  Results are sorted in ascending order by default. To sort results in descending order, use the &#x60;desc&#x60; keyword. | [optional] 
 **group_by** | **str**| Example: &#x60;group_by&#x3D;city_field as city&#x60;  A group by expression defines a grouping function for an aggregation. It can be:  - a field name: group result by each value of this field  - a range function: group result by range  - a date function: group result by date  It is possible to specify a custom name with the &#39;as name&#39; notation. | [optional] 
 **limit** | **int**| Number of items to return in export.  Use -1 (default) to retrieve all records  | [optional] [default to -1]
 **offset** | **int**| Index of the first item to return (starting at 0).  To use with the &#x60;limit&#x60; parameter to implement pagination.  **Note:** the maximum value depends on the type of query, see the note on &#x60;limit&#x60; for the details  | [optional] [default to 0]
 **refine** | **str**| Example: &#x60;refine&#x3D;modified:2020&#x60; - Return only the value &#x60;2020&#x60; from the &#x60;modified&#x60; facet.  A facet filter used to limit the result set. Using this parameter, you can refine your query to display only the selected facet value in the response.  Refinement uses the following syntax: &#x60;refine&#x3D;&lt;FACETNAME&gt;:&lt;FACETVALUE&gt;&#x60;  For date, and other hierarchical facets, when refining on one value, all second-level values related to that entry will appear in facets enumeration. For example, after refining on the year 2019, the related second-level month will appear. And when refining on August 2019, the third-level day will appear.  **&#x60;refine&#x60; must not be confused with a &#x60;where&#x60; filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.** | [optional] 
 **exclude** | **str**| Examples: - &#x60;exclude&#x3D;city:Paris&#x60; - Exclude the value &#x60;Paris&#x60; from the &#x60;city&#x60; facet. Facets enumeration will display &#x60;Paris&#x60; as &#x60;excluded&#x60; without any count information. - &#x60;exclude&#x3D;modified:2019/12&#x60; - Exclude the value &#x60;2019/12&#x60; from the &#x60;modified&#x60; facet. Facets enumeration will display &#x60;2020&#x60; as &#x60;excluded&#x60; without any count information.  A facet filter used to exclude a facet value from the result set. Using this parameter, you can filter your query to exclude the selected facet value in the response.  &#x60;exclude&#x60; uses the following syntax: &#x60;exclude&#x3D;&lt;FACETNAME&gt;:&lt;FACETVALUE&gt;&#x60;  **&#x60;exclude&#x60; must not be confused with a &#x60;where&#x60; filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.** | [optional] 
 **lang** | **str**| A language value.  If specified, the &#x60;lang&#x60; value override the default language, which is \&quot;fr\&quot;. The language is used to format string, for example in the &#x60;date_format&#x60; function. | [optional] 
 **timezone** | **str**| Set the timezone for datetime fields.  Timezone IDs are defined by the [Unicode CLDR project](https://github.com/unicode-org/cldr). The list of timezone IDs is available in [timezone.xml](https://github.com/unicode-org/cldr/blob/master/common/bcp47/timezone.xml). | [optional] [default to &#39;UTC&#39;]

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a file |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**429** | Too many requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset**
> Dataset get_dataset(dataset_id, select=select, lang=lang, timezone=timezone, include_links=include_links, include_app_metas=include_app_metas)

Show dataset information

Returns a list of available endpoints for the specified dataset, with metadata and endpoints.

The response includes the following links:
* the attachments endpoint
* the files endpoint
* the records endpoint
* the catalog endpoint.

### Example

* Api Key Authentication (apikey):

```python
import opendatasoft_explore_async
from opendatasoft_explore_async.models.dataset import Dataset
from opendatasoft_explore_async.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://PLACEHOLDER_SCHEME://PLACEHOLDER_HOST/api/explore/v2.1
# See configuration.py for a list of all supported configuration parameters.
configuration = opendatasoft_explore_async.Configuration(
    host = "http://PLACEHOLDER_SCHEME://PLACEHOLDER_HOST/api/explore/v2.1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
async with opendatasoft_explore_async.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opendatasoft_explore_async.CatalogApi(api_client)
    dataset_id = 'dataset_id_example' # str | The identifier of the dataset to be queried.  You can find it in the \"Information\" tab of the dataset page or in the dataset URL, right after `/datasets/`.
    select = 'select_example' # str | Examples: - `select=size` - Example of select, which only return the \"size\" field. - `select=size * 2 as bigger_size` - Example of a complex expression with a label, which returns a new field named \"bigger_size\" and containing the double of size field value. - `select=dataset_id, fields` - Example of a select in catalog ODSQL query to only retrieve dataset_id and schema of datasets.  A select expression can be used to add, remove or change the fields to return. An expression can be:   - a wildcard ('*'): all fields are returned.   - A field name: only the specified field is returned.   - An include/exclude function: All fields matching the include or exclude expression are included or excluded. This expression can contain wildcard.   - A complex expression. The result of the expression is returned. A label can be set for this expression, and in that case, the field will be named after this label. (optional)
    lang = 'lang_example' # str | A language value.  If specified, the `lang` value override the default language, which is \"fr\". The language is used to format string, for example in the `date_format` function. (optional)
    timezone = 'UTC' # str | Set the timezone for datetime fields.  Timezone IDs are defined by the [Unicode CLDR project](https://github.com/unicode-org/cldr). The list of timezone IDs is available in [timezone.xml](https://github.com/unicode-org/cldr/blob/master/common/bcp47/timezone.xml). (optional) (default to 'UTC')
    include_links = False # bool | If set to `true`, this parameter will add HATEOAS links in the response.  (optional) (default to False)
    include_app_metas = False # bool | If set to `true`, this parameter will add application metadata to the response.  (optional) (default to False)

    try:
        # Show dataset information
        api_response = await api_instance.get_dataset(dataset_id, select=select, lang=lang, timezone=timezone, include_links=include_links, include_app_metas=include_app_metas)
        print("The response of CatalogApi->get_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogApi->get_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The identifier of the dataset to be queried.  You can find it in the \&quot;Information\&quot; tab of the dataset page or in the dataset URL, right after &#x60;/datasets/&#x60;. | 
 **select** | **str**| Examples: - &#x60;select&#x3D;size&#x60; - Example of select, which only return the \&quot;size\&quot; field. - &#x60;select&#x3D;size * 2 as bigger_size&#x60; - Example of a complex expression with a label, which returns a new field named \&quot;bigger_size\&quot; and containing the double of size field value. - &#x60;select&#x3D;dataset_id, fields&#x60; - Example of a select in catalog ODSQL query to only retrieve dataset_id and schema of datasets.  A select expression can be used to add, remove or change the fields to return. An expression can be:   - a wildcard (&#39;*&#39;): all fields are returned.   - A field name: only the specified field is returned.   - An include/exclude function: All fields matching the include or exclude expression are included or excluded. This expression can contain wildcard.   - A complex expression. The result of the expression is returned. A label can be set for this expression, and in that case, the field will be named after this label. | [optional] 
 **lang** | **str**| A language value.  If specified, the &#x60;lang&#x60; value override the default language, which is \&quot;fr\&quot;. The language is used to format string, for example in the &#x60;date_format&#x60; function. | [optional] 
 **timezone** | **str**| Set the timezone for datetime fields.  Timezone IDs are defined by the [Unicode CLDR project](https://github.com/unicode-org/cldr). The list of timezone IDs is available in [timezone.xml](https://github.com/unicode-org/cldr/blob/master/common/bcp47/timezone.xml). | [optional] [default to &#39;UTC&#39;]
 **include_links** | **bool**| If set to &#x60;true&#x60;, this parameter will add HATEOAS links in the response.  | [optional] [default to False]
 **include_app_metas** | **bool**| If set to &#x60;true&#x60;, this parameter will add application metadata to the response.  | [optional] [default to False]

### Return type

[**Dataset**](Dataset.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8json, application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The dataset |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**429** | Too many requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datasets**
> Datasets get_datasets(select=select, where=where, order_by=order_by, limit=limit, offset=offset, refine=refine, exclude=exclude, lang=lang, timezone=timezone, group_by=group_by, include_links=include_links, include_app_metas=include_app_metas)

Query catalog datasets

Retrieve available datasets.

### Example

* Api Key Authentication (apikey):

```python
import opendatasoft_explore_async
from opendatasoft_explore_async.models.datasets import Datasets
from opendatasoft_explore_async.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://PLACEHOLDER_SCHEME://PLACEHOLDER_HOST/api/explore/v2.1
# See configuration.py for a list of all supported configuration parameters.
configuration = opendatasoft_explore_async.Configuration(
    host = "http://PLACEHOLDER_SCHEME://PLACEHOLDER_HOST/api/explore/v2.1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
async with opendatasoft_explore_async.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opendatasoft_explore_async.CatalogApi(api_client)
    select = 'select_example' # str | Examples: - `select=size` - Example of select, which only return the \"size\" field. - `select=size * 2 as bigger_size` - Example of a complex expression with a label, which returns a new field named \"bigger_size\" and containing the double of size field value. - `select=dataset_id, fields` - Example of a select in catalog ODSQL query to only retrieve dataset_id and schema of datasets.  A select expression can be used to add, remove or change the fields to return. An expression can be:   - a wildcard ('*'): all fields are returned.   - A field name: only the specified field is returned.   - An include/exclude function: All fields matching the include or exclude expression are included or excluded. This expression can contain wildcard.   - A complex expression. The result of the expression is returned. A label can be set for this expression, and in that case, the field will be named after this label. (optional)
    where = 'where_example' # str | A `where` filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) and lots of other functions to perform complex and precise search operations.  For more information, see [Opendatasoft Query Language (ODSQL)](<https://help.opendatasoft.com/apis/ods-explore-v2/#section/Opendatasoft-Query-Language-(ODSQL)/Where-clause>) reference documentation. (optional)
    order_by = 'order_by_example' # str | Example: `order_by=sum(age) desc, name asc`  A comma-separated list of field names or aggregations to sort on, followed by an order (`asc` or `desc`).  Results are sorted in ascending order by default. To sort results in descending order, use the `desc` keyword. (optional)
    limit = 10 # int | Number of items to return.  To use with the `offset` parameter to implement pagination.  The maximum possible value depends on whether the query contains a `group_by` clause or not.  For a query **without** a `group_by`:   - the maximum value for `limit` is 100,   - `offset+limit` should be less than 10000  For a query **with** a `group_by`:   - the maximum value for `limit` is 20000,   - `offset+limit` should be less than 20000  **Note:** If you need more results, please use the /exports endpoint.  (optional) (default to 10)
    offset = 0 # int | Index of the first item to return (starting at 0).  To use with the `limit` parameter to implement pagination.  **Note:** the maximum value depends on the type of query, see the note on `limit` for the details  (optional) (default to 0)
    refine = 'refine_example' # str | Example: `refine=modified:2020` - Return only the value `2020` from the `modified` facet.  A facet filter used to limit the result set. Using this parameter, you can refine your query to display only the selected facet value in the response.  Refinement uses the following syntax: `refine=<FACETNAME>:<FACETVALUE>`  For date, and other hierarchical facets, when refining on one value, all second-level values related to that entry will appear in facets enumeration. For example, after refining on the year 2019, the related second-level month will appear. And when refining on August 2019, the third-level day will appear.  **`refine` must not be confused with a `where` filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.** (optional)
    exclude = 'exclude_example' # str | Examples: - `exclude=city:Paris` - Exclude the value `Paris` from the `city` facet. Facets enumeration will display `Paris` as `excluded` without any count information. - `exclude=modified:2019/12` - Exclude the value `2019/12` from the `modified` facet. Facets enumeration will display `2020` as `excluded` without any count information.  A facet filter used to exclude a facet value from the result set. Using this parameter, you can filter your query to exclude the selected facet value in the response.  `exclude` uses the following syntax: `exclude=<FACETNAME>:<FACETVALUE>`  **`exclude` must not be confused with a `where` filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.** (optional)
    lang = 'lang_example' # str | A language value.  If specified, the `lang` value override the default language, which is \"fr\". The language is used to format string, for example in the `date_format` function. (optional)
    timezone = 'UTC' # str | Set the timezone for datetime fields.  Timezone IDs are defined by the [Unicode CLDR project](https://github.com/unicode-org/cldr). The list of timezone IDs is available in [timezone.xml](https://github.com/unicode-org/cldr/blob/master/common/bcp47/timezone.xml). (optional) (default to 'UTC')
    group_by = 'group_by_example' # str | Example: `group_by=city_field as city`  A group by expression defines a grouping function for an aggregation. It can be:  - a field name: group result by each value of this field  - a range function: group result by range  - a date function: group result by date  It is possible to specify a custom name with the 'as name' notation. (optional)
    include_links = False # bool | If set to `true`, this parameter will add HATEOAS links in the response.  (optional) (default to False)
    include_app_metas = False # bool | If set to `true`, this parameter will add application metadata to the response.  (optional) (default to False)

    try:
        # Query catalog datasets
        api_response = await api_instance.get_datasets(select=select, where=where, order_by=order_by, limit=limit, offset=offset, refine=refine, exclude=exclude, lang=lang, timezone=timezone, group_by=group_by, include_links=include_links, include_app_metas=include_app_metas)
        print("The response of CatalogApi->get_datasets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogApi->get_datasets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | **str**| Examples: - &#x60;select&#x3D;size&#x60; - Example of select, which only return the \&quot;size\&quot; field. - &#x60;select&#x3D;size * 2 as bigger_size&#x60; - Example of a complex expression with a label, which returns a new field named \&quot;bigger_size\&quot; and containing the double of size field value. - &#x60;select&#x3D;dataset_id, fields&#x60; - Example of a select in catalog ODSQL query to only retrieve dataset_id and schema of datasets.  A select expression can be used to add, remove or change the fields to return. An expression can be:   - a wildcard (&#39;*&#39;): all fields are returned.   - A field name: only the specified field is returned.   - An include/exclude function: All fields matching the include or exclude expression are included or excluded. This expression can contain wildcard.   - A complex expression. The result of the expression is returned. A label can be set for this expression, and in that case, the field will be named after this label. | [optional] 
 **where** | **str**| A &#x60;where&#x60; filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) and lots of other functions to perform complex and precise search operations.  For more information, see [Opendatasoft Query Language (ODSQL)](&lt;https://help.opendatasoft.com/apis/ods-explore-v2/#section/Opendatasoft-Query-Language-(ODSQL)/Where-clause&gt;) reference documentation. | [optional] 
 **order_by** | **str**| Example: &#x60;order_by&#x3D;sum(age) desc, name asc&#x60;  A comma-separated list of field names or aggregations to sort on, followed by an order (&#x60;asc&#x60; or &#x60;desc&#x60;).  Results are sorted in ascending order by default. To sort results in descending order, use the &#x60;desc&#x60; keyword. | [optional] 
 **limit** | **int**| Number of items to return.  To use with the &#x60;offset&#x60; parameter to implement pagination.  The maximum possible value depends on whether the query contains a &#x60;group_by&#x60; clause or not.  For a query **without** a &#x60;group_by&#x60;:   - the maximum value for &#x60;limit&#x60; is 100,   - &#x60;offset+limit&#x60; should be less than 10000  For a query **with** a &#x60;group_by&#x60;:   - the maximum value for &#x60;limit&#x60; is 20000,   - &#x60;offset+limit&#x60; should be less than 20000  **Note:** If you need more results, please use the /exports endpoint.  | [optional] [default to 10]
 **offset** | **int**| Index of the first item to return (starting at 0).  To use with the &#x60;limit&#x60; parameter to implement pagination.  **Note:** the maximum value depends on the type of query, see the note on &#x60;limit&#x60; for the details  | [optional] [default to 0]
 **refine** | **str**| Example: &#x60;refine&#x3D;modified:2020&#x60; - Return only the value &#x60;2020&#x60; from the &#x60;modified&#x60; facet.  A facet filter used to limit the result set. Using this parameter, you can refine your query to display only the selected facet value in the response.  Refinement uses the following syntax: &#x60;refine&#x3D;&lt;FACETNAME&gt;:&lt;FACETVALUE&gt;&#x60;  For date, and other hierarchical facets, when refining on one value, all second-level values related to that entry will appear in facets enumeration. For example, after refining on the year 2019, the related second-level month will appear. And when refining on August 2019, the third-level day will appear.  **&#x60;refine&#x60; must not be confused with a &#x60;where&#x60; filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.** | [optional] 
 **exclude** | **str**| Examples: - &#x60;exclude&#x3D;city:Paris&#x60; - Exclude the value &#x60;Paris&#x60; from the &#x60;city&#x60; facet. Facets enumeration will display &#x60;Paris&#x60; as &#x60;excluded&#x60; without any count information. - &#x60;exclude&#x3D;modified:2019/12&#x60; - Exclude the value &#x60;2019/12&#x60; from the &#x60;modified&#x60; facet. Facets enumeration will display &#x60;2020&#x60; as &#x60;excluded&#x60; without any count information.  A facet filter used to exclude a facet value from the result set. Using this parameter, you can filter your query to exclude the selected facet value in the response.  &#x60;exclude&#x60; uses the following syntax: &#x60;exclude&#x3D;&lt;FACETNAME&gt;:&lt;FACETVALUE&gt;&#x60;  **&#x60;exclude&#x60; must not be confused with a &#x60;where&#x60; filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.** | [optional] 
 **lang** | **str**| A language value.  If specified, the &#x60;lang&#x60; value override the default language, which is \&quot;fr\&quot;. The language is used to format string, for example in the &#x60;date_format&#x60; function. | [optional] 
 **timezone** | **str**| Set the timezone for datetime fields.  Timezone IDs are defined by the [Unicode CLDR project](https://github.com/unicode-org/cldr). The list of timezone IDs is available in [timezone.xml](https://github.com/unicode-org/cldr/blob/master/common/bcp47/timezone.xml). | [optional] [default to &#39;UTC&#39;]
 **group_by** | **str**| Example: &#x60;group_by&#x3D;city_field as city&#x60;  A group by expression defines a grouping function for an aggregation. It can be:  - a field name: group result by each value of this field  - a range function: group result by range  - a date function: group result by date  It is possible to specify a custom name with the &#39;as name&#39; notation. | [optional] 
 **include_links** | **bool**| If set to &#x60;true&#x60;, this parameter will add HATEOAS links in the response.  | [optional] [default to False]
 **include_app_metas** | **bool**| If set to &#x60;true&#x60;, this parameter will add application metadata to the response.  | [optional] [default to False]

### Return type

[**Datasets**](Datasets.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of available datasets |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**429** | Too many requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datasets_facets**
> GetDatasetsFacets200Response get_datasets_facets(facet=facet, refine=refine, exclude=exclude, where=where, timezone=timezone)

List facet values

Enumerate facet values for datasets and returns a list of values for each facet.
Can be used to implement guided navigation in large result sets.

### Example

* Api Key Authentication (apikey):

```python
import opendatasoft_explore_async
from opendatasoft_explore_async.models.get_datasets_facets200_response import GetDatasetsFacets200Response
from opendatasoft_explore_async.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://PLACEHOLDER_SCHEME://PLACEHOLDER_HOST/api/explore/v2.1
# See configuration.py for a list of all supported configuration parameters.
configuration = opendatasoft_explore_async.Configuration(
    host = "http://PLACEHOLDER_SCHEME://PLACEHOLDER_HOST/api/explore/v2.1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
async with opendatasoft_explore_async.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opendatasoft_explore_async.CatalogApi(api_client)
    facet = 'facet_example' # str | A facet is a field used for simple filtering (through the `refine` and `exclude` parameters) or exploration (with the `/facets` endpoint).  It can also be a function such as `facet=facet(name=\"field_name\")` which is identical to `facet=field_name`. But this `facet()` function can also take some optional arguments such as `disjunctive`, `hierarchical`, `separator`, `sort` and `limit`.  * `disjunctive`: a boolean `true/false`, whether multiple values can be selected for the facet * `hierarchical`: a boolean `true/false` if the field is hierarchical. The separator must be given as the argument.    For instance, you can do `facet=facet(name=\"filepath\", hierarchical=true, separator=\"/\")` to retrieve facets related to this field which might look like `\"/home/user/file.txt\"` * `separator`: a string, e.g. `/`, `-`, `;` * `sort`: a string which describes how to sort the facets. Possible arguments are `count` and `-count` for all field types, `alphanum` and `-alphanum` for `date`, `datetime` and `text`, `num` and `-num` for `decimal` and `int` * `limit`: an integer to limit the number of results  (optional)
    refine = 'refine_example' # str | Example: `refine=modified:2020` - Return only the value `2020` from the `modified` facet.  A facet filter used to limit the result set. Using this parameter, you can refine your query to display only the selected facet value in the response.  Refinement uses the following syntax: `refine=<FACETNAME>:<FACETVALUE>`  For date, and other hierarchical facets, when refining on one value, all second-level values related to that entry will appear in facets enumeration. For example, after refining on the year 2019, the related second-level month will appear. And when refining on August 2019, the third-level day will appear.  **`refine` must not be confused with a `where` filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.** (optional)
    exclude = 'exclude_example' # str | Examples: - `exclude=city:Paris` - Exclude the value `Paris` from the `city` facet. Facets enumeration will display `Paris` as `excluded` without any count information. - `exclude=modified:2019/12` - Exclude the value `2019/12` from the `modified` facet. Facets enumeration will display `2020` as `excluded` without any count information.  A facet filter used to exclude a facet value from the result set. Using this parameter, you can filter your query to exclude the selected facet value in the response.  `exclude` uses the following syntax: `exclude=<FACETNAME>:<FACETVALUE>`  **`exclude` must not be confused with a `where` filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.** (optional)
    where = 'where_example' # str | A `where` filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) and lots of other functions to perform complex and precise search operations.  For more information, see [Opendatasoft Query Language (ODSQL)](<https://help.opendatasoft.com/apis/ods-explore-v2/#section/Opendatasoft-Query-Language-(ODSQL)/Where-clause>) reference documentation. (optional)
    timezone = 'UTC' # str | Set the timezone for datetime fields.  Timezone IDs are defined by the [Unicode CLDR project](https://github.com/unicode-org/cldr). The list of timezone IDs is available in [timezone.xml](https://github.com/unicode-org/cldr/blob/master/common/bcp47/timezone.xml). (optional) (default to 'UTC')

    try:
        # List facet values
        api_response = await api_instance.get_datasets_facets(facet=facet, refine=refine, exclude=exclude, where=where, timezone=timezone)
        print("The response of CatalogApi->get_datasets_facets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogApi->get_datasets_facets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facet** | **str**| A facet is a field used for simple filtering (through the &#x60;refine&#x60; and &#x60;exclude&#x60; parameters) or exploration (with the &#x60;/facets&#x60; endpoint).  It can also be a function such as &#x60;facet&#x3D;facet(name&#x3D;\&quot;field_name\&quot;)&#x60; which is identical to &#x60;facet&#x3D;field_name&#x60;. But this &#x60;facet()&#x60; function can also take some optional arguments such as &#x60;disjunctive&#x60;, &#x60;hierarchical&#x60;, &#x60;separator&#x60;, &#x60;sort&#x60; and &#x60;limit&#x60;.  * &#x60;disjunctive&#x60;: a boolean &#x60;true/false&#x60;, whether multiple values can be selected for the facet * &#x60;hierarchical&#x60;: a boolean &#x60;true/false&#x60; if the field is hierarchical. The separator must be given as the argument.    For instance, you can do &#x60;facet&#x3D;facet(name&#x3D;\&quot;filepath\&quot;, hierarchical&#x3D;true, separator&#x3D;\&quot;/\&quot;)&#x60; to retrieve facets related to this field which might look like &#x60;\&quot;/home/user/file.txt\&quot;&#x60; * &#x60;separator&#x60;: a string, e.g. &#x60;/&#x60;, &#x60;-&#x60;, &#x60;;&#x60; * &#x60;sort&#x60;: a string which describes how to sort the facets. Possible arguments are &#x60;count&#x60; and &#x60;-count&#x60; for all field types, &#x60;alphanum&#x60; and &#x60;-alphanum&#x60; for &#x60;date&#x60;, &#x60;datetime&#x60; and &#x60;text&#x60;, &#x60;num&#x60; and &#x60;-num&#x60; for &#x60;decimal&#x60; and &#x60;int&#x60; * &#x60;limit&#x60;: an integer to limit the number of results  | [optional] 
 **refine** | **str**| Example: &#x60;refine&#x3D;modified:2020&#x60; - Return only the value &#x60;2020&#x60; from the &#x60;modified&#x60; facet.  A facet filter used to limit the result set. Using this parameter, you can refine your query to display only the selected facet value in the response.  Refinement uses the following syntax: &#x60;refine&#x3D;&lt;FACETNAME&gt;:&lt;FACETVALUE&gt;&#x60;  For date, and other hierarchical facets, when refining on one value, all second-level values related to that entry will appear in facets enumeration. For example, after refining on the year 2019, the related second-level month will appear. And when refining on August 2019, the third-level day will appear.  **&#x60;refine&#x60; must not be confused with a &#x60;where&#x60; filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.** | [optional] 
 **exclude** | **str**| Examples: - &#x60;exclude&#x3D;city:Paris&#x60; - Exclude the value &#x60;Paris&#x60; from the &#x60;city&#x60; facet. Facets enumeration will display &#x60;Paris&#x60; as &#x60;excluded&#x60; without any count information. - &#x60;exclude&#x3D;modified:2019/12&#x60; - Exclude the value &#x60;2019/12&#x60; from the &#x60;modified&#x60; facet. Facets enumeration will display &#x60;2020&#x60; as &#x60;excluded&#x60; without any count information.  A facet filter used to exclude a facet value from the result set. Using this parameter, you can filter your query to exclude the selected facet value in the response.  &#x60;exclude&#x60; uses the following syntax: &#x60;exclude&#x3D;&lt;FACETNAME&gt;:&lt;FACETVALUE&gt;&#x60;  **&#x60;exclude&#x60; must not be confused with a &#x60;where&#x60; filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.** | [optional] 
 **where** | **str**| A &#x60;where&#x60; filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) and lots of other functions to perform complex and precise search operations.  For more information, see [Opendatasoft Query Language (ODSQL)](&lt;https://help.opendatasoft.com/apis/ods-explore-v2/#section/Opendatasoft-Query-Language-(ODSQL)/Where-clause&gt;) reference documentation. | [optional] 
 **timezone** | **str**| Set the timezone for datetime fields.  Timezone IDs are defined by the [Unicode CLDR project](https://github.com/unicode-org/cldr). The list of timezone IDs is available in [timezone.xml](https://github.com/unicode-org/cldr/blob/master/common/bcp47/timezone.xml). | [optional] [default to &#39;UTC&#39;]

### Return type

[**GetDatasetsFacets200Response**](GetDatasetsFacets200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An enumeration of facets |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**429** | Too many requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_export_formats**
> ListExportFormats200Response list_export_formats()

List export formats

List available export formats

### Example

* Api Key Authentication (apikey):

```python
import opendatasoft_explore_async
from opendatasoft_explore_async.models.list_export_formats200_response import ListExportFormats200Response
from opendatasoft_explore_async.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://PLACEHOLDER_SCHEME://PLACEHOLDER_HOST/api/explore/v2.1
# See configuration.py for a list of all supported configuration parameters.
configuration = opendatasoft_explore_async.Configuration(
    host = "http://PLACEHOLDER_SCHEME://PLACEHOLDER_HOST/api/explore/v2.1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
async with opendatasoft_explore_async.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opendatasoft_explore_async.CatalogApi(api_client)

    try:
        # List export formats
        api_response = await api_instance.list_export_formats()
        print("The response of CatalogApi->list_export_formats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogApi->list_export_formats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListExportFormats200Response**](ListExportFormats200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of available export formats |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**429** | Too many requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

