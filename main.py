import requests

cookies = {
    'ci_session': 'fd35124ee945570bb676eaaaa05c2270cf594b95',
}

headers = {
    'authority': 'shibaminers.pro',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'ci_session=fd35124ee945570bb676eaaaa05c2270cf594b95',
    'origin': 'https://shibaminers.pro',
    'referer': 'https://shibaminers.pro/',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'username': 'oxqaygcbjsbvegshehaseh',
    'password': 'ppppp',
    'reference_user_id': '',
}

response = requests.post('https://shibaminers.pro/ajax_auth', cookies=cookies, headers=headers, data=data)
