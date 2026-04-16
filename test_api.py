import requests

def test_open_food_facts_api():
    url = "https://world.openfoodfacts.org/api/v0/product/3017620425035.json"
    headers = {"User-Agent": "MyTestApp/1.0"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data['product']['product_name'] is not None
    print(f"✅ API test passed – product: {data['product']['product_name']}")

if __name__ == "__main__":
    test_open_food_facts_api()