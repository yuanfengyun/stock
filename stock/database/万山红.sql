
-- 万山红九不买
-- 1、不买私人老板的股票
-- 2、不买绩优成长股
-- 3、不买大小非的股票
-- 4、不买一年内离最低点40%的股票
-- 5、不买市净率大于4的股票
-- 6、不买无形资产大于有形资产的股票
-- 7、不买流动比率小于2，速动比率小于1的股票
-- 8、不买有过污点的股票
-- 9、不买等待增发的股票

SELECT count(*) FROM base WHERE orgtype != "民营企业" and orgtype != "外资企业" and cur_price/low52w < 1.4 and pb < 4 and float_market_capital/market_capital > 0.5

select * from base where majorbiz like "%制氧%"

truncate ban;