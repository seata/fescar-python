# seata-python

seata-python是一个seata分布式事务python版本的客户端，什么是seata访问https://seata.io

## 项目介绍
本人不是python开发者，主要是为了学习一下python才写的这个项目，目前项目还没有写完，主要是完成seata AT模式
项目里面有很多实现不合理的地方，欢迎各位大佬前来修改。谢谢！

## 项目完成度
1. seata-server 网络协议模块
  - [x] TCP协议
  - [ ] socket优化
2. 封装Connection, Cursor处理前后置镜像
  - [x] insert
  - [x] delete
  - [x] update
3. 解析 sql 模块
  - [x] insert
  - [x] delete
  - [x] update
  - [x] select for update
4. undo 回滚模块
  - [x] insert
  - [x] delete
  - [x] update
5. 优化代码结构
  - [ ] TMClient 结构
  - [ ] RMClient 结构
  - [ ] 项目整体结构
6. 配置集成
  - [x] file
  - [ ] nacos
7. 其他
  - [ ] 其他数据库
  - [ ] GRPC 协议
  - [ ] 等等

## 项目依赖
```
Python3.7

test:
PyMySQL==1.0.2
```

## pip源配置
```
https://pypi.org/simple 默认
https://pypi.tuna.tsinghua.edu.cn/simple/
```