import requests

def check_bridgekeeper():
    try:
        response = requests.get("https://bridgekeeper.onrender.com", timeout=10)
        if response.status_code == 200:
            print("Bridgekeeper is up.")
        else:
            print(f"Bridgekeeper returned status code {response.status_code}")
    except Exception as e:
        print(f"Bridgekeeper check failed: {e}")

if __name__ == "__main__":
    check_bridgekeeper()

