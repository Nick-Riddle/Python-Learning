--SQL partitions

CREATE DATABASE [MykolaBezrukyi_PartitionDB];

USE [MykolaBezrukyi_PartitionDB]
GO;

ALTER DATABASE [MykolaBezrukyi_PartitionDB]
ADD FILEGROUP t1fg;

ALTER DATABASE [MykolaBezrukyi_PartitionDB]
ADD FILEGROUP t2fg;  

ALTER DATABASE [MykolaBezrukyi_PartitionDB] 
ADD FILEGROUP t3fg;

ALTER DATABASE [MykolaBezrukyi_PartitionDB] 
ADD FILEGROUP t4fg;  

ALTER DATABASE [MykolaBezrukyi_PartitionDB] 
ADD FILE   
(  
    NAME = t1d1,  
    FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER2\MSSQL\DATA\t1d1.ndf'  
)  
TO FILEGROUP t1fg;  

ALTER DATABASE [MykolaBezrukyi_PartitionDB]  
ADD FILE   
(  
    NAME = t2d2,  
    FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER2\MSSQL\DATA\t2d2.ndf' 
)  
TO FILEGROUP t2fg;  

ALTER DATABASE [MykolaBezrukyi_PartitionDB]   
ADD FILE   
(  
    NAME = t3d3,  
    FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER2\MSSQL\DATA\t3d3.ndf' 
)  
TO FILEGROUP t3fg;  

ALTER DATABASE [MykolaBezrukyi_PartitionDB]   
ADD FILE   
(  
    NAME = t4d4,  
    FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER2\MSSQL\DATA\t4d4.ndf' 
)  
TO FILEGROUP t4fg;  


CREATE PARTITION FUNCTION [partFunction](DATE)  
AS RANGE LEFT FOR VALUES 
(
	'2021-04-01',
	'2021-08-01',
	'2021-12-31'
);   

CREATE PARTITION SCHEME [partScheme]
AS PARTITION [partFunction]
TO 
(
	t1fg,
	t2fg,
	t3fg,
	t4fg
);  

CREATE TABLE [partTable]
(
	[Date] DATE PRIMARY KEY,
	[NumberSickPeople] INT
)
ON [partScheme]([Date]);   

INSERT INTO [partTable]
(
	[Date],
	[NumberSickPeople]
)
VALUES	('2021-01-05', '15000'),
		('2021-02-16', '12843'),
		('2021-06-21', '7452'),
		('2021-04-09', '10445'),
		('2021-11-16', '21456')

SELECT $PARTITION.[partFunction]([Date]) AS 'PartNumber', *
FROM [partTable];