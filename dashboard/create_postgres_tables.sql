

CREATE TABLE categories (
    "categoryID" INTEGER,
    "categoryName" VARCHAR(255),
    description VARCHAR(255),
    picture TEXT
);


CREATE TABLE customers (
    “customerID” SERIAL primary key,
     “companyName” VARCHAR(255) not null,
     “contactName” VARCHAR (255),
     "contactTitle" VARCHAR (255),
     address VARCHAR (255),
     city VARCHAR (255),
     region VARCHAR (255),
     "postalCode" VARCHAR (255),
     country VARCHAR (255),
     phone VARCHAR (255),
     fax VARCHAR (255)
);


CREATE TABLE employees (
	“employeeID” INTEGER,
	 “lastName” VARCHAR(255) not null,
	 “firstName” VARCHAR (255),
	 title VARCHAR(255),
     "titleOfCourtesy" VARCHAR(255),
     "birthDate" DATE,
     "hireDate" DATE,
     address VARCHAR(255),   
     city VARCHAR(255),
     region VARCHAR(255),
     "postalCode" VARCHAR(255),
     country VARCHAR(255),
     "homePhone" VARCHAR(255),
     extension VARCHAR(255),
     photo TEXT,
     notes TEXT, 
     "reportsTo" INTEGER, 
     "photoPath" TEXT
);


CREATE TABLE employee_territories (
	“employeeID” INTEGER,
    "territyID" VARCHAR(10)
);


CREATE TABLE order_details (
	"orderID" CHAR(5),
    "productID" INTEGER,
    "unitPrice" NUMERIC,
    quantity INTEGER,
    discount NUMERIC
);

CREATE TABLE orders (
	"orderID" CHAR(5),
    "customerID" VARCHAR(10),
    "employeeID" INTEGER,
    "orderDate" DATE,
    "requiredDate" DATE,
    "shippedDate" DATE,
    "shipVia" INTEGER,
    freight NUMERIC,
    "shipName" VARCHAR(255),
    "shipAddress" VARCHAR(255),
    "shipCity" VARCHAR(255),
    "shipRegion" VARCHAR(255),
    "shipPostalCode" VARCHAR(255),
    "shipCountry" VARCHAR(255)
);

CREATE TABLE products (
    "productID" INTEGER NOT NULL,
    "productName" VARCHAR(255),
    "supplierID" INTEGER,
    "categoryID" INTEGER,
    "quantityPerUnit" VARCHAR(255),
    "unitPrice" NUMERIC,
    "unitsInStock" INTEGER,
    "unitsOnOrder" INTEGER,
    "reorderLevel" INTEGER,
    discontinued INTEGER
);


CREATE TABLE regions (
    "regionID" INTEGER,
    "regionDescription" VARCHAR(255)
);

CREATE TABLE shippers (
    "shipperID" INTEGER,
    "companyName" VARCHAR(255),
    phone VARCHAR(255)
);

CREATE TABLE suppliers (
    "supplierID" INTEGER,
    "companyName" VARCHAR(255),
    "contactName" VARCHAR(255),
    "contactTitle" VARCHAR(255),
    address VARCHAR(255),
    city VARCHAR(255),
    refion VARCHAR(255),
    "postalCode" VARCHAR(255),
    country VARCHAR(255),
    phone VARCHAR(255),
    fax VARCHAR(255),
    "homePage" TEXT
);

CREATE TABLE territories (
    "territoryID" INTEGER,
    "territoryDescription" VARCHAR(255),
    "regionID" INTEGER
);


COPY categories FROM 'data/categories.csv' DELIMITER ',' CSV HEADER NULL 'NULL'; 
COPY territories FROM 'data/territories.csv' DELIMITER ',' CSV HEADER NULL 'NULL';
COPY suppliers FROM 'data/suppliers.csv' DELIMITER ',' CSV HEADER NULL 'NULL';
COPY shippers FROM 'data/shippers.csv' DELIMITER ',' CSV HEADER NULL 'NULL';
COPY regions FROM 'data/regions.csv' DELIMITER ',' CSV HEADER NULL 'NULL';
COPY customers FROM 'data/customers.csv' DELIMITER ',' CSV HEADER NULL 'NULL';
COPY employees FROM 'data/employees.csv' DELIMITER ',' CSV HEADER NULL 'NULL';
COPY employee_territories FROM 'data/employee_territories.csv' DELIMITER ',' CSV HEADER NULL 'NULL';
COPY products FROM 'data/products.csv' DELIMITER ',' CSV HEADER NULL 'NULL';
COPY order_details FROM 'data/order_details.csv' DELIMITER ',' CSV HEADER NULL 'NULL';
COPY orders FROM 'data/orders.csv' DELIMITER ',' CSV HEADER NULL 'NULL';
COPY products FROM 'data/products.csv' DELIMITER ',' CSV HEADER NULL 'NULL';


/* We are creating the table for the countries in order to create the world map*/

CREATE TABLE country (
 iso2 char(2) NOT NULL,
 name varchar(45) NOT NULL,
 iso3 char(3) NOT NULL,
 "numeric" smallint );


INSERT INTO country (iso2, name, iso3, "numeric") VALUES
('AF', 'Afghanistan', 'AFG', 4),
('AX', 'Åland Islands', 'ALA', 248),
('AL', 'Albania', 'ALB', 8),
('DZ', 'Algeria', 'DZA', 12),
('AS', 'American Samoa', 'ASM', 16),
('AD', 'Andorra', 'AND', 20),
('AO', 'Angola', 'AGO', 24),
('AI', 'Anguilla', 'AIA', 660),
('AQ', 'Antarctica', 'ATA', 10),
('AG', 'Antigua and Barbuda', 'ATG', 28),
('AR', 'Argentina', 'ARG', 32),
('AM', 'Armenia', 'ARM', 51),
('AW', 'Aruba', 'ABW', 533),
('AU', 'Australia', 'AUS', 36),
('AT', 'Austria', 'AUT', 40),
('AZ', 'Azerbaijan', 'AZE', 31),
('BS', 'Bahamas', 'BHS', 44),
('BH', 'Bahrain', 'BHR', 48),
('BD', 'Bangladesh', 'BGD', 50),
('BB', 'Barbados', 'BRB', 52),
('BY', 'Belarus', 'BLR', 112),
('BE', 'Belgium', 'BEL', 56),
('BZ', 'Belize', 'BLZ', 84),
('BJ', 'Benin', 'BEN', 204),
('BM', 'Bermuda', 'BMU', 60),
('BT', 'Bhutan', 'BTN', 64),
('BO', 'Bolivia', 'BOL', 68),
('BQ', 'Bonaire, Sint Eustatius and Saba', 'BES', 535),
('BA', 'Bosnia and Herzegovina', 'BIH', 70),
('BW', 'Botswana', 'BWA', 72),
('BV', 'Bouvet Island', 'BVT', 74),
('BR', 'Brazil', 'BRA', 76),
('IO', 'British Indian Ocean Territory', 'IOT', 86),
('BN', 'Brunei Darussalam', 'BRN', 96),
('BG', 'Bulgaria', 'BGR', 100),
('BF', 'Burkina Faso', 'BFA', 854),
('BI', 'Burundi', 'BDI', 108),
('KH', 'Cambodia', 'KHM', 116),
('CM', 'Cameroon', 'CMR', 120),
('CA', 'Canada', 'CAN', 124),
('CV', 'Cape Verde', 'CPV', 132),
('KY', 'Cayman Islands', 'CYM', 136),
('CF', 'Central African Republic', 'CAF', 140),
('TD', 'Chad', 'TCD', 148),
('CL', 'Chile', 'CHL', 152),
('CN', 'China', 'CHN', 156),
('CX', 'Christmas Island', 'CXR', 162),
('CC', 'Cocos (Keeling) Islands', 'CCK', 166),
('CO', 'Colombia', 'COL', 170),
('KM', 'Comoros', 'COM', 174),
('CG', 'Congo', 'COG', 178),
('CD', 'Congo, the Democratic Republic of the', 'COD', 180),
('CK', 'Cook Islands', 'COK', 184),
('CR', 'Costa Rica', 'CRI', 188),
('CI', 'Cote D''Ivoire', 'CIV', 384),
('HR', 'Croatia', 'HRV', 191),
('CU', 'Cuba', 'CUB', 192),
('CW', 'Curaçao', 'CUW', 531),
('CY', 'Cyprus', 'CYP', 196),
('CZ', 'Czech Republic', 'CZE', 203),
('DK', 'Denmark', 'DNK', 208),
('DJ', 'Djibouti', 'DJI', 262),
('DM', 'Dominica', 'DMA', 212),
('DO', 'Dominican Republic', 'DOM', 214),
('EC', 'Ecuador', 'ECU', 218),
('EG', 'Egypt', 'EGY', 818),
('SV', 'El Salvador', 'SLV', 222),
('GQ', 'Equatorial Guinea', 'GNQ', 226),
('ER', 'Eritrea', 'ERI', 232),
('EE', 'Estonia', 'EST', 233),
('ET', 'Ethiopia', 'ETH', 231),
('FK', 'Falkland Islands (Malvinas)', 'FLK', 238),
('FO', 'Faroe Islands', 'FRO', 234),
('FJ', 'Fiji', 'FJI', 242),
('FI', 'Finland', 'FIN', 246),
('FR', 'France', 'FRA', 250),
('GF', 'French Guiana', 'GUF', 254),
('PF', 'French Polynesia', 'PYF', 258),
('TF', 'French Southern Territories', 'ATF', 260),
('GA', 'Gabon', 'GAB', 266),
('GM', 'Gambia', 'GMB', 270),
('GE', 'Georgia', 'GEO', 268),
('DE', 'Germany', 'DEU', 276),
('GH', 'Ghana', 'GHA', 288),
('GI', 'Gibraltar', 'GIB', 292),
('GR', 'Greece', 'GRC', 300),
('GL', 'Greenland', 'GRL', 304),
('GD', 'Grenada', 'GRD', 308),
('GP', 'Guadeloupe', 'GLP', 312),
('GU', 'Guam', 'GUM', 316),
('GT', 'Guatemala', 'GTM', 320),
('GG', 'Guernsey', 'GGY', 831),
('GN', 'Guinea', 'GIN', 324),
('GW', 'Guinea-Bissau', 'GNB', 624),
('GY', 'Guyana', 'GUY', 328),
('HT', 'Haiti', 'HTI', 332),
('HM', 'Heard Island and Mcdonald Islands', 'HMD', 334),
('VA', 'Holy See (Vatican City State)', 'VAT', 336),
('HN', 'Honduras', 'HND', 340),
('HK', 'Hong Kong', 'HKG', 344),
('HU', 'Hungary', 'HUN', 348),
('IS', 'Iceland', 'ISL', 352),
('IN', 'India', 'IND', 356),
('ID', 'Indonesia', 'IDN', 360),
('IR', 'Iran, Islamic Republic of', 'IRN', 364),
('IQ', 'Iraq', 'IRQ', 368),
('IE', 'Ireland', 'IRL', 372),
('IM', 'Isle of Man', 'IMN', 833),
('IL', 'Israel', 'ISR', 376),
('IT', 'Italy', 'ITA', 380),
('JM', 'Jamaica', 'JAM', 388),
('JP', 'Japan', 'JPN', 392),
('JE', 'Jersey', 'JEY', 832),
('JO', 'Jordan', 'JOR', 400),
('KZ', 'Kazakhstan', 'KAZ', 398),
('KE', 'Kenya', 'KEN', 404),
('KI', 'Kiribati', 'KIR', 296),
('KP', 'Korea, Democratic People''s Republic of', 'PRK', 408),
('KR', 'Korea, Republic of', 'KOR', 410),
('KW', 'Kuwait', 'KWT', 414),
('KG', 'Kyrgyzstan', 'KGZ', 417),
('LA', 'Lao People''s Democratic Republic', 'LAO', 418),
('LV', 'Latvia', 'LVA', 428),
('LB', 'Lebanon', 'LBN', 422),
('LS', 'Lesotho', 'LSO', 426),
('LR', 'Liberia', 'LBR', 430),
('LY', 'Libya', 'LBY', 434),
('LI', 'Liechtenstein', 'LIE', 438),
('LT', 'Lithuania', 'LTU', 440),
('LU', 'Luxembourg', 'LUX', 442),
('MO', 'Macao', 'MAC', 446),
('MK', 'Republic of North Macedonia', 'MKD', 807),
('MG', 'Madagascar', 'MDG', 450),
('MW', 'Malawi', 'MWI', 454),
('MY', 'Malaysia', 'MYS', 458),
('MV', 'Maldives', 'MDV', 462),
('ML', 'Mali', 'MLI', 466),
('MT', 'Malta', 'MLT', 470),
('MH', 'Marshall Islands', 'MHL', 584),
('MQ', 'Martinique', 'MTQ', 474),
('MR', 'Mauritania', 'MRT', 478),
('MU', 'Mauritius', 'MUS', 480),
('YT', 'Mayotte', 'MYT', 175),
('MX', 'Mexico', 'MEX', 484),
('FM', 'Micronesia, Federated States of', 'FSM', 583),
('MD', 'Moldova, Republic of', 'MDA', 498),
('MC', 'Monaco', 'MCO', 492),
('MN', 'Mongolia', 'MNG', 496),
('ME', 'Montenegro', 'MNE', 499),
('MS', 'Montserrat', 'MSR', 500),
('MA', 'Morocco', 'MAR', 504),
('MZ', 'Mozambique', 'MOZ', 508),
('MM', 'Myanmar', 'MMR', 104),
('NA', 'Namibia', 'NAM', 516),
('NR', 'Nauru', 'NRU', 520),
('NP', 'Nepal', 'NPL', 524),
('NL', 'Netherlands', 'NLD', 528),
('NC', 'New Caledonia', 'NCL', 540),
('NZ', 'New Zealand', 'NZL', 554),
('NI', 'Nicaragua', 'NIC', 558),
('NE', 'Niger', 'NER', 562),
('NG', 'Nigeria', 'NGA', 566),
('NU', 'Niue', 'NIU', 570),
('NF', 'Norfolk Island', 'NFK', 574),
('MP', 'Northern Mariana Islands', 'MNP', 580),
('NO', 'Norway', 'NOR', 578),
('OM', 'Oman', 'OMN', 512),
('PK', 'Pakistan', 'PAK', 586),
('PW', 'Palau', 'PLW', 585),
('PS', 'Palestine, State of', 'PSE', 275),
('PA', 'Panama', 'PAN', 591),
('PG', 'Papua New Guinea', 'PNG', 598),
('PY', 'Paraguay', 'PRY', 600),
('PE', 'Peru', 'PER', 604),
('PH', 'Philippines', 'PHL', 608),
('PN', 'Pitcairn', 'PCN', 612),
('PL', 'Poland', 'POL', 616),
('PT', 'Portugal', 'PRT', 620),
('PR', 'Puerto Rico', 'PRI', 630),
('QA', 'Qatar', 'QAT', 634),
('RE', 'Reunion', 'REU', 638),
('RO', 'Romania', 'ROU', 642),
('RU', 'Russian Federation', 'RUS', 643),
('RW', 'Rwanda', 'RWA', 646),
('BL', 'Saint Barthélemy', 'BLM', 652),
('SH', 'Saint Helena, Ascension and Tristan da Cunha', 'SHN', 654),
('KN', 'Saint Kitts and Nevis', 'KNA', 659),
('LC', 'Saint Lucia', 'LCA', 662),
('MF', 'Saint Martin (French part)', 'MAF', 663),
('PM', 'Saint Pierre and Miquelon', 'SPM', 666),
('VC', 'Saint Vincent and the Grenadines', 'VCT', 670),
('WS', 'Samoa', 'WSM', 882),
('SM', 'San Marino', 'SMR', 674),
('ST', 'Sao Tome and Principe', 'STP', 678),
('SA', 'Saudi Arabia', 'SAU', 682),
('SN', 'Senegal', 'SEN', 686),
('RS', 'Serbia', 'SRB', 688),
('SC', 'Seychelles', 'SYC', 690),
('SL', 'Sierra Leone', 'SLE', 694),
('SG', 'Singapore', 'SGP', 702),
('SX', 'Sint Maarten (Dutch part)', 'SXM', 534),
('SK', 'Slovakia', 'SVK', 703),
('SI', 'Slovenia', 'SVN', 705),
('SB', 'Solomon Islands', 'SLB', 90),
('SO', 'Somalia', 'SOM', 706),
('ZA', 'South Africa', 'ZAF', 710),
('GS', 'South Georgia and the South Sandwich Islands', 'SGS', 239),
('SS', 'South Sudan', 'SSD', 728),
('ES', 'Spain', 'ESP', 724),
('LK', 'Sri Lanka', 'LKA', 144),
('SD', 'Sudan', 'SDN', 736),
('SR', 'Suriname', 'SUR', 740),
('SJ', 'Svalbard and Jan Mayen', 'SJM', 744),
('SZ', 'Swaziland', 'SWZ', 748),
('SE', 'Sweden', 'SWE', 752),
('CH', 'Switzerland', 'CHE', 756),
('SY', 'Syrian Arab Republic (the)', 'SYR', 760),
('TW', 'Taiwan (Province of China)', 'TWN', 158),
('TJ', 'Tajikistan', 'TJK', 762),
('TZ', 'Tanzania, the United Republic of', 'TZA', 834),
('TH', 'Thailand', 'THA', 764),
('TL', 'Timor-Leste', 'TLS', 626),
('TG', 'Togo', 'TGO', 768),
('TK', 'Tokelau', 'TKL', 772),
('TO', 'Tonga', 'TON', 776),
('TT', 'Trinidad and Tobago', 'TTO', 780),
('TN', 'Tunisia', 'TUN', 788),
('TR', 'Turkey', 'TUR', 792),
('TM', 'Turkmenistan', 'TKM', 795),
('TC', 'Turks and Caicos Islands', 'TCA', 796),
('TV', 'Tuvalu', 'TUV', 798),
('UG', 'Uganda', 'UGA', 800),
('UA', 'Ukraine', 'UKR', 804),
('AE', 'United Arab Emirates', 'ARE', 784),
('GB', 'United Kingdom', 'GBR', 826),
('US', 'United States', 'USA', 840),
('UM', 'United States Minor Outlying Islands', 'UMI', 581),
('UY', 'Uruguay', 'URY', 858),
('UZ', 'Uzbekistan', 'UZB', 860),
('VU', 'Vanuatu', 'VUT', 548),
('VE', 'Venezuela', 'VEN', 862),
('VN', 'Viet Nam', 'VNM', 704),
('VG', 'Virgin Islands (British)', 'VGB', 92),
('VI', 'Virgin Islands (U.S.)', 'VIR', 850),
('WF', 'Wallis and Futuna', 'WLF', 876),
('EH', 'Western Sahara', 'ESH', 732),
('YE', 'Yemen', 'YEM', 887),
('ZM', 'Zambia', 'ZMB', 894),
('ZW', 'Zimbabwe', 'ZWE', 716);