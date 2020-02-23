# 股票数据库：

* base 股票基本信息(市盈率、是否国企、行业、主营业务、省份)

* daily_history 股票每日交易信息

* cash_statement 现金流表

* balance_sheet 资产负债表

* income_statement 利润表

* ban 限售解禁表

## sql语句选股

1. 查询所有低价国企股

```sql
select avg(percent) from base where orgtype like '%国资%' and cur_price < 3.0 order by cur_price;
```

2. 查询猪相关股票

```sql
select * from base where majorbiz like '%猪%' or bizscope like '%猪%';
```

3. 查询白酒类今日平均涨幅

```
select avg(percent) from base where majorbiz like '%白酒%' or bizscope like '%白酒%';
```

