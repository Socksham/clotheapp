
import uuid
import json
import requests
def get_random_code():
    code = str(uuid.uuid4())[:8].replace('-', '').lower()
    return code

#clothingtype: top, bottom, lower,/style: casual or formal 
def getAPICall(location, gender, color, clothingtype, style, priceUpper, priceLower):
    # set up the request parameters
    query = gender + " " + color + " " + clothingtype + " " + style
    params = {
    'api_key': '4EA59F5AB8A1436290675DE6F9B92FD8',
    'location': location,
    'search_type':"shopping",
    'q': query
    }

    # make the http GET request to Scale SERP
    api_result = requests.get('https://api.scaleserp.com/search', params)

    # print the JSON response from Scale SERP
    # print(json.dumps(api_result.json()))
    res = api_result.json()

    results = []

    for item in res["shopping_results"]:
        if item['price'] > priceLower and item['price']>priceUpper:
            answerDict = {
                "title": item['price'],
                "id": item['id'],
                "link": item['link'],
                "rating": item['rating'],
                "reviews": item['reviews'],
                "price": item['price'],
                "price_raw": item['price_raw'],
                "merchant": item['merchant'],
                "snippet": item['snippet'],
                "delivery": item['delivery'],
                'image': item['image'],
                "position": item['position']
            }
            results.append(answerDict)
    return results