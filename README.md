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

# 波段操作股概览

### 粤传媒

性质：国企

板块: 传媒

对标：新华传媒

核心题材：创投(影谱科技)

周边题材：大湾区

重大事件：粤传媒由于收购案被立案调查，二审中

进货价 5.40

出货价 6.00

### 六国化工

性质：国企

板块: 化工

核心题材：磷矿、国企改革、化肥

重大事件：2018巨额亏损

进货价 4.10

出货价 4.50

### 比亚迪

核心题材：新能源电动车

进货价 40 ~ 50

出货价 55 ~ 60

### 万家乐

核心题材：超市

进货价: 3.20

出货价：4.00

### 招商银行

进货价：25.00

出货价：30.00

# 贸易战结束利好方向

1. 东南港口

2. 港口相关科技股

3. 5G
