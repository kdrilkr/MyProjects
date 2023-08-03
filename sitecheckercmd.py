import requests

def check(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{url} is running well.")
        else:
            print(f"{url} is NOT running well")
    except requests.RequestException as e :
        print(f"Error of {url} : {e}")
if __name__ == "__main__":
    url = input("URL: ")
    check(url)
    