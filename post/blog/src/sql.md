# SQL 语句的分类

- 日期：2020-03-09

## 语句分类

1. **DDL 语句**——数据定义
2. **DML 语句**——数据操纵
3. **DQL 语句**——数据查询

**DDL 语句**：对数据库、表、视图、索引、存储过程进行定义。

> create table/database table_name/database_name (字段名 属性 , 字段名 属性 , ……);
>
> drop  
> 删除数据库或数据表
>
> alter  
> 可以增加,修改,删除数据  
> 增加字段—alter table table_name add 字段名 属性;  
> 修改字段—alter table table_name change 旧字段名 新字段名 属性 ;  
> 修改表名—alter table table_name rename to 新表名;  
> 删除字段—alter table table_name drop 字段名

**DML 语句**：插入数据 INSERT、删除数据 DELETE、更新数据 UPDATE。  
>insert  
>  
>向数据表插入数据  
>insert into table_name values(插入的数据) , () , () , …… ;

> delete  
> 删除数据  
> delete from table_name where 字段名=“某一具体的值”;
>
> update  
> update table_name set 字段名=“某一具体的值” where 加限定条件;

**DQL 语句**：数据库查询语句，查询数据 SELECT。  
>select  
>select语句可以根据子条件进行多样查询,有简单的查询,也有嵌套查询或者是联合多表查询  
>![SQL 查询示意图](/post/blog/img/sql-1.jpg)  
>

**DCL 语句**：数据库控制语句，控制用户的访问权限 GRANT、REVOKE。  
>commit , rollback , grant  
>

---
