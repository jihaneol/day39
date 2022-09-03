import requests
sheet_inputs = {
        "price": {
            "city":"Paris",
            "iataCode":"d"
        }
    }
hear = {
    "Authorization":"Bearer asdffaadfs"
}
rr =requests.get(url="https://api.sheety.co/e1c2d9228e3745b0df1bda676cf9ef5d/flightDeals의 사본/prices",json=sheet_inputs,headers=hear )
print(rr.json()["prices"][0])