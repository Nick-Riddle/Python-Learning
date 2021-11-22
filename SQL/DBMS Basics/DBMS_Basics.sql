--SQL Views

USE [AdventureWorks2019];
GO

CREATE VIEW [NumberCust]
AS
SELECT	COUNT([C].[CustomerID]) AS 'NumberCust',
		[C].[TerritoryId]
FROM [Sales].[Customer] AS [C]
GROUP BY [C].[TerritoryID];
GO


--SQL Triggers

USE [AdventureWorks2019];
GO

--SQL Triggers (1)

SELECT *
INTO [HumanResources].[DepartmentHistory]
FROM [HumanResources].[Department]
WHERE 1 <> 1;

SET IDENTITY_INSERT [HumanResources].[DepartmentHistory] ON;
GO

CREATE TRIGGER trgDelete
ON [HumanResources].[Department]
AFTER DELETE
AS
INSERT INTO [HumanResources].[DepartmentHistory]
(
	[DepartmentHistory].[DepartmentID],
	[DepartmentHistory].[Name],
	[DepartmentHistory].[GroupName],
	[DepartmentHistory].[ModifiedDate]
)
SELECT	[d].[DepartmentID],
		[d].[Name],
		[d].[GroupName],
		[d].[ModifiedDate]
FROM deleted AS [d];
GO

/* Before deleting need to delete [HumanResources].[EmployeeDepartmentHistory]
or set ON DELETE CASCADE for foreign key EmployeeDepartmentHistory_Department_DepartmentID */

--SQL Triggers (2)

CREATE TRIGGER trgUpdate ON [HumanResources].[vEmployee]
INSTEAD OF UPDATE
AS
RAISERROR
(
	'Data cannot be updated at this view.',
	16,
	1
);
GO


--SQL Stored Procedures

USE [AdventureWorks2019];
GO

--SQL Stored Procedures (1)

CREATE PROCEDURE sp_ChangeCity
AS
SET NOCOUNT ON
UPDATE [Person].[Address]
SET [City] = UPPER([City]);
GO

--SQL Stored Procedures (2)

CREATE PROCEDURE sp_GetLastName @EmployeeID INT,
								@LastName [dbo].[Name] OUTPUT
AS
SET NOCOUNT ON
SELECT @LastName = (SELECT [P].[LastName]
					FROM [Person].[Person] AS [P]
					JOIN [HumanResources].[Employee] AS [E]
					ON [P].BusinessEntityID = [E].BusinessEntityID
					WHERE [E].BusinessEntityID = @EmployeeID);
GO

DECLARE @GlobalLastName [dbo].[Name]

EXEC sp_GetLastName @EmployeeID = 3,
					@LastName = @GlobalLastName OUTPUT;

PRINT @GlobalLastName;
GO


--SQL XML grouping and ranking functions

USE [AdventureWorks2019]
GO;

SELECT	[PV].[ProductID],
		[PV].[AverageLeadTime],
		[PV].[MinOrderQty],
		[PV].[MaxOrderQty],
		[PV].[UnitMeasureCode],
		SUM([PV].[StandardPrice]) AS [SumPrice]
FROM [Purchasing].[ProductVendor] AS [PV]
GROUP BY ROLLUP
(
	[PV].[ProductID],
	[PV].[AverageLeadTime],
	[PV].[MinOrderQty],
	[PV].[MaxOrderQty],
	[PV].[UnitMeasureCode]
);

SELECT	[PV].[ProductID],
		[PV].[AverageLeadTime],
		[PV].[MinOrderQty],
		[PV].[MaxOrderQty],
		[PV].[UnitMeasureCode],
		SUM([PV].[StandardPrice]) AS [SumPrice]
FROM [Purchasing].[ProductVendor] AS [PV]
GROUP BY CUBE
(
	[PV].[ProductID],
	[PV].[AverageLeadTime],
	[PV].[MinOrderQty],
	[PV].[MaxOrderQty],
	[PV].[UnitMeasureCode]
);

SELECT	[PV].[ProductID],
		[PV].[AverageLeadTime],
		[PV].[MinOrderQty],
		[PV].[MaxOrderQty],
		[PV].[UnitMeasureCode],
		SUM([PV].[StandardPrice]) AS [SumPrice]
FROM [Purchasing].[ProductVendor] AS [PV]
GROUP BY GROUPING SETS
(
	[PV].[ProductID],
	([PV].[ProductID], [PV].[AverageLeadTime], [PV].[MinOrderQty], [PV].[MaxOrderQty], [PV].[UnitMeasureCode])
);


--SQL XML data-types

USE [AdventureWorks2019];
GO

DECLARE @xmlhandle INT;
DECLARE @xmlinput XML;
 
SELECT @xmlinput = B 
FROM OPENROWSET (BULK 'D:\Breakfasts.xml',
				 SINGLE_BLOB) AS Breakfasts(B);

/* OR:
CREATE TABLE breakfasts (xmlcol XML);

INSERT INTO breakfasts
VALUES
(
	'<breakfastMenu_MykolaBezrukyi>
		<Breakfast>
			<Name>Belgian Waffles</Name>
			<Price>5.95</Price>
			<Description>
				Two of our famous Belgian Waffles with plenty of real maple syrup
			</Description>
			<Calories>650</Calories>
		</Breakfast>
		<Breakfast>
			<Name>Strawberry Belgian Waffles</Name>
			<Price>7.95</Price>
			<Description>
				Light Belgian waffles covered with strawberries and whipped cream
			</Description>
			<Calories>900</Calories>
		</Breakfast>
		<Breakfast>
			<Name>Berry-Berry Belgian Waffles</Name>
			<Price>8.95</Price>
			<Description>
				Belgian waffles covered with assorted fresh berries and whipped cream
			</Description>
			<Calories>900</Calories>
		</Breakfast>
		<Breakfast>
			<Name>French Toast</Name>
			<Price>4.50</Price>
			<Description>
				Thick slices made from our homemade sourdough bread
			</Description>
			<Calories>600</Calories>
		</Breakfast>
		<Breakfast>
			<Name>Homestyle Breakfast</Name>
			<Price>6.95</Price>
			<Description>
				Two eggs, bacon or sausage, toast, and our ever-popular hash browns
			</Description>
			<Calories>950</Calories>
		</Breakfast>
	</breakfastMenu_MykolaBezrukyi>'
);

SET @xmlinput = (SELECT *
				 FROM [breakfasts]);
*/

EXEC sp_xml_preparedocument @xmlhandle OUTPUT, @xmlinput;

SELECT *
FROM OPENXML (@xmlhandle,
			  '/breakfastMenu_MykolaBezrukyi/Breakfast',
			  2)
WITH
(
	[Name] VARCHAR(50),
	[Price] DECIMAL(4, 2),
	[Description] VARCHAR(150),
	[Calories] INT
);
    
EXEC sp_xml_removedocument @xmlhandle;


--SQL partitions

CREATE DATABASE [MykolaBezrukyi_PartitionDB];

USE [MykolaBezrukyi_PartitionDB];
GO

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


--SQL Geography and geometry types

DECLARE @gem geometry = 'POLYGON((-6 -4, -4.5 -6, -3 -7, 0 -7.5, 3 -7, 4.5 -6, 6 -4, 6.5 -3, 6.6 -2.5, 6.7 -1,
								6.5 0, 6 1, 5.5 2, 4.5 3, 3 4.2, 2 4.5, -0.5 4.6, -0.6 5, -1.5 6.2, -2.3 6.4,
								-2.3 6.2, -1.5 5.7, -1 4.8, -1 4.5, -3 4.3, -5 3.3, -6 2, -6.85 0, -6.85 -2, -6 -4))';

SELECT @gem AS APPLE;

