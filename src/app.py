import requests


def fetch_page(url):
    
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    url = 'https://www.lenovo.com/br/pt/p/laptops/loq-laptops/lenovo-loq-15irh8/83eus00300'
    page_content = fetch_page(url)
    print(page_content)