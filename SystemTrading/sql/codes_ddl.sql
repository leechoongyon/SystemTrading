CREATE TABLE `codes` 
(
  `Id` INT NOT NULL AUTO_INCREMENT COMMENT '자동 증가(Auto Increment)',
  `Last_update` VARCHAR(8) NULL COMMENT '마지막 데이터 업데이트 일자',
  `Code` VARCHAR(200) NULL COMMENT '종목코드',
  `Full_code` VARCHAR(200) NULL COMMENT '종목 전체코드',
  `Market_type` INT NULL COMMENT '시장종류 1=코스피, 2= 코스닥',
  `Company` VARCHAR(200) NULL COMMENT '종목명',
  PRIMARY KEY (`Id`) 
) DEFAULT CHARSET=utf8;
