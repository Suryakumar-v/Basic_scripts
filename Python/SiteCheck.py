# first do pip install requests

import requests

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return False

def main():
    websites = [
        "http://google.com",
        "http://reddit.com"
        # Add more URLs as needed
    ]

    for site in websites:
        if check_website(site):
            print(f"{site} is accessible")
        else:
            print(f"{site} is not accessible")

if __name__ == "__main__":
    main()