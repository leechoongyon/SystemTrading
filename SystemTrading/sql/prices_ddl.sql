CREATE TABLE `price` (
  `Id` INT NOT NULL AUTO_INCREMENT COMMENT '자동 증가(Auto Increment)',
  `Last_update` VARCHAR(8) NULL COMMENT '마지막 데이터 업데이트',
  `Price_date` DATETIME NULL COMMENT '주가일자',
  `Code` VARCHAR(200) NULL COMMENT '종목코드',
  `Price_open` INT NULL COMMENT '시가',
  `Price_close` INT NULL COMMENT '종가',
  `Price_high` INT NULL COMMENT '최고가',
  `Price_low` INT NULL COMMENT '하한가',
  `Price_adj_close` INT NULL COMMENT '보정된 종가',
  `volume` INT NULL COMMENT '거래량',
  PRIMARY KEY (`Id`));
