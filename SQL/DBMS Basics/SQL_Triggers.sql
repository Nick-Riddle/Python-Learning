--SQL Triggers

USE [AdventureWorks2019];

--SQL Triggers (1)

SELECT *
INTO [HumanResources].[DepartmentHistory]
FROM [HumanResources].[Department]
WHERE 1 <> 1;

SET IDENTITY_INSERT [HumanResources].[DepartmentHistory] ON
GO;

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
FROM deleted AS [d]
GO;

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
)
GO;


