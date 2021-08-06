# Ubuntu设置终端走代理

 发表于 2020-07-26 | 分类于 [UBuntu](https://www.windsings.com/categories/UBuntu/) | [评论数： 0](https://www.windsings.com/posts/3c42339d/#comments)

Ubuntu设置终端走代理



# 方法一

如果默认是socket5通信且端口是1080,即127.0.01:1080的方式

使用如下两种方式

```
socks5://127.0.0.1:1080
```

这里无关自己代理客户端是不是SSR或SS只要是通过socket通信即可,前提是满足已经能够正常代理访问.

第二种是http代理,即通信方式为http而不是socket

```
http://127.0.0.1:12333
```

![img](https://www.windsings.com/posts/3c42339d/clip_image001.jpg)

在终端中直接运行：

```
export http_proxy=http://proxyAddress:port
```

如果你是SSR,并且走的http的代理端口是12333，想执行wget或者curl来下载国外的东西，可以使用如下命令：



```
export http_proxy=http://127.0.0.1:12333
```



如果是https那么就经过如下命令：



```
export https_proxy=http://127.0.0.1:12333
```



# 方法二

这个办法的好处是把代理服务器永久保存了，下次就可以直接用了

把代理服务器地址写入shell配置文件.bashrc或者.zshrc 直接在.bashrc或者.zshrc添加下面内容



```
export http_proxy="http://localhost:port"
export https_proxy="http://localhost:port"
```



或者走socket5协议（ss,ssr）的话，代理端口是1080



```
export http_proxy="socks5://127.0.0.1:1080"

export https_proxy="socks5://127.0.0.1:1080"
```



或者干脆直接设置ALL_PROXY

```
export ALL_PROXY=socks5://127.0.0.1:1080
```

最后在执行如下命令应用设置



```
source ~/.bashrc
```



或者通过设置alias简写来简化操作，每次要用的时候输入setproxy，不用了就unsetproxy。



```
alias setproxy="export ALL_PROXY=socks5://127.0.0.1:1080" alias unsetproxy="unset ALL_PROXY"
```



# 方法三

改相应工具的配置，比如apt的配置



```
sudo vim /etc/apt/apt.conf
```



在文件末尾加入下面这行



```
Acquire::http::Proxy "<http://proxyAddress:port>"
```



重点来了！！如果说经常使用git对于其他方面都不是经常使用，可以直接配置git的命令。

使用ss/ssr来加快git的速度

直接输入这个命令就好了



```
git config --global http.proxy 'socks5://127.0.0.1:1080' 

git config --global https.proxy 'socks5://127.0.0.1:1080'
```



# 测试

使用`curl ifconfig.me`会返回出口的公网IP

使用`curl www.google.com`会向谷歌发送get请求，如果出来一堆，那就说明翻墙成功，如果长时间没有任何输出，则是继续被墙。

如果是设置的`export http_proxy=http://.....`可以使用

```
echo $http_proxy
```

来查看当前的http proxy

# 参考

https://zhuanlan.zhihu.com/p/46973701