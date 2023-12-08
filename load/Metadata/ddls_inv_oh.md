create or replace TABLE FINANCIALS.MARVELL_DEMO.INVENTORY_ON_HANDS (
	ITEM_WID NUMBER(38,0) ,
	AMOUNT FLOAT,
	QUANTITY FLOAT,
	QUARTER_NAME VARCHAR(16777216),
	CUM_YIELD FLOAT,
	YIELD_QUANTITY FLOAT
);

**Table 2: FINANCIALS.MARVELL_DEMO.INVENTORY_ON_HANDS	Description : Stores inventory on hand for future quarters and the inventory on hand as of end of quarters for previous quarters. Definition of each column is as follow
- ITEM_WID			-  	Unique ID for an ITEM. This column refers to ITEM_WID in table FINANCIALS.MARVELL_DEMO.ITEM_DETAILS. Column alias is ITEM WID
- AMOUNT			-  	Amount associated with the ITEM, Inventory Value in $. Column alias is ON-HAND AMOUNT and type os currency
- QUANTITY			-  	Number of ITEM Quantities recorded Per Quarter. Column alias is QUANTITY
- QUARTER_NAME			-  	Quarter when Item inventory was populated. Column alias is QUARTER NAME
- CUM_YIELD			-  	Cummulative Yield for an Item. Column alias is CUMULATIVE YIELD
- YIELD_QUANTITY 		-  	"Quantity Yield" for an Item per Quarter against Number of ITEM Quantity. Column alias is YIELD QUANTITY
