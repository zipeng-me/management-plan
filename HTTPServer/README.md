原理性理解：
结构:
               |--httpserver --HttpServer.py (主程序)
               |             --settings (httpserver配置)
               |   
  project--|
               |
               |
               |--WebFrame --static （存放静态网页）
                           --views.py （ 应用处理程序） 
                           --urls.py （存放路由）
                           --settings （框架配置）
                           --WebFrame.py (主程序代码)