manager shell 是一个 大马：lionaneesh/lionaneesh

Publishb.php     weekly 生成的， 密码为：32150d1a0dfece88

publishr.php  是msfveom生成的，用于反弹shell，这个还是最好还是使用msf 的 meterpreter的脚本进行反弹shell的监听，主要是 方便

.low_warm.php  执行之后会在每个目录下生成 Publishb.php  这个weekly 利用后门

.good.php   是常规后门，可通过 蚁剑进行连接，连接url ： http://ip:port/good.php?pass=cyber_S_A_L   在post cmd 参数

.warm 蠕虫病毒，还没有经过验证

.no_dead.php 这是不死马，中间的shell_code 就是生成一句话木马的base64之后的内容，可以进行更改。杀不死马的手段。1、重启服务（一般是无权限的），2、关进程，有风险。 3、 生成木马一样名字的 文件夹，一定文件夹，可以写个脚本反复生成。

tuma  文件夹就是存放常规的图马
