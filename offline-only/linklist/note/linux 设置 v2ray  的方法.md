linux 设置 v2ray  的方法



安装客户端 

``` 
sudo snap install qv2ray

安装qv2ray：

如果想使用Terminal命令行安装Qv2ray，则需要借助snap这个依赖包。

1
sudo snap install qv2ray
安装完的路径在~/snap/qv2ray/中，可以打开qv2ray软件，在首选项—>内核设置中看到路径。

配置v2ray-core：

进入~/snap/qv2ray/3384/.config/qv2ray中，

1
2
3
cd ~/snap/qv2ray/3384/.config/qv2ray  #在首选项-->内核设置中看到路径
wget https://github.com/v2ray/v2ray-core/releases/download/v4.28.2/v2ray-linux-64.zip
unzip v2ray-linux-64.zip  -d vcore
最后，点击首选项—>内核设置里的检查V2Ray核心设置，确认是否配置成功。

导入连接：

利用之前windows的v2rayN导出url，然后在qv2ray首页，点击新建，输入一个名字，然后再链接中粘贴刚才导出的url，再点击导入即可。

打开连接：

选中刚才新建的连接，点击连接/断开按钮即可科学上网。


命令行设置代理

export http_proxy=http://proxyAddress:port

export http_proxy="http://127.0.0.1:8889"

git config --global http.proxy 'http://127.0.0.1:8889' 

```



