CREATE TABLE `price` (
  `Id` INT NOT NULL AUTO_INCREMENT COMMENT '�ڵ� ����(Auto Increment)',
  `Last_update` VARCHAR(8) NULL COMMENT '������ ������ ������Ʈ',
  `Price_date` DATETIME NULL COMMENT '�ְ�����',
  `Code` VARCHAR(200) NULL COMMENT '�����ڵ�',
  `Price_open` INT NULL COMMENT '�ð�',
  `Price_close` INT NULL COMMENT '����',
  `Price_high` INT NULL COMMENT '�ְ�',
  `Price_low` INT NULL COMMENT '���Ѱ�',
  `Price_adj_close` INT NULL COMMENT '������ ����',
  `volume` INT NULL COMMENT '�ŷ���',
  PRIMARY KEY (`Id`));
