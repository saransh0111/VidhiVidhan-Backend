from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from helper import keys, messages

search_param = openapi.Parameter(keys.SEARCH,in_=openapi.IN_QUERY, description=messages.ENTER_SEARCH_DATA, type=openapi.TYPE_STRING)
mobile_param = openapi.Parameter(keys.MOBILE,in_=openapi.IN_QUERY, description=messages.ENTER_VALID_NUMBER, type=openapi.TYPE_STRING)
image_param = openapi.Parameter(keys.IMAGE,in_=openapi.IN_FORM, description=messages.UPLOAD_IMAGE, type=openapi.TYPE_FILE)