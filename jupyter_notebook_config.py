# 局域网访问jupyter notebook
1. 执行如下命令
jupyter notebook --generate-config

2.在生成的配置文件中添加如下：

c.ServerApp.ip = '0.0.0.0'
c.ServerApp.port = 8888
c.ServerApp.open_browser = False
c.ServerApp.allow_origin = '*'
c.ServerApp.token = ''
c.ServerApp.password = ''
