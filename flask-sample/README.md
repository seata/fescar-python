1. 安装依赖 requirements.txt
2. 增加pool_config.py文件
```
host = "localhost"
port = 3306
user = ""
password = ""
database = ""
```
3. 创建表
```
create table `test` (
  `id` int(11) not null auto_increment,
  `name` varchar(20),
  `created` datetime,
  primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `undo_log` (
  `branch_id` bigint(20) NOT NULL COMMENT 'branch transaction id',
  `xid` varchar(128) NOT NULL COMMENT 'global transaction id',
  `context` varchar(128) NOT NULL COMMENT 'undo_log context,such as serialization',
  `rollback_info` longblob NOT NULL COMMENT 'rollback info',
  `log_status` int(11) NOT NULL COMMENT '0:normal status,1:defense status',
  `log_created` datetime(6) NOT NULL COMMENT 'create datetime',
  `log_modified` datetime(6) NOT NULL COMMENT 'modify datetime',
  UNIQUE KEY `ux_undo_log` (`xid`,`branch_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='AT transaction mode undo table';
```
4. 启动flask_test.py
5. 启动flask_test2.py
6. 浏览器或者http工具访问
```
rollback
http://127.0.0.1:8001/hello2?e=true
commit
http://127.0.0.1:8001/hello2?e=false
```