CREATE TABLE `codes` 
(
  `Id` INT NOT NULL AUTO_INCREMENT COMMENT '�ڵ� ����(Auto Increment)',
  `Last_update` VARCHAR(8) NULL COMMENT '������ ������ ������Ʈ ����',
  `Code` VARCHAR(200) NULL COMMENT '�����ڵ�',
  `Full_code` VARCHAR(200) NULL COMMENT '���� ��ü�ڵ�',
  `Market_type` INT NULL COMMENT '�������� 1=�ڽ���, 2= �ڽ���',
  `Company` VARCHAR(200) NULL COMMENT '�����',
  PRIMARY KEY (`Id`) 
) DEFAULT CHARSET=utf8;
