# swagger_client.MiscApi

All URIs are relative to *http://localhost.multiloginapp.com:35000/api/v1/profile*

Method | HTTP request | Description
------------- | ------------- | -------------
[**active_get**](MiscApi.md#active_get) | **GET** /active | checkProfileRunning
[**by_profile_id_get**](MiscApi.md#by_profile_id_get) | **GET** /clone | cloneProfile
[**cookies_import_netscape_get**](MiscApi.md#cookies_import_netscape_get) | **POST** /cookies/import/netscape | cookieImportNetscape
[**cookies_import_webext_get**](MiscApi.md#cookies_import_webext_get) | **POST** /cookies/import/webext | cookieImportJSON
[**share_get**](MiscApi.md#share_get) | **GET** /share | shareProfile
[**start_get**](MiscApi.md#start_get) | **GET** /start | startProfile
[**stop_get**](MiscApi.md#stop_get) | **GET** /stop | stopProfile


# **active_get**
> active_get(profile_id)

checkProfileRunning

Check if profile is already running

### Example
```python
from __future__ import print_function
import time
import multiloginlocal
from multiloginlocal.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = multiloginlocal.MiscApi()
profile_id = 'profile_id_example' # str | Browser profile ID

try:
    # checkProfileRunning
    api_instance.active_get(profile_id)
except ApiException as e:
    print("Exception when calling MiscApi->active_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| Browser profile ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **by_profile_id_get**
> by_profile_id_get(profile_id)

cloneProfile

Clone browser profile

### Example
```python
from __future__ import print_function
import time
import multiloginlocal
from multiloginlocal.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = multiloginlocal.MiscApi()
profile_id = 'profile_id_example' # str | Browser profile ID

try:
    # cloneProfile
    api_instance.by_profile_id_get(profile_id)
except ApiException as e:
    print("Exception when calling MiscApi->by_profile_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| Browser profile ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cookies_import_netscape_get**
> cookies_import_netscape_get(profile_id, content_type, body)

cookieImportNetscape

Import Cookies in Netscape format

### Example
```python
from __future__ import print_function
import time
import multiloginlocal
from multiloginlocal.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = multiloginlocal.MiscApi()
profile_id = 'profile_id_example' # str | Browser profile ID
content_type = 'content_type_example' # str | Cookies in text/plain format
body = multiloginlocal.CookieNetscapeExample() # CookieNetscapeExample | 

try:
    # cookieImportNetscape
    api_instance.cookies_import_netscape_get(profile_id, content_type, body)
except ApiException as e:
    print("Exception when calling MiscApi->cookies_import_netscape_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| Browser profile ID | 
 **content_type** | **str**| Cookies in text/plain format | 
 **body** | [**CookieNetscapeExample**](CookieNetscapeExample.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cookies_import_webext_get**
> cookies_import_webext_get(profile_id, content_type, body)

cookieImportJSON

Import Cookies in JSON format

### Example
```python
from __future__ import print_function
import time
import multiloginlocal
from multiloginlocal.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = multiloginlocal.MiscApi()
profile_id = 'profile_id_example' # str | Browser profile ID
content_type = 'content_type_example' # str | Cookies in application/json format
body = multiloginlocal.CookieJSONExample() # CookieJSONExample | 

try:
    # cookieImportJSON
    api_instance.cookies_import_webext_get(profile_id, content_type, body)
except ApiException as e:
    print("Exception when calling MiscApi->cookies_import_webext_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| Browser profile ID | 
 **content_type** | **str**| Cookies in application/json format | 
 **body** | [**CookieJSONExample**](CookieJSONExample.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_get**
> share_get(profile_id, user)

shareProfile

Share browser profile

### Example
```python
from __future__ import print_function
import time
import multiloginlocal
from multiloginlocal.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = multiloginlocal.MiscApi()
profile_id = 'profile_id_example' # str | Browser profile ID
user = 'user_example' # str | Multilogin account (email address) to share profile with

try:
    # shareProfile
    api_instance.share_get(profile_id, user)
except ApiException as e:
    print("Exception when calling MiscApi->share_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| Browser profile ID | 
 **user** | **str**| Multilogin account (email address) to share profile with | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_get**
> start_get(profile_id, load_tabs=load_tabs, automation=automation, puppeteer=puppeteer)

startProfile

Launch browser profile

### Example
```python
from __future__ import print_function
import time
import multiloginlocal
from multiloginlocal.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = multiloginlocal.MiscApi()
profile_id = 'profile_id_example' # str | Browser profile ID
load_tabs = true # bool | If set to true, tabs from previous session will open (optional)
automation = true # bool | Set to true to launch profile with Selenium/Puppeteer (optional)
puppeteer = true # bool | Set to true to launch profile with Puppeteer automation (optional)

try:
    # startProfile
    api_instance.start_get(profile_id, load_tabs=load_tabs, automation=automation, puppeteer=puppeteer)
except ApiException as e:
    print("Exception when calling MiscApi->start_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| Browser profile ID | 
 **load_tabs** | **bool**| If set to true, tabs from previous session will open | [optional] 
 **automation** | **bool**| Set to true to launch profile with Selenium/Puppeteer | [optional] 
 **puppeteer** | **bool**| Set to true to launch profile with Puppeteer automation | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_get**
> stop_get(profile_id)

stopProfile

Stop browser profile

### Example
```python
from __future__ import print_function
import time
import multiloginlocal
from multiloginlocal.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = multiloginlocal.MiscApi()
profile_id = 'profile_id_example' # str | Browser profile ID

try:
    # stopProfile
    api_instance.stop_get(profile_id)
except ApiException as e:
    print("Exception when calling MiscApi->stop_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| Browser profile ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

