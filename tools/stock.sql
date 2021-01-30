# Host: 120.79.91.100  (Version 5.7.20-0ubuntu0.16.04.1)
# Date: 2019-03-07 00:41:42
# Generator: MySQL-Front 6.1  (Build 1.26)


#
# Structure for table "balance_sheet"
#

CREATE TABLE `balance_sheet` (
  `id` varchar(20) NOT NULL DEFAULT '0',
  `publishdate` date DEFAULT NULL,
  `reportdate` date NOT NULL,
  `curfds` bigint(20) DEFAULT '0',
  `tradfinasset` bigint(20) DEFAULT '0',
  `notesrece` bigint(20) DEFAULT '0',
  `accorece` bigint(20) DEFAULT '0',
  `prep` bigint(20) DEFAULT '0',
  `dividrece` bigint(20) DEFAULT '0',
  `inve` bigint(20) DEFAULT '0',
  `othercurrasse` bigint(20) DEFAULT '0',
  `totcurrasset` bigint(20) DEFAULT '0',
  `longrece` bigint(20) DEFAULT '0',
  `equiinve` bigint(20) DEFAULT '0',
  `fixedassenet` bigint(20) DEFAULT '0',
  `consprog` bigint(20) DEFAULT '0',
  `intaasset` bigint(20) DEFAULT '0',
  `logprepexpe` bigint(20) DEFAULT '0',
  `defetaxasset` bigint(20) DEFAULT '0',
  `othernoncasse` bigint(20) DEFAULT '0',
  `totalnoncassets` bigint(20) DEFAULT '0',
  `totasset` bigint(20) DEFAULT '0',
  `shorttermborr` bigint(20) DEFAULT '0',
  `copeworkersal` bigint(20) DEFAULT '0',
  `taxespaya` bigint(20) DEFAULT '0',
  `intepaya` bigint(20) DEFAULT '0',
  `duenoncliab` bigint(20) DEFAULT '0',
  `totalcurrliab` bigint(20) DEFAULT '0',
  `longborr` bigint(20) DEFAULT '0',
  `longdefeinco` bigint(20) DEFAULT '0',
  `othernoncliabi` bigint(20) DEFAULT '0',
  `totalnoncliab` bigint(20) DEFAULT '0',
  `totliab` bigint(20) DEFAULT '0',
  `paidincapi` bigint(20) DEFAULT '0',
  `capisurp` bigint(20) DEFAULT '0',
  `rese` bigint(20) DEFAULT '0',
  `undiprof` bigint(20) DEFAULT '0',
  `paresharrigh` bigint(20) DEFAULT '0',
  `minysharrigh` bigint(20) DEFAULT '0',
  `righaggr` bigint(20) DEFAULT '0',
  `totliabsharequi` bigint(20) DEFAULT '0',
  PRIMARY KEY (`id`,`reportdate`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Structure for table "ban"
#

CREATE TABLE `ban` (
  `id` varchar(20) NOT NULL DEFAULT '',
  `holder_name` varchar(255) NOT NULL DEFAULT '',
  `date` bigint(20) DEFAULT NULL,
  `num` bigint(20) DEFAULT NULL,
  `type` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Structure for table "base"
#

CREATE TABLE `base` (
  `id` varchar(11) NOT NULL DEFAULT '',
  `name` varchar(255) NOT NULL DEFAULT '',
  `cur_price` float NOT NULL DEFAULT '0',
  `percent` float(11,4) NOT NULL DEFAULT '0.0000',
  `high52w` float NOT NULL DEFAULT '0' COMMENT '52周最高价',
  `low52w` float NOT NULL DEFAULT '0' COMMENT '52周最低价',
  `ttm` float NOT NULL DEFAULT '0' COMMENT '市盈率',
  `market_capital` float NOT NULL DEFAULT '0' COMMENT '市值',
  `float_market_capital` double(20,4) NOT NULL DEFAULT '0.0000',
  `industry` varchar(255) NOT NULL DEFAULT '' COMMENT '行业',
  `intro` varchar(1024) NOT NULL DEFAULT '' COMMENT '简介',
  `orgtype` varchar(255) NOT NULL DEFAULT '' COMMENT '国企，地方国企，私企',
  `province` varchar(255) NOT NULL DEFAULT '',
  `city` varchar(255) NOT NULL DEFAULT '',
  `compintro` varchar(4096) DEFAULT NULL,
  `bizscope` varchar(4096) DEFAULT NULL,
  `majorbiz` varchar(4096) DEFAULT NULL,
  `compname` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Structure for table "cash_statement"
#

CREATE TABLE `cash_statement` (
  `id` varchar(20) DEFAULT NULL,
  `begindate` date DEFAULT NULL,
  `enddate` date DEFAULT NULL,
  `laborgetcash` bigint(20) DEFAULT NULL,
  `deponetr` bigint(20) DEFAULT NULL,
  `bankloannetincr` bigint(20) DEFAULT NULL,
  `fininstnetr` bigint(20) DEFAULT NULL,
  `inspremcash` bigint(20) DEFAULT NULL,
  `insnetc` bigint(20) DEFAULT NULL,
  `savinetr` bigint(20) DEFAULT NULL,
  `disptradnetincr` bigint(20) DEFAULT NULL,
  `charintecash` bigint(20) DEFAULT NULL,
  `fdsborrnetr` bigint(20) DEFAULT NULL,
  `repnetincr` bigint(20) DEFAULT NULL,
  `taxrefd` bigint(20) DEFAULT NULL,
  `receotherbizcash` bigint(20) DEFAULT NULL,
  `bizinflitse` bigint(20) DEFAULT NULL,
  `bizinflform` bigint(20) DEFAULT NULL,
  `bizcashinfl` bigint(20) DEFAULT NULL,
  `labopayc` bigint(20) DEFAULT NULL,
  `loansnetr` bigint(20) DEFAULT NULL,
  `tradepaymnetr` bigint(20) DEFAULT NULL,
  `paycompgold` bigint(20) DEFAULT NULL,
  `payintecash` bigint(20) DEFAULT NULL,
  `paydivicash` bigint(20) DEFAULT NULL,
  `payworkcash` bigint(20) DEFAULT NULL,
  `paytax` bigint(20) DEFAULT NULL,
  `payacticash` bigint(20) DEFAULT NULL,
  `bizoutfitse` bigint(20) DEFAULT NULL,
  `bizoutfform` bigint(20) DEFAULT NULL,
  `bizcashoutf` bigint(20) DEFAULT NULL,
  `biznetitse` bigint(20) DEFAULT NULL,
  `biznetform` bigint(20) DEFAULT NULL,
  `mananetr` bigint(20) DEFAULT NULL,
  `withinvgetcash` bigint(20) DEFAULT NULL,
  `inveretugetcash` bigint(20) DEFAULT NULL,
  `fixedassetnetc` bigint(20) DEFAULT NULL,
  `subsnetc` bigint(20) DEFAULT NULL,
  `receinvcash` bigint(20) DEFAULT NULL,
  `reducashpled` bigint(20) DEFAULT NULL,
  `invinflitse` bigint(20) DEFAULT NULL,
  `invinffrom` bigint(20) DEFAULT NULL,
  `invcashinfl` bigint(20) DEFAULT NULL,
  `acquassetcash` bigint(20) DEFAULT NULL,
  `invpayc` bigint(20) DEFAULT NULL,
  `loannetr` bigint(20) DEFAULT NULL,
  `subspaynetcash` bigint(20) DEFAULT NULL,
  `payinvecash` bigint(20) DEFAULT NULL,
  `incrcashpled` bigint(20) DEFAULT NULL,
  `invoutfitse` bigint(20) DEFAULT NULL,
  `invoutfform` bigint(20) DEFAULT NULL,
  `invcashoutf` bigint(20) DEFAULT NULL,
  `netinvitse` bigint(20) DEFAULT NULL,
  `netinvform` bigint(20) DEFAULT NULL,
  `invnetcashflow` bigint(20) DEFAULT NULL,
  `invrececash` bigint(20) DEFAULT NULL,
  `subsrececash` bigint(20) DEFAULT NULL,
  `recefromloan` bigint(20) DEFAULT NULL,
  `issbdrececash` bigint(20) DEFAULT NULL,
  `recefincash` bigint(20) DEFAULT NULL,
  `fininflitse` bigint(20) DEFAULT NULL,
  `fininflform` bigint(20) DEFAULT NULL,
  `fincashinfl` bigint(20) DEFAULT NULL,
  `debtpaycash` bigint(20) DEFAULT NULL,
  `diviprofpaycash` bigint(20) DEFAULT NULL,
  `subspaydivid` bigint(20) DEFAULT NULL,
  `finrelacash` bigint(20) DEFAULT NULL,
  `finoutfitse` bigint(20) DEFAULT NULL,
  `finoutfform` bigint(20) DEFAULT NULL,
  `fincashoutf` bigint(20) DEFAULT NULL,
  `finnetitse` bigint(20) DEFAULT NULL,
  `finnetform` bigint(20) DEFAULT NULL,
  `finnetcflow` bigint(20) DEFAULT NULL,
  `chgexchgchgs` bigint(20) DEFAULT NULL,
  `netcashitse` bigint(20) DEFAULT NULL,
  `netcashform` bigint(20) DEFAULT NULL,
  `cashnetr` bigint(20) DEFAULT NULL,
  `inicashbala` bigint(20) DEFAULT NULL,
  `cashfinalitse` bigint(20) DEFAULT NULL,
  `cashfinalform` bigint(20) DEFAULT NULL,
  `finalcashbala` bigint(20) DEFAULT NULL,
  `netprofit` bigint(20) DEFAULT NULL,
  `minysharrigh` bigint(20) DEFAULT NULL,
  `unreinveloss` bigint(20) DEFAULT NULL,
  `asseimpa` bigint(20) DEFAULT NULL,
  `assedepr` bigint(20) DEFAULT NULL,
  `realestadep` bigint(20) DEFAULT NULL,
  `intaasseamor` bigint(20) DEFAULT NULL,
  `longdefeexpenamor` bigint(20) DEFAULT NULL,
  `prepexpedecr` bigint(20) DEFAULT NULL,
  `accrexpeincr` bigint(20) DEFAULT NULL,
  `dispfixedassetloss` bigint(20) DEFAULT NULL,
  `fixedassescraloss` bigint(20) DEFAULT NULL,
  `valuechgloss` bigint(20) DEFAULT NULL,
  `defeincoincr` bigint(20) DEFAULT NULL,
  `estidebts` bigint(20) DEFAULT NULL,
  `finexpe` bigint(20) DEFAULT NULL,
  `inveloss` bigint(20) DEFAULT NULL,
  `defetaxassetdecr` bigint(20) DEFAULT NULL,
  `defetaxliabincr` bigint(20) DEFAULT NULL,
  `inveredu` bigint(20) DEFAULT NULL,
  `receredu` bigint(20) DEFAULT NULL,
  `payaincr` bigint(20) DEFAULT NULL,
  `unseparachg` bigint(20) DEFAULT NULL,
  `unfiparachg` bigint(20) DEFAULT NULL,
  `other` bigint(20) DEFAULT NULL,
  `biznetscheitse` bigint(20) DEFAULT NULL,
  `biznetscheform` bigint(20) DEFAULT NULL,
  `biznetcflow` bigint(20) DEFAULT NULL,
  `debtintocapi` bigint(20) DEFAULT NULL,
  `expiconvbd` bigint(20) DEFAULT NULL,
  `finfixedasset` bigint(20) DEFAULT NULL,
  `cashfinalbala` bigint(20) DEFAULT NULL,
  `cashopenbala` bigint(20) DEFAULT NULL,
  `equfinalbala` bigint(20) DEFAULT NULL,
  `equopenbala` bigint(20) DEFAULT NULL,
  `netcashscheitse` bigint(20) DEFAULT NULL,
  `netcashscheform` bigint(20) DEFAULT NULL,
  `cashneti` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Structure for table "daily_history_1"
#

CREATE TABLE `daily_history_1` (
  `id` varchar(20) NOT NULL,
  `volume` double(20,4) DEFAULT NULL,
  `open` double(20,4) DEFAULT NULL,
  `high` double(20,4) DEFAULT NULL,
  `close` double(20,4) DEFAULT NULL,
  `low` double(20,4) DEFAULT NULL,
  `chg` double(20,4) DEFAULT NULL,
  `percent` double(20,4) DEFAULT NULL,
  `turnrate` double(20,4) DEFAULT NULL,
  `ma5` double(20,4) DEFAULT NULL,
  `ma10` double(20,4) DEFAULT NULL,
  `ma20` double(20,4) DEFAULT NULL,
  `ma30` double(20,4) DEFAULT NULL,
  `dif` double(20,4) DEFAULT NULL,
  `dea` double(20,4) DEFAULT NULL,
  `macd` double(20,4) DEFAULT NULL,
  `lot_volume` double(20,4) DEFAULT NULL,
  `timestamp` bigint(20) NOT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`,`timestamp`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

#
# Structure for table "daily_history_10"
#

CREATE TABLE `daily_history_10` (
  `id` varchar(20) NOT NULL,
  `volume` double(20,4) DEFAULT NULL,
  `open` double(20,4) DEFAULT NULL,
  `high` double(20,4) DEFAULT NULL,
  `close` double(20,4) DEFAULT NULL,
  `low` double(20,4) DEFAULT NULL,
  `chg` double(20,4) DEFAULT NULL,
  `percent` double(20,4) DEFAULT NULL,
  `turnrate` double(20,4) DEFAULT NULL,
  `ma5` double(20,4) DEFAULT NULL,
  `ma10` double(20,4) DEFAULT NULL,
  `ma20` double(20,4) DEFAULT NULL,
  `ma30` double(20,4) DEFAULT NULL,
  `dif` double(20,4) DEFAULT NULL,
  `dea` double(20,4) DEFAULT NULL,
  `macd` double(20,4) DEFAULT NULL,
  `lot_volume` double(20,4) DEFAULT NULL,
  `timestamp` bigint(20) NOT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`,`timestamp`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

#
# Structure for table "daily_history_11"
#

CREATE TABLE `daily_history_11` (
  `id` varchar(20) NOT NULL,
  `volume` double(20,4) DEFAULT NULL,
  `open` double(20,4) DEFAULT NULL,
  `high` double(20,4) DEFAULT NULL,
  `close` double(20,4) DEFAULT NULL,
  `low` double(20,4) DEFAULT NULL,
  `chg` double(20,4) DEFAULT NULL,
  `percent` double(20,4) DEFAULT NULL,
  `turnrate` double(20,4) DEFAULT NULL,
  `ma5` double(20,4) DEFAULT NULL,
  `ma10` double(20,4) DEFAULT NULL,
  `ma20` double(20,4) DEFAULT NULL,
  `ma30` double(20,4) DEFAULT NULL,
  `dif` double(20,4) DEFAULT NULL,
  `dea` double(20,4) DEFAULT NULL,
  `macd` double(20,4) DEFAULT NULL,
  `lot_volume` double(20,4) DEFAULT NULL,
  `timestamp` bigint(20) NOT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`,`timestamp`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

#
# Structure for table "daily_history_12"
#

CREATE TABLE `daily_history_12` (
  `id` varchar(20) NOT NULL,
  `volume` double(20,4) DEFAULT NULL,
  `open` double(20,4) DEFAULT NULL,
  `high` double(20,4) DEFAULT NULL,
  `close` double(20,4) DEFAULT NULL,
  `low` double(20,4) DEFAULT NULL,
  `chg` double(20,4) DEFAULT NULL,
  `percent` double(20,4) DEFAULT NULL,
  `turnrate` double(20,4) DEFAULT NULL,
  `ma5` double(20,4) DEFAULT NULL,
  `ma10` double(20,4) DEFAULT NULL,
  `ma20` double(20,4) DEFAULT NULL,
  `ma30` double(20,4) DEFAULT NULL,
  `dif` double(20,4) DEFAULT NULL,
  `dea` double(20,4) DEFAULT NULL,
  `macd` double(20,4) DEFAULT NULL,
  `lot_volume` double(20,4) DEFAULT NULL,
  `timestamp` bigint(20) NOT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`,`timestamp`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

#
# Structure for table "daily_history_13"
#

CREATE TABLE `daily_history_13` (
  `id` varchar(20) NOT NULL,
  `volume` double(20,4) DEFAULT NULL,
  `open` double(20,4) DEFAULT NULL,
  `high` double(20,4) DEFAULT NULL,
  `close` double(20,4) DEFAULT NULL,
  `low` double(20,4) DEFAULT NULL,
  `chg` double(20,4) DEFAULT NULL,
  `percent` double(20,4) DEFAULT NULL,
  `turnrate` double(20,4) DEFAULT NULL,
  `ma5` double(20,4) DEFAULT NULL,
  `ma10` double(20,4) DEFAULT NULL,
  `ma20` double(20,4) DEFAULT NULL,
  `ma30` double(20,4) DEFAULT NULL,
  `dif` double(20,4) DEFAULT NULL,
  `dea` double(20,4) DEFAULT NULL,
  `macd` double(20,4) DEFAULT NULL,
  `lot_volume` double(20,4) DEFAULT NULL,
  `timestamp` bigint(20) NOT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`,`timestamp`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

#
# Structure for table "daily_history_14"
#

CREATE TABLE `daily_history_14` (
  `id` varchar(20) NOT NULL,
  `volume` double(20,4) DEFAULT NULL,
  `open` double(20,4) DEFAULT NULL,
  `high` double(20,4) DEFAULT NULL,
  `close` double(20,4) DEFAULT NULL,
  `low` double(20,4) DEFAULT NULL,
  `chg` double(20,4) DEFAULT NULL,
  `percent` double(20,4) DEFAULT NULL,
  `turnrate` double(20,4) DEFAULT NULL,
  `ma5` double(20,4) DEFAULT NULL,
  `ma10` double(20,4) DEFAULT NULL,
  `ma20` double(20,4) DEFAULT NULL,
  `ma30` double(20,4) DEFAULT NULL,
  `dif` double(20,4) DEFAULT NULL,
  `dea` double(20,4) DEFAULT NULL,
  `macd` double(20,4) DEFAULT NULL,
  `lot_volume` double(20,4) DEFAULT NULL,
  `timestamp` bigint(20) NOT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`,`timestamp`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

#
# Structure for table "daily_history_15"
#

CREATE TABLE `daily_history_15` (
  `id` varchar(20) NOT NULL,
  `volume` double(20,4) DEFAULT NULL,
  `open` double(20,4) DEFAULT NULL,
  `high` double(20,4) DEFAULT NULL,
  `close` double(20,4) DEFAULT NULL,
  `low` double(20,4) DEFAULT NULL,
  `chg` double(20,4) DEFAULT NULL,
  `percent` double(20,4) DEFAULT NULL,
  `turnrate` double(20,4) DEFAULT NULL,
  `ma5` double(20,4) DEFAULT NULL,
  `ma10` double(20,4) DEFAULT NULL,
  `ma20` double(20,4) DEFAULT NULL,
  `ma30` double(20,4) DEFAULT NULL,
  `dif` double(20,4) DEFAULT NULL,
  `dea` double(20,4) DEFAULT NULL,
  `macd` double(20,4) DEFAULT NULL,
  `lot_volume` double(20,4) DEFAULT NULL,
  `timestamp` bigint(20) NOT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`,`timestamp`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

#
# Structure for table "daily_history_16"
#

CREATE TABLE `daily_history_16` (
  `id` varchar(20) NOT NULL,
  `volume` double(20,4) DEFAULT NULL,
  `open` double(20,4) DEFAULT NULL,
  `high` double(20,4) DEFAULT NULL,
  `close` double(20,4) DEFAULT NULL,
  `low` double(20,4) DEFAULT NULL,
  `chg` double(20,4) DEFAULT NULL,
  `percent` double(20,4) DEFAULT NULL,
  `turnrate` double(20,4) DEFAULT NULL,
  `ma5` double(20,4) DEFAULT NULL,
  `ma10` double(20,4) DEFAULT NULL,
  `ma20` double(20,4) DEFAULT NULL,
  `ma30` double(20,4) DEFAULT NULL,
  `dif` double(20,4) DEFAULT NULL,
  `dea` double(20,4) DEFAULT NULL,
  `macd` double(20,4) DEFAULT NULL,
  `lot_volume` double(20,4) DEFAULT NULL,
  `timestamp` bigint(20) NOT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`,`timestamp`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

#
# Structure for table "daily_history_17"
#

CREATE TABLE `daily_history_17` (
  `id` varchar(20) NOT NULL,
  `volume` double(20,4) DEFAULT NULL,
  `open` double(20,4) DEFAULT NULL,
  `high` double(20,4) DEFAULT NULL,
  `close` double(20,4) DEFAULT NULL,
  `low` double(20,4) DEFAULT NULL,
  `chg` double(20,4) DEFAULT NULL,
  `percent` double(20,4) DEFAULT NULL,
  `turnrate` double(20,4) DEFAULT NULL,
  `ma5` double(20,4) DEFAULT NULL,
  `ma10` double(20,4) DEFAULT NULL,
  `ma20` double(20,4) DEFAULT NULL,
  `ma30` double(20,4) DEFAULT NULL,
  `dif` double(20,4) DEFAULT NULL,
  `dea` double(20,4) DEFAULT NULL,
  `macd` double(20,4) DEFAULT NULL,
  `lot_volume` double(20,4) DEFAULT NULL,
  `timestamp` bigint(20) NOT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`,`timestamp`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

#
# Structure for table "daily_history_18"
#

CREATE TABLE `daily_history_18` (
  `id` varchar(20) NOT NULL,
  `volume` double(20,4) DEFAULT NULL,
  `open` double(20,4) DEFAULT NULL,
  `high` double(20,4) DEFAULT NULL,
  `close` double(20,4) DEFAULT NULL,
  `low` double(20,4) DEFAULT NULL,
  `chg` double(20,4) DEFAULT NULL,
  `percent` double(20,4) DEFAULT NULL,
  `turnrate` double(20,4) DEFAULT NULL,
  `ma5` double(20,4) DEFAULT NULL,
  `ma10` double(20,4) DEFAULT NULL,
  `ma20` double(20,4) DEFAULT NULL,
  `ma30` double(20,4) DEFAULT NULL,
  `dif` double(20,4) DEFAULT NULL,
  `dea` double(20,4) DEFAULT NULL,
  `macd` double(20,4) DEFAULT NULL,
  `lot_volume` double(20,4) DEFAULT NULL,
  `timestamp` bigint(20) NOT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`,`timestamp`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

#
# Structure for table "daily_history_19"
#

CREATE TABLE `daily_history_19` (
  `id` varchar(20) NOT NULL,
  `volume` double(20,4) DEFAULT NULL,
  `open` double(20,4) DEFAULT NULL,
  `high` double(20,4) DEFAULT NULL,
  `close` double(20,4) DEFAULT NULL,
  `low` double(20,4) DEFAULT NULL,
  `chg` double(20,4) DEFAULT NULL,
  `percent` double(20,4) DEFAULT NULL,
  `turnrate` double(20,4) DEFAULT NULL,
  `ma5` double(20,4) DEFAULT NULL,
  `ma10` double(20,4) DEFAULT NULL,
  `ma20` double(20,4) DEFAULT NULL,
  `ma30` double(20,4) DEFAULT NULL,
  `dif` double(20,4) DEFAULT NULL,
  `dea` double(20,4) DEFAULT NULL,
  `macd` double(20,4) DEFAULT NULL,
  `lot_volume` double(20,4) DEFAULT NULL,
  `timestamp` bigint(20) NOT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`,`timestamp`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

#
# Structure for table "daily_history_2"
#

CREATE TABLE `daily_history_2` (
  `id` varchar(20) NOT NULL,
  `volume` double(20,4) DEFAULT NULL,
  `open` double(20,4) DEFAULT NULL,
  `high` double(20,4) DEFAULT NULL,
  `close` double(20,4) DEFAULT NULL,
  `low` double(20,4) DEFAULT NULL,
  `chg` double(20,4) DEFAULT NULL,
  `percent` double(20,4) DEFAULT NULL,
  `turnrate` double(20,4) DEFAULT NULL,
  `ma5` double(20,4) DEFAULT NULL,
  `ma10` double(20,4) DEFAULT NULL,
  `ma20` double(20,4) DEFAULT NULL,
  `ma30` double(20,4) DEFAULT NULL,
  `dif` double(20,4) DEFAULT NULL,
  `dea` double(20,4) DEFAULT NULL,
  `macd` double(20,4) DEFAULT NULL,
  `lot_volume` double(20,4) DEFAULT NULL,
  `timestamp` bigint(20) NOT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`,`timestamp`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

#
# Structure for table "daily_history_20"
#

CREATE TABLE `daily_history_20` (
  `id` varchar(20) NOT NULL,
  `volume` double(20,4) DEFAULT NULL,
  `open` double(20,4) DEFAULT NULL,
  `high` double(20,4) DEFAULT NULL,
  `close` double(20,4) DEFAULT NULL,
  `low` double(20,4) DEFAULT NULL,
  `chg` double(20,4) DEFAULT NULL,
  `percent` double(20,4) DEFAULT NULL,
  `turnrate` double(20,4) DEFAULT NULL,
  `ma5` double(20,4) DEFAULT NULL,
  `ma10` double(20,4) DEFAULT NULL,
  `ma20` double(20,4) DEFAULT NULL,
  `ma30` double(20,4) DEFAULT NULL,
  `dif` double(20,4) DEFAULT NULL,
  `dea` double(20,4) DEFAULT NULL,
  `macd` double(20,4) DEFAULT NULL,
  `lot_volume` double(20,4) DEFAULT NULL,
  `timestamp` bigint(20) NOT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`,`timestamp`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

#
# Structure for table "daily_history_3"
#

CREATE TABLE `daily_history_3` (
  `id` varchar(20) NOT NULL,
  `volume` double(20,4) DEFAULT NULL,
  `open` double(20,4) DEFAULT NULL,
  `high` double(20,4) DEFAULT NULL,
  `close` double(20,4) DEFAULT NULL,
  `low` double(20,4) DEFAULT NULL,
  `chg` double(20,4) DEFAULT NULL,
  `percent` double(20,4) DEFAULT NULL,
  `turnrate` double(20,4) DEFAULT NULL,
  `ma5` double(20,4) DEFAULT NULL,
  `ma10` double(20,4) DEFAULT NULL,
  `ma20` double(20,4) DEFAULT NULL,
  `ma30` double(20,4) DEFAULT NULL,
  `dif` double(20,4) DEFAULT NULL,
  `dea` double(20,4) DEFAULT NULL,
  `macd` double(20,4) DEFAULT NULL,
  `lot_volume` double(20,4) DEFAULT NULL,
  `timestamp` bigint(20) NOT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`,`timestamp`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

#
# Structure for table "daily_history_4"
#

CREATE TABLE `daily_history_4` (
  `id` varchar(20) NOT NULL,
  `volume` double(20,4) DEFAULT NULL,
  `open` double(20,4) DEFAULT NULL,
  `high` double(20,4) DEFAULT NULL,
  `close` double(20,4) DEFAULT NULL,
  `low` double(20,4) DEFAULT NULL,
  `chg` double(20,4) DEFAULT NULL,
  `percent` double(20,4) DEFAULT NULL,
  `turnrate` double(20,4) DEFAULT NULL,
  `ma5` double(20,4) DEFAULT NULL,
  `ma10` double(20,4) DEFAULT NULL,
  `ma20` double(20,4) DEFAULT NULL,
  `ma30` double(20,4) DEFAULT NULL,
  `dif` double(20,4) DEFAULT NULL,
  `dea` double(20,4) DEFAULT NULL,
  `macd` double(20,4) DEFAULT NULL,
  `lot_volume` double(20,4) DEFAULT NULL,
  `timestamp` bigint(20) NOT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`,`timestamp`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

#
# Structure for table "daily_history_5"
#

CREATE TABLE `daily_history_5` (
  `id` varchar(20) NOT NULL,
  `volume` double(20,4) DEFAULT NULL,
  `open` double(20,4) DEFAULT NULL,
  `high` double(20,4) DEFAULT NULL,
  `close` double(20,4) DEFAULT NULL,
  `low` double(20,4) DEFAULT NULL,
  `chg` double(20,4) DEFAULT NULL,
  `percent` double(20,4) DEFAULT NULL,
  `turnrate` double(20,4) DEFAULT NULL,
  `ma5` double(20,4) DEFAULT NULL,
  `ma10` double(20,4) DEFAULT NULL,
  `ma20` double(20,4) DEFAULT NULL,
  `ma30` double(20,4) DEFAULT NULL,
  `dif` double(20,4) DEFAULT NULL,
  `dea` double(20,4) DEFAULT NULL,
  `macd` double(20,4) DEFAULT NULL,
  `lot_volume` double(20,4) DEFAULT NULL,
  `timestamp` bigint(20) NOT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`,`timestamp`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

#
# Structure for table "daily_history_6"
#

CREATE TABLE `daily_history_6` (
  `id` varchar(20) NOT NULL,
  `volume` double(20,4) DEFAULT NULL,
  `open` double(20,4) DEFAULT NULL,
  `high` double(20,4) DEFAULT NULL,
  `close` double(20,4) DEFAULT NULL,
  `low` double(20,4) DEFAULT NULL,
  `chg` double(20,4) DEFAULT NULL,
  `percent` double(20,4) DEFAULT NULL,
  `turnrate` double(20,4) DEFAULT NULL,
  `ma5` double(20,4) DEFAULT NULL,
  `ma10` double(20,4) DEFAULT NULL,
  `ma20` double(20,4) DEFAULT NULL,
  `ma30` double(20,4) DEFAULT NULL,
  `dif` double(20,4) DEFAULT NULL,
  `dea` double(20,4) DEFAULT NULL,
  `macd` double(20,4) DEFAULT NULL,
  `lot_volume` double(20,4) DEFAULT NULL,
  `timestamp` bigint(20) NOT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`,`timestamp`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

#
# Structure for table "daily_history_7"
#

CREATE TABLE `daily_history_7` (
  `id` varchar(20) NOT NULL,
  `volume` double(20,4) DEFAULT NULL,
  `open` double(20,4) DEFAULT NULL,
  `high` double(20,4) DEFAULT NULL,
  `close` double(20,4) DEFAULT NULL,
  `low` double(20,4) DEFAULT NULL,
  `chg` double(20,4) DEFAULT NULL,
  `percent` double(20,4) DEFAULT NULL,
  `turnrate` double(20,4) DEFAULT NULL,
  `ma5` double(20,4) DEFAULT NULL,
  `ma10` double(20,4) DEFAULT NULL,
  `ma20` double(20,4) DEFAULT NULL,
  `ma30` double(20,4) DEFAULT NULL,
  `dif` double(20,4) DEFAULT NULL,
  `dea` double(20,4) DEFAULT NULL,
  `macd` double(20,4) DEFAULT NULL,
  `lot_volume` double(20,4) DEFAULT NULL,
  `timestamp` bigint(20) NOT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`,`timestamp`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

#
# Structure for table "daily_history_8"
#

CREATE TABLE `daily_history_8` (
  `id` varchar(20) NOT NULL,
  `volume` double(20,4) DEFAULT NULL,
  `open` double(20,4) DEFAULT NULL,
  `high` double(20,4) DEFAULT NULL,
  `close` double(20,4) DEFAULT NULL,
  `low` double(20,4) DEFAULT NULL,
  `chg` double(20,4) DEFAULT NULL,
  `percent` double(20,4) DEFAULT NULL,
  `turnrate` double(20,4) DEFAULT NULL,
  `ma5` double(20,4) DEFAULT NULL,
  `ma10` double(20,4) DEFAULT NULL,
  `ma20` double(20,4) DEFAULT NULL,
  `ma30` double(20,4) DEFAULT NULL,
  `dif` double(20,4) DEFAULT NULL,
  `dea` double(20,4) DEFAULT NULL,
  `macd` double(20,4) DEFAULT NULL,
  `lot_volume` double(20,4) DEFAULT NULL,
  `timestamp` bigint(20) NOT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`,`timestamp`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

#
# Structure for table "daily_history_9"
#

CREATE TABLE `daily_history_9` (
  `id` varchar(20) NOT NULL,
  `volume` double(20,4) DEFAULT NULL,
  `open` double(20,4) DEFAULT NULL,
  `high` double(20,4) DEFAULT NULL,
  `close` double(20,4) DEFAULT NULL,
  `low` double(20,4) DEFAULT NULL,
  `chg` double(20,4) DEFAULT NULL,
  `percent` double(20,4) DEFAULT NULL,
  `turnrate` double(20,4) DEFAULT NULL,
  `ma5` double(20,4) DEFAULT NULL,
  `ma10` double(20,4) DEFAULT NULL,
  `ma20` double(20,4) DEFAULT NULL,
  `ma30` double(20,4) DEFAULT NULL,
  `dif` double(20,4) DEFAULT NULL,
  `dea` double(20,4) DEFAULT NULL,
  `macd` double(20,4) DEFAULT NULL,
  `lot_volume` double(20,4) DEFAULT NULL,
  `timestamp` bigint(20) NOT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`,`timestamp`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

#
# Structure for table "income_statement"
#

CREATE TABLE `income_statement` (
  `id` varchar(11) NOT NULL DEFAULT '',
  `begindate` date NOT NULL,
  `enddate` date NOT NULL,
  `biztotinco` bigint(20) NOT NULL DEFAULT '0' COMMENT '营业总收入',
  `biztotcost` bigint(20) NOT NULL DEFAULT '0' COMMENT '营业总成本',
  `biztax` bigint(20) NOT NULL DEFAULT '0' COMMENT '税',
  `salesexpe` bigint(20) NOT NULL DEFAULT '0' COMMENT '销售费用',
  `manaexpe` bigint(20) NOT NULL DEFAULT '0' COMMENT '管理费用',
  `finexpe` bigint(20) NOT NULL DEFAULT '0' COMMENT '财务费用',
  `asseimpaloss` bigint(20) NOT NULL DEFAULT '0' COMMENT '资产减值',
  `valuechgloss` bigint(20) NOT NULL DEFAULT '0' COMMENT '公允价值变动收益',
  `inveinco` bigint(20) DEFAULT NULL COMMENT '投资收益',
  `assoinveprof` bigint(20) DEFAULT NULL COMMENT '对联营企业和合营企业的投资收益',
  `perprofit` bigint(20) DEFAULT NULL COMMENT '营业利润',
  `nonoreve` bigint(20) DEFAULT NULL COMMENT '营业外收入',
  `nonoexpe` bigint(20) DEFAULT NULL COMMENT '营业外支出',
  `totprofit` bigint(20) DEFAULT NULL COMMENT '利润总额',
  `incotaxexpe` bigint(20) DEFAULT NULL COMMENT '所得税费用',
  `netprofit` bigint(20) DEFAULT NULL COMMENT '净利润',
  `parenetp` bigint(20) DEFAULT NULL COMMENT '归属于母公司所有者的净利润',
  `minysharrigh` bigint(20) DEFAULT NULL COMMENT '少数股东损益归属于母公司所有者的净利润',
  `basiceps` bigint(20) DEFAULT NULL COMMENT '基本每股收益',
  `dilutedeps` bigint(20) DEFAULT NULL COMMENT '稀释每股收益',
  `othercompinco` bigint(20) DEFAULT NULL COMMENT '其他综合收益',
  `parecompinco` bigint(20) DEFAULT NULL COMMENT '归属母公司所有者的其他综合收益',
  `compincoamt` bigint(20) DEFAULT NULL COMMENT '综合收益总额',
  `parecompincoamt` bigint(20) DEFAULT NULL COMMENT '归属于母公司股东的综合收益总额',
  `minysharincoamt` bigint(20) DEFAULT NULL COMMENT '归属于少数股东的综合收益总额',
  PRIMARY KEY (`id`,`begindate`,`enddate`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Structure for table "daily_history"
#

CREATE TABLE `daily_history` (
  `id` varchar(20) NOT NULL,
  `volume` double(20,4) DEFAULT NULL,
  `open` double(20,4) DEFAULT NULL,
  `high` double(20,4) DEFAULT NULL,
  `close` double(20,4) DEFAULT NULL,
  `low` double(20,4) DEFAULT NULL,
  `chg` double(20,4) DEFAULT NULL,
  `percent` double(20,4) DEFAULT NULL,
  `turnrate` double(20,4) DEFAULT NULL,
  `ma5` double(20,4) DEFAULT NULL,
  `ma10` double(20,4) DEFAULT NULL,
  `ma20` double(20,4) DEFAULT NULL,
  `ma30` double(20,4) DEFAULT NULL,
  `dif` double(20,4) DEFAULT NULL,
  `dea` double(20,4) DEFAULT NULL,
  `macd` double(20,4) DEFAULT NULL,
  `lot_volume` double(20,4) DEFAULT NULL,
  `timestamp` bigint(20) NOT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`,`timestamp`)
) ENGINE=MRG_MyISAM DEFAULT CHARSET=utf8 UNION=(`daily_history_1`,`daily_history_2`,`daily_history_3`,`daily_history_4`,`daily_history_5`,`daily_history_6`,`daily_history_7`,`daily_history_8`,`daily_history_9`,`daily_history_10`,`daily_history_11`,`daily_history_12`,`daily_history_13`,`daily_history_14`,`daily_history_15`,`daily_history_16`,`daily_history_17`,`daily_history_18`,`daily_history_19`,`daily_history_20`);
