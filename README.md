# seata-python

seata-python是一个seata分布式事务python版本的客户端，什么是seata访问https://seata.io

## 项目介绍
本人不是python开发者，主要是为了学习一下python才写的这个项目，目前项目还没有写完，主要是完成seata AT模式
项目里面有很多实现不合理的地方，欢迎各位大佬前来修改。谢谢！

## 项目完成度
1. seata-server 网络协议模块 (完成)
2. 封装Connection, Cursor处理前后置镜像 (进行中)
3. 解析sql模块 (未开始)
4. 优化TMClient, RMClient (未开始)

## 项目依赖
```
DBUtils(PooledDB)==2.0
antlr4-python3-runtime==4.9.2
protobuf==3.17.3
gevent==21.8.0

test:
mariadb==1.0.5
PyMySQL==1.0.2
```

## pip源配置
```
https://pypi.org/simple 默认
https://pypi.tuna.tsinghua.edu.cn/simple/
```