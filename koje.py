import requests
import random
import string

url = 'https://www.idaind.com/7a-api/user/login'

# Generate random User-Agent
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/123.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/123.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/123.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Edge/123.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/123.0.0.0 Mobile Safari/537.36'
]

def run_script():
    # Ask user how many times they want to run the script
    num_runs = int(input("Ingin berapa kali tuan: "))
    
    for _ in range(num_runs):
        # Generate random deviceId for each run
        device_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=30))
        # Generate random User-Agent for each run
        user_agent = random.choice(user_agents)

        headers = {
            'Host': 'www.idaind.com',
            'Connection': 'keep-alive',
            'Content-Length': '322',
            'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'Content-Type': 'application/json',
            'sec-ch-ua-mobile': '?1',
            'access-token': '',
            'User-Agent': user_agent,
            'sec-ch-ua-platform': '"Android"',
            'Accept': '*/*',
            'Origin': 'https://www.7aonline.in',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.7aonline.in/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
        }

        data = {
            "loginType": "1",
            "deviceId": device_id,
            "code": "DBFO9URM",
            "registChannel": None,
            "apiType": 2,
            "fbc": "",
            "fbp": "",
            "fbEventUrl": "https://www.7aonline.in/?code=DBFO9URM#/",
            "fbClientUserAgent": user_agent
        }

        response = requests.post(url, headers=headers, json=data)

        print(f"Response Code (Run {_+1}): {response.status_code}")
        print(f"Response Text (Run {_+1}): {response.text}")
        print("\n")

run_script()
