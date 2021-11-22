--SQL Stored Procedures

USE [AdventureWorks2019]
GO;

--SQL Stored Procedures (1)

CREATE PROCEDURE sp_ChangeCity
AS
SET NOCOUNT ON
UPDATE [Person].[Address]
SET [City] = UPPER([City])
GO;


--SQL Stored Procedures (2)

CREATE PROCEDURE sp_GetLastName @EmployeeID INT,
								@LastName [dbo].[Name] OUTPUT
AS
SET NOCOUNT ON
SELECT @LastName = (SELECT [P].[LastName]
					FROM [Person].[Person] AS [P]
					JOIN [HumanResources].[Employee] AS [E]
					ON [P].BusinessEntityID = [E].BusinessEntityID
					WHERE [E].BusinessEntityID = @EmployeeID)
GO;

DECLARE @GlobalLastName [dbo].[Name]

EXEC sp_GetLastName @EmployeeID = 3,
					@LastName = @GlobalLastName OUTPUT;

PRINT @GlobalLastName
GO;