## Ask For pandas  熊猫问答
###  是由本作者[assasin0308@sina.com]()开发的一个线上问答平台

### Flask迁移三部曲
```txt
   1. flask db init: 执行一次生成迁移目录
   2. flask db migrate: 识别ORM模型改变,生成迁移脚本
   3. flask db upgrade: 运行迁移脚本,同步数据库
```
   