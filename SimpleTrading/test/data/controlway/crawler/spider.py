'''
Created on 2016. 9. 6.

@author: lee
'''

import json

from scrapy.http import FormRequest, response


if __name__ == '__main__':
    url = 'https://www.mcdonalds.com.sg/wp-admin/admin-ajax.php'
    payload = {'action': 'ws_search_store_location', 'store_name':'0', 'store_area':'0', 'store_type':'0'}
    req = FormRequest(url, formdata=payload)

    data = json.loads(response.body)
    