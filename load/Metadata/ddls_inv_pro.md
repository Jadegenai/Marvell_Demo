create or replace TABLE FINANCIALS.MARVELL_DEMO.PROJECTED_INVENTORY (
	ITEM_WID NUMBER(38,0),
	AMOUNT FLOAT,
	QUARTER_NAME VARCHAR(16777216),
	TYPE VARCHAR(16777216)
);

**Table 4: FINANCIALS.MARVELL_DEMO.PROJECTED_INVENTORY	Description: Stores projected inventory for future quarters with type of projected inventory. Definition of each column is as follow
- ITEM_WID			-   	Unique ID for an ITEM. This column refers to ITEM_WID in table FINANCIALS.MARVELL_DEMO.ITEM_DETAILS. Column alias is ITEM WID
- AMOUNT			-	Amount associated with the ITEM	, Inventory Value in $. Column alias is AMOUNT and type os currency
- QUARTER_NAME			-   	Quarter when Item inventory	was populated. Column alias is QUARTER. The format of value is YYYY-QQ
- TYPE				-   	Type of Inventory for Projected Items. Column alias is TYPE
