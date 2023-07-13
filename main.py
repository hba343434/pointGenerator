import requests
import argparse
import time
class main():

    headers={
    "Cookie": "XSRF-TOKEN=eyJpdiI6IjVnaERuVXowZGxBNXJONi9hbE1YTUE9PSIsInZhbHVlIjoiYUYrd3RUNXhVTDFSdkw2UHo5dlBkbUZjZDNLY1NSOUhlMGlsakJCd2NWM0RiMnpTWUw4YUpXV29xTU5hb016TlZpdHFIVzVmVkVEd0xlenVrVk05bzhkSHFjNCtHWGZhWkdxMnpsRVBQZXhQNkRJNkoxMm4zV1lsUzAycXhySFEiLCJtYWMiOiJmMzc1ZWI2ZWVjMTA5MzQ3ZjViZjYzOTBhZGFhZmRiNTllMmMyOGMzOWMyN2ZhNWZkYzdiZjkyYTNlYjViMmM3IiwidGFnIjoiIn0%3D; storyglory_session=eyJpdiI6IjNZTXFEbzdVSkJmbXBydjliUTFOaHc9PSIsInZhbHVlIjoidzVXVVFZWW16RVNTeFdFVWlHS3FycjdITThjQlJnNGV6SHl1L2pCV3VSUXNBMm5qMzFzVHBJVG9samcybDNJRkNOcE15bE5PdG9VK3lQZHE4NG83Mkp6aWpLbzRBYjN6UFhyQkpwUDdQdll4ZGVWeUsvRlRtOVhGV2lIckp2Y2IiLCJtYWMiOiJhNTUyMDA0NGIzMDI2ZTg5YjdmYmYyZjIwMTAwNGU1OWEyOGM0ZGYzMDQ3ZWE5MTBlNjc4ODE3NWM0Mzk3OTIwIiwidGFnIjoiIn0%3D",

    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/json",
    "Content-Length": "57",
    "Referer": "https://mmstoryglory.com/login",
    "X-Xsrf-Token": "eyJpdiI6IjVnaERuVXowZGxBNXJONi9hbE1YTUE9PSIsInZhbHVlIjoiYUYrd3RUNXhVTDFSdkw2UHo5dlBkbUZjZDNLY1NSOUhlMGlsakJCd2NWM0RiMnpTWUw4YUpXV29xTU5hb016TlZpdHFIVzVmVkVEd0xlenVrVk05bzhkSHFjNCtHWGZhWkdxMnpsRVBQZXhQNkRJNkoxMm4zV1lsUzAycXhySFEiLCJtYWMiOiJmMzc1ZWI2ZWVjMTA5MzQ3ZjViZjYzOTBhZGFhZmRiNTllMmMyOGMzOWMyN2ZhNWZkYzdiZjkyYTNlYjViMmM3IiwidGFnIjoiIn0=",


    "Origin": "https://mmstoryglory.com",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Te": "trailers"}
    request=requests.session()

    def __init__(self):
        print("""
              
⣴⡿⠶⠀⠀⠀⣦⣀⣴⠀⠀⠀⠀
⣿⡄⠀⠀⣠⣾⠛⣿⠛⣷⠀⠿⣦
⠙⣷⣦⣾⣿⣿⣿⣿⣿⠟⠀⣴⣿
⠀⣸⣿⣿⣿⣿⣿⣿⣿⣾⠿⠋⠁
⠀⣿⣿⣿⠿⡿⣿⣿⡿⠀⠀⠀⠀
⢸⣿⡋⠀⠀⠀⢹⣿⡇⠀⠀⠀⠀
⣿⡟⠀⠀⠀⠀⠀⢿⡇⠀⠀⠀⠀
⠉⠁⠀⠀⠀⠀⠀⠸⠇⠀⠀⠀⠀
              
author:::hlaing bwar aung
nickname:::blackkitty
              
              """)

    def attack(self,email,password):
        cred={"email":email,"password":password}
        resp=self.request.post("https://mmstoryglory.com/login",headers=self.headers,json=cred)
        c=1
        while True:
            
            resp3=self.request.get("https://mmstoryglory.com/get-free-points?point-id=44&token=b20c73e9-0e1f-40ea-9363-4788d3240406")
            
            print(f":> attempt {c} complete check your points") if resp3.status_code == 200 else print(':>error occur ')

            time.sleep(300)
            c+=1

if __name__=="__main__":
    arg=argparse.ArgumentParser(description="-e = eamil | -p = password")
    arg.add_argument('--email','-e',type=str,help='user email')
    arg.add_argument('--password','-p',type=str,help='user password')
    var=arg.parse_args()
    a=main()

    a.attack(var.email,var.password)
 
