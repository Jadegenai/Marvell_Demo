create or replace TABLE FINANCIALS.MARVELL_DEMO.ITEM_DETAILS (
	ITEM_WID NUMBER(38,0),
	COMPANY VARCHAR(16777216),
	DIVISION VARCHAR(16777216),
	BU VARCHAR(16777216),
	PRODUCT_LINE VARCHAR(16777216),
	SUB_PRODUCT_LINE VARCHAR(16777216),
	FINANCIAL_GROUP VARCHAR(16777216),
	PART_NUMBER VARCHAR(16777216),
	ITEM_STAGE VARCHAR(16777216),
	ASSY_PART_NUMBER VARCHAR(16777216),
	DIE_PART_NUMBER VARCHAR(16777216),
	ECCN FLOAT,
	FAB_PART_NUMBER VARCHAR(16777216),
	SCHEDULE_B_NUM FLOAT,
	TEST_PART_NUMBER VARCHAR(16777216),
	PLATFORM FLOAT,
	BASE_DIE VARCHAR(16777216),
	BASE_DIE_REV VARCHAR(16777216),
	FAB_HOUSE VARCHAR(16777216),
	DESIGN_COUNTRY FLOAT,
	MARKETING_ITEM VARCHAR(16777216),
	ITEM_TYPE VARCHAR(16777216),
	PLANNER_CODE FLOAT,
	INVENTORY_ORGANIZATION NUMBER(38,0),
	COUNTRY_OF_MANUFACTURING FLOAT,
	DEVICE VARCHAR(16777216),
	PRODUCT_GROUP VARCHAR(16777216),
	PROJECT_CODE FLOAT,
	PROJECT_CODE_DESCRIPTION VARCHAR(16777216),
	PACKAGE_CODE VARCHAR(16777216),
	SERVICE_PART_NUMBER VARCHAR(16777216),
	LICENSE_EXCEPTION FLOAT,
	END_MARKET VARCHAR(16777216),
	SUB_MARKET VARCHAR(16777216),
	MODEL_NUMBER VARCHAR(16777216),
	SPEED FLOAT,
	ITEM_TYPE_GROUP VARCHAR(16777216),
	MPR_YEAR_CATEGORY FLOAT,
	MPR_YEAR_CATEGORY_GROUP VARCHAR(16777216),
	MPR_YEAR_CATEGORY_SORTING NUMBER(38,0),
	CURRENT_MODEL_NUMBER VARCHAR(16777216),
	SALES_COMP_DIVISION VARCHAR(16777216),
	SALES_COMP_BU VARCHAR(16777216),
	SALES_COMP_PRODUCT_LINE VARCHAR(16777216),
	SALES_COMP_FINANCIAL_GROUP VARCHAR(16777216),
	SALES_COMP_SUB_PRODUCT_LINE VARCHAR(16777216),
	TECHNOLOGY_GROUP VARCHAR(16777216),
	IDENTIFIED_IP FLOAT,
	BUSINESS_OWNER VARCHAR(16777216),
	PRODUCT_LINE_MANAGER FLOAT
);

**Table 3: FINANCIALS.MARVELL_DEMO.ITEM_DETAILS	Description: This is ITEM master table stores ITEM Information including their Item WID, Division,BU, ProductLine ETC. Definition of each column is as follow
- ITEM_WID 			-	Unique ID for an ITEM. Column alias is ITEM WID
- COMPANY                       -	NAME of the company Item belongs to. Column alias is COMPANY
- DIVISION                      -	Division In the company Item belongs to. Column alias is DIVISION
- BU                            -	BU In the company Item belongs to. Column alias is BU. Must be refered if user query refers Organization or Business Unit or BU. 
- PRODUCT_LINE                  -	Product Line In the company Item belongs to. Column alias is PRODUCT LINE
- SUB_PRODUCT_LINE              -	Sub Product Line In the company Item belongs to. SUB PRODUCT LINE
- FINANCIAL_GROUP               -	"Financial Group" which is associated with a ITEM in the company. Column alias is FINANCIAL GROUP. Must be referred when user query contains "manufacturing Financial Group" or "Financial Group" or "Financial_Group". 
- PART_NUMBER                   -	Displays the Part Number for an ITEM_WID. Column alias is PART NUMBER or part_number.Some of the Part Number examples are dX-6SJnP-KLL, R8-WrkGz-H8e.
- ITEM_STAGE                    -	Product Life Cycle Stage in which Item is currently in. Column alias is ITEM STAGE. One of the values is FG that stands for Finished Goods. This column must be referred if user query contains "item stage" or "product stage" or "product lifecycle stage" or "sub inventory stage" or "sub-inventory stage"
- ASSY_PART_NUMBER              -	Number when the part of Item is in Assembly stage. Column alias is ASSEMBLY PART NUMBER
- DIE_PART_NUMBER               -	Number when the part of Item is in Die stage. Column alias is DIE PART NUMBER
- ECCN                          -	ECCN Number for an Item to determine licencing information. Column alias is ECCN
- FAB_PART_NUMBER               -	Number when the part of Item is in FAB stage. Column alias is FAB PART NUMBER
- SCHEDULE_B_NUM                -	Specific Classification Code for Exporting Goods. Column alias is CLASSIFICATION CODE
- TEST_PART_NUMBER              -	Number when the part of Item is in Test stage. Column alias is TEST PART NUMBER
- PLATFORM                      -	Column alias is PLATFORM
- BASE_DIE                      -	Item Id for the Die. Column alias is BASE DIE
- BASE_DIE_REV                  -	Revised Item Id for the Die. Column alias is BASED DIE REVISED ID
- FAB_HOUSE                     -	Fabrication House Name for the Item. Column alias is FAB HOUSE. This is also called "manufacturing source" or "qualified manufacturing sources". This column contains value ESMC, GF and Marvell
- DESIGN_COUNTRY                -	Country Name where the Item is Designed. Column alias is DESIGN COUNTRY or geogrpahy of manufacturing. This column will have geography information , Some users might also refer to this as geogrpahy of manufacturing.
- MARKETING_ITEM                -	Item Number Associated for  Marketting Reference. Column alias is MARKETING ITEM NUMBER
- ITEM_TYPE                     -	Type of Item or Item category or the Stage at which the Item is in. Column alias is ITEM TYPE or Stage. This column contains value of various "stage" like "NPI" ("New Product Introduction") , "FG" ("Finished Goods"), "FIN". must be referred only when user query contains combination of "stage" and "NPI" or "New Product Introduction" or "FG" or "Finished Goods" or "FIN".
- PLANNER_CODE                  -	PLanner Code for an Item which are up to date with Factory Status. Column alias is PLANNER CODE
- INVENTORY_ORGANIZATION        -	Unique Number of Inventory Organization. Column alias is INVENTORY ORGANIZATION
- COUNTRY_OF_MANUFACTURING      -	Country where Item is Manufactured. Column alias is MANUFACTURING COUNTRY
- DEVICE                        -	Device Name of the Item. Column alias is DEVICE
- PRODUCT_GROUP                 -	"Type of Product" or product group with list of allowed values Wfr, IC and MD where Wfr stands for Wafer, IC stands for Integrated Circuit and MD stands for Mechanical Devices. Column alias is PRODUCT GROUP
- PROJECT_CODE                  -	Project Code Associated with an Item. Column alias is PROJECT CODE
- PROJECT_CODE_DESCRIPTION      -	Description of a Project Code. Column alias is PROJECT CODE DESCRIPTION
- PACKAGE_CODE                  -	Package Code for an Item. Column alias is PACKAGE CODE
- SERVICE_PART_NUMBER           -	Service Part Number for an Item. Column alias is SERVICE PART NUMBER
- LICENSE_EXCEPTION             -	Export Licence Exception Number for the Item. Column alias is LICENSE EXCEPTION
- END_MARKET                    -	Describes which category of Market Item belongs to during Sale. Column alias is END MARKET
- SUB_MARKET 			-	Describes which Sub category of Market Item belongs to during Sale. Column alias is SUB MARKET
- MODEL_NUMBER       		-	Model Number for an ITEM. Column alias is MODEL NUMBER
- SPEED                         -	Speed for an Item from performance Characteristics. Column alias is SPEED
- ITEM_TYPE_GROUP               -	Item Group Type for an Item Listed. Column alias is ITEM TYPE GROUP
- MPR_YEAR_CATEGORY             -	MPR YEAR CATEGORY for an Item. Column alias is MPR YEAR CATEGORY
- MPR_YEAR_CATEGORY_GROUP       -	Year Categroy Group for MPR. Column alias is MPR YEAR CATEGORY GROUP
- MPR_YEAR_CATEGORY_SORTING     -	Column alias is MPR YEAR CATEGORY SORTING
- CURRENT_MODEL_NUMBER          -	Current Model Number for an ITEM. Column alias is CURRENT MODEL NUMBER
- SALES_COMP_DIVISION           -	Division for the Sales Team doing the Sales for an ITEM. Column alias is SALES COMP DIVISION. This column must be cosnidered when user query has sales comp mentioned
- SALES_COMP_BU                 -	BU or Organization for the Sales Team doing the Sales for an ITEM. Column alias is SALES COMP BU. This column must be cosnidered when user query has sales comp mentioned
- SALES_COMP_PRODUCT_LINE       -	Product Line for the Sales Team doing the Sales for an ITEM. Column alias is SALES COMP PRODUCT LINE. This column must be cosnidered when user query has sales comp mentioned
- SALES_COMP_FINANCIAL_GROUP    -	Sales Company Fin Group for the Sales Team doing the Sales for an ITEM in the company. Column alias is SALES COMP FINANCIAL GROUP , This column must be cosnidered when user query has sales comp mentioned.
- SALES_COMP_SUB_PRODUCT_LINE   -	Sub Product Line for the Sales Team doing the Sales for an ITEM. Column alias is SALES COMP SUB PRODUCT LINE. This column must be cosnidered when user query has sales comp mentioned
- TECHNOLOGY_GROUP              -	Tech Group for an ITEM parts. this can also be referred as tech group. Column alias is TECHNOLOGY GROUP. This column is also called "FAB technology Node". Values in this column generally have format Xnm or XXnm or XXnm_XXnm for example 80nm_90nm or 7nm and so on
- IDENTIFIED_IP                 -	Intellectual property for an Item. Column alias is IDENTIFIED IP
- BUSINESS_OWNER                -	Busines owner of the ITEM. Column alias is BUSINESS OWNER
- PRODUCT_LINE_MANAGER          -	Line Manager for an ITEM. Column alias is PRODUCT LINE MANAGER