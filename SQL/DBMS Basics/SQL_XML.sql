--SQL XML data-types

USE [AdventureWorks2019]
GO;

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