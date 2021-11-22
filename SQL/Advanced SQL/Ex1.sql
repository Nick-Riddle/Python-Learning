--Ex.1

USE [DoctorWho];
GO

SELECT [C].[CompanionName]
FROM [tblCompanion] AS [C]
FULL OUTER JOIN [tblEpisodeCompanion] AS [EC]
ON [C].CompanionId = [EC].CompanionId
WHERE [EC].CompanionId IS NULL;