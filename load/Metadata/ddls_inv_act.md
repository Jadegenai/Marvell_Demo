create or replace TABLE FINANCIALS.MARVELL_DEMO.INVENTORY_ACTUALS (
	ITEM_WID NUMBER(38,0),
	AMOUNT FLOAT,
	QUARTER_NAME VARCHAR(16777216),
	TYPE VARCHAR(16777216)
);

**Table 1: FINANCIALS.MARVELL_DEMO.INVENTORY_ACTUALS	Description: Stores Actual Inventory ITEM information for  Different Types in previous quarters. Definition of each column is as follow - ITEM_WID			-	Unique ID for an ITEM. This column refers to ITEM_WID in table FINANCIALS.MARVELL_DEMO.ITEM_DETAILS. Column alias is ITEM WID
- AMOUNT			-  	Amount associated with the ITEM , Inventory Value in $. Column alias is AMOUNT and type os currency
- QUARTER_NAME			-  	Quarter when Item actual inventory was recorded. Column alias is QUARTER NAME
- TYPE				-  	Type of Inventory for Actual Items. Column alias is TYPE