# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/country.proto
# Protobuf Python Version: 6.30.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    0,
    '',
    'api/commons/country.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x61pi/commons/country.proto\x12\x0b\x61pi.commons*\x98\x32\n\x07\x43ountry\x12\x15\n\x11\x43OUNTRY_UNDEFINED\x10\x00\x12\x17\n\x13\x43OUNTRY_AFGHANISTAN\x10\x04\x12\x13\n\x0f\x43OUNTRY_ALBANIA\x10\x08\x12\x13\n\x0f\x43OUNTRY_ALGERIA\x10\x0c\x12\x13\n\x0f\x43OUNTRY_ANDORRA\x10\x14\x12\x12\n\x0e\x43OUNTRY_ANGOLA\x10\x18\x12\x16\n\x12\x43OUNTRY_ANTARCTICA\x10\n\x12\x15\n\x11\x43OUNTRY_ARGENTINA\x10 \x12\x13\n\x0f\x43OUNTRY_ARMENIA\x10\x33\x12\x12\n\rCOUNTRY_ARUBA\x10\x95\x04\x12\x15\n\x11\x43OUNTRY_AUSTRALIA\x10$\x12\x13\n\x0f\x43OUNTRY_AUSTRIA\x10(\x12\x16\n\x12\x43OUNTRY_AZERBAIJAN\x10\x1f\x12\x13\n\x0f\x43OUNTRY_BAHRAIN\x10\x30\x12\x16\n\x12\x43OUNTRY_BANGLADESH\x10\x32\x12\x13\n\x0f\x43OUNTRY_BELARUS\x10p\x12\x13\n\x0f\x43OUNTRY_BELGUIM\x10\x38\x12\x12\n\x0e\x43OUNTRY_BELIZE\x10T\x12\x12\n\rCOUNTRY_BENIN\x10\xcc\x01\x12\x13\n\x0f\x43OUNTRY_BERMUDA\x10<\x12\x12\n\x0e\x43OUNTRY_BHUTAN\x10@\x12\x13\n\x0f\x43OUNTRY_BOLIVIA\x10\x44\x12\"\n\x1e\x43OUNTRY_BOSNIA_AND_HERZEGOVINA\x10\x46\x12\x14\n\x10\x43OUNTRY_BOTSWANA\x10H\x12\x12\n\x0e\x43OUNTRY_BRAZIL\x10L\x12\x1d\n\x19\x43OUNTRY_BRUNEI_DARUSSALAM\x10`\x12\x14\n\x10\x43OUNTRY_BULGARIA\x10\x64\x12\x19\n\x14\x43OUNTRY_BURKINA_FASO\x10\xd6\x06\x12\x13\n\x0f\x43OUNTRY_BURUNDI\x10l\x12\x14\n\x10\x43OUNTRY_CAMBODIA\x10t\x12\x14\n\x10\x43OUNTRY_CAMEROON\x10x\x12%\n COUNTRY_CENTRAL_AFRICAN_REPUBLIC\x10\x8c\x01\x12\x11\n\x0c\x43OUNTRY_CHAD\x10\x94\x01\x12\x12\n\rCOUNTRY_CHILE\x10\x98\x01\x12\x12\n\rCOUNTRY_CHINA\x10\x9c\x01\x12\x15\n\x10\x43OUNTRY_COLOMBIA\x10\xaa\x01\x12\x14\n\x0f\x43OUNTRY_COMOROS\x10\xae\x01\x12&\n!COUNTRY_CONGO_DEMOCRATIC_REPUBLIC\x10\xb4\x01\x12\x12\n\rCOUNTRY_CONGO\x10\xb2\x01\x12\x19\n\x14\x43OUNTRY_COOK_ISLANDS\x10\xb8\x01\x12\x17\n\x12\x43OUNTRY_COSTA_RICA\x10\xbc\x01\x12\x14\n\x0f\x43OUNTRY_CROATIA\x10\xbf\x01\x12\x14\n\x0f\x43OUNTRY_CURACAO\x10\x93\x04\x12\x13\n\x0e\x43OUNTRY_CYPRUS\x10\xc4\x01\x12\x14\n\x0f\x43OUNTRY_CZECHIA\x10\xcb\x01\x12\x14\n\x0f\x43OUNTRY_DENMARK\x10\xd0\x01\x12\x15\n\x10\x43OUNTRY_DJIBOUTI\x10\x86\x02\x12\x14\n\x0f\x43OUNTRY_ECUADOR\x10\xda\x01\x12\x12\n\rCOUNTRY_EGYPT\x10\xb2\x06\x12\x18\n\x13\x43OUNTRY_EL_SALVADOR\x10\xde\x01\x12\x1e\n\x19\x43OUNTRY_EQUATORIAL_GUINEA\x10\xe2\x01\x12\x14\n\x0f\x43OUNTRY_ERITREA\x10\xe8\x01\x12\x14\n\x0f\x43OUNTRY_ESTONIA\x10\xe9\x01\x12\x15\n\x10\x43OUNTRY_ESWATINI\x10\xec\x05\x12\x15\n\x10\x43OUNTRY_ETHIOPIA\x10\xe7\x01\x12\x1d\n\x18\x43OUNTRY_FALKLAND_ISLANDS\x10\xee\x01\x12\x11\n\x0c\x43OUNTRY_FIJI\x10\xf2\x01\x12\x14\n\x0f\x43OUNTRY_FINLAND\x10\xf6\x01\x12\x13\n\x0e\x43OUNTRY_FRANCE\x10\xfa\x01\x12\x1a\n\x15\x43OUNTRY_FRENCH_GUIANA\x10\xfe\x01\x12\x1d\n\x18\x43OUNTRY_FRENCH_POLYNESIA\x10\x82\x02\x12\x12\n\rCOUNTRY_GABON\x10\x8a\x02\x12\x13\n\x0e\x43OUNTRY_GAMBIA\x10\x8e\x02\x12\x14\n\x0f\x43OUNTRY_GEORGIA\x10\x8c\x02\x12\x14\n\x0f\x43OUNTRY_GERMANY\x10\x94\x02\x12\x12\n\rCOUNTRY_GHANA\x10\xa0\x02\x12\x16\n\x11\x43OUNTRY_GIBRALTAR\x10\xa4\x02\x12\x13\n\x0e\x43OUNTRY_GREECE\x10\xac\x02\x12\x16\n\x11\x43OUNTRY_GREENLAND\x10\xb0\x02\x12\x17\n\x12\x43OUNTRY_GUADELOUPE\x10\xb8\x02\x12\x16\n\x11\x43OUNTRY_GUATEMALA\x10\xc0\x02\x12\x13\n\x0e\x43OUNTRY_GUINEA\x10\xc4\x02\x12\x1a\n\x15\x43OUNTRY_GUINEA_BISSAU\x10\xf0\x04\x12\x13\n\x0e\x43OUNTRY_GUYANA\x10\xc8\x02\x12\x12\n\rCOUNTRY_HAITI\x10\xcc\x02\x12\x15\n\x10\x43OUNTRY_HONDURAS\x10\xd4\x02\x12\x16\n\x11\x43OUNTRY_HONG_KONG\x10\xd8\x02\x12\x14\n\x0f\x43OUNTRY_HUNGARY\x10\xdc\x02\x12\x14\n\x0f\x43OUNTRY_ICELAND\x10\xe0\x02\x12\x12\n\rCOUNTRY_INDIA\x10\xe4\x02\x12\x16\n\x11\x43OUNTRY_INDONESIA\x10\xe8\x02\x12\x11\n\x0c\x43OUNTRY_IRAQ\x10\xf0\x02\x12\x14\n\x0f\x43OUNTRY_IRELAND\x10\xf4\x02\x12\x13\n\x0e\x43OUNTRY_ISRAEL\x10\xf8\x02\x12\x12\n\rCOUNTRY_ITALY\x10\xfc\x02\x12\x12\n\rCOUNTRY_JAPAN\x10\x88\x03\x12\x13\n\x0e\x43OUNTRY_JORDAN\x10\x90\x03\x12\x17\n\x12\x43OUNTRY_KAZAKHSTAN\x10\x8e\x03\x12\x12\n\rCOUNTRY_KENYA\x10\x94\x03\x12\x1b\n\x16\x43OUNTRY_KOREA_REPUBLIC\x10\x9a\x03\x12\x13\n\x0e\x43OUNTRY_KUWAIT\x10\x9e\x03\x12\x17\n\x12\x43OUNTRY_KYRGYZSTAN\x10\xa1\x03\x12,\n\'COUNTRY_LAO_PEOPLES_DEMOCRATIC_REPUBLIC\x10\xa2\x03\x12\x13\n\x0e\x43OUNTRY_LATVIA\x10\xac\x03\x12\x14\n\x0f\x43OUNTRY_LEBANON\x10\xa6\x03\x12\x14\n\x0f\x43OUNTRY_LESOTHO\x10\xaa\x03\x12\x14\n\x0f\x43OUNTRY_LIBERIA\x10\xae\x03\x12\x12\n\rCOUNTRY_LIBYA\x10\xb2\x03\x12\x1a\n\x15\x43OUNTRY_LIECHTENSTEIN\x10\xb6\x03\x12\x16\n\x11\x43OUNTRY_LITHUANIA\x10\xb8\x03\x12\x17\n\x12\x43OUNTRY_LUXEMBOURG\x10\xba\x03\x12\x1c\n\x17\x43OUNTRY_NORTH_MACEDONIA\x10\xa7\x06\x12\x17\n\x12\x43OUNTRY_MADAGASCAR\x10\xc2\x03\x12\x13\n\x0e\x43OUNTRY_MALAWI\x10\xc6\x03\x12\x15\n\x10\x43OUNTRY_MALAYSIA\x10\xca\x03\x12\x15\n\x10\x43OUNTRY_MALDIVES\x10\xce\x03\x12\x11\n\x0c\x43OUNTRY_MALI\x10\xd2\x03\x12\x12\n\rCOUNTRY_MALTA\x10\xd6\x03\x12\x1d\n\x18\x43OUNTRY_MARSHALL_ISLANDS\x10\xc8\x04\x12\x17\n\x12\x43OUNTRY_MARTINIQUE\x10\xda\x03\x12\x17\n\x12\x43OUNTRY_MAURITANIA\x10\xde\x03\x12\x16\n\x11\x43OUNTRY_MAURITIUS\x10\xe0\x03\x12\x13\n\x0e\x43OUNTRY_MEXICO\x10\xe4\x03\x12\x17\n\x12\x43OUNTRY_MICRONESIA\x10\xc7\x04\x12\x14\n\x0f\x43OUNTRY_MOLDOVA\x10\xf2\x03\x12\x13\n\x0e\x43OUNTRY_MONACO\x10\xec\x03\x12\x16\n\x11\x43OUNTRY_MONGOLLIA\x10\xf0\x03\x12\x17\n\x12\x43OUNTRY_MONTENEGRO\x10\xf3\x03\x12\x14\n\x0f\x43OUNTRY_MOROCCO\x10\xf8\x03\x12\x17\n\x12\x43OUNTRY_MOZAMBIQUE\x10\xfc\x03\x12\x13\n\x0f\x43OUNTRY_MYANMAR\x10h\x12\x14\n\x0f\x43OUNTRY_NAMIBIA\x10\x84\x04\x12\x12\n\rCOUNTRY_NAURU\x10\x88\x04\x12\x12\n\rCOUNTRY_NEPAL\x10\x8c\x04\x12\x18\n\x13\x43OUNTRY_NETHERLANDS\x10\x90\x04\x12\x1a\n\x15\x43OUNTRY_NEW_CALEDONIA\x10\x9c\x04\x12\x18\n\x13\x43OUNTRY_NEW_ZEALAND\x10\xaa\x04\x12\x16\n\x11\x43OUNTRY_NICARAGUA\x10\xae\x04\x12\x12\n\rCOUNTRY_NIGER\x10\xb2\x04\x12\x14\n\x0f\x43OUNTRY_NIGERIA\x10\xb6\x04\x12\x11\n\x0c\x43OUNTRY_NIUE\x10\xba\x04\x12\x13\n\x0e\x43OUNTRY_NORWAY\x10\xc2\x04\x12\x11\n\x0c\x43OUNTRY_OMAN\x10\x80\x04\x12\x15\n\x10\x43OUNTRY_PAKISTAN\x10\xca\x04\x12\x12\n\rCOUNTRY_PALAU\x10\xc9\x04\x12\x16\n\x11\x43OUNTRY_PALESTINE\x10\x93\x02\x12\x13\n\x0e\x43OUNTRY_PANAMA\x10\xcf\x04\x12\x1d\n\x18\x43OUNTRY_PAPUA_NEW_GUINEA\x10\xd6\x04\x12\x15\n\x10\x43OUNTRY_PARAGUAY\x10\xd8\x04\x12\x11\n\x0c\x43OUNTRY_PERU\x10\xdc\x04\x12\x18\n\x13\x43OUNTRY_PHILIPPINES\x10\xe0\x04\x12\x13\n\x0e\x43OUNTRY_POLAND\x10\xe8\x04\x12\x15\n\x10\x43OUNTRY_PORTUGAL\x10\xec\x04\x12\x12\n\rCOUNTRY_QATAR\x10\xfa\x04\x12\x14\n\x0f\x43OUNTRY_ROMANIA\x10\x82\x05\x12\x1f\n\x1a\x43OUNTRY_RUSSIAN_FEDERATION\x10\x83\x05\x12\x13\n\x0e\x43OUNTRY_RWANDA\x10\x86\x05\x12\x19\n\x14\x43OUNTRY_SAINT_HELENA\x10\x8e\x05\x12&\n!COUNTRY_SAINT_PIERRE_AND_MIQUELON\x10\x9a\x05\x12\x12\n\rCOUNTRY_SAMOA\x10\xf2\x06\x12\x17\n\x12\x43OUNTRY_SAN_MARINO\x10\xa2\x05\x12\x19\n\x14\x43OUNTRY_SAUDI_ARABIA\x10\xaa\x05\x12\x14\n\x0f\x43OUNTRY_SENAGAL\x10\xae\x05\x12\x13\n\x0e\x43OUNTRY_SERBIA\x10\xb0\x05\x12\x19\n\x14\x43OUNTRY_SIERRA_LEONE\x10\xb6\x05\x12\x16\n\x11\x43OUNTRY_SINGAPORE\x10\xbe\x05\x12\x19\n\x14\x43OUNTRY_SINT_MAARTEN\x10\x96\x04\x12\x15\n\x10\x43OUNTRY_SLOVAKIA\x10\xbf\x05\x12\x15\n\x10\x43OUNTRY_SLOVENIA\x10\xc1\x05\x12\x1b\n\x17\x43OUNTRY_SOLOMON_ISLANDS\x10Z\x12\x14\n\x0f\x43OUNTRY_SOMALIA\x10\xc2\x05\x12\x19\n\x14\x43OUNTRY_SOUTH_AFRICA\x10\xc6\x05\x12\x18\n\x13\x43OUNTRY_SOUTH_SUDAN\x10\xd8\x05\x12\x12\n\rCOUNTRY_SPAIN\x10\xd4\x05\x12\x16\n\x11\x43OUNTRY_SRI_LANKA\x10\x90\x01\x12\x12\n\rCOUNTRY_SUDAN\x10\xd9\x05\x12\x15\n\x10\x43OUNTRY_SURINAME\x10\xe4\x05\x12\x13\n\x0e\x43OUNTRY_SWEDEN\x10\xf0\x05\x12\x18\n\x13\x43OUNTRY_SWITZERLAND\x10\xf4\x05\x12!\n\x1c\x43OUNTRY_SYRIAN_ARAB_REPUBLIC\x10\xf8\x05\x12\x13\n\x0e\x43OUNTRY_TAIWAN\x10\x9e\x01\x12\x17\n\x12\x43OUNTRY_TAJIKISTAN\x10\xfa\x05\x12\x15\n\x10\x43OUNTRY_TANZANIA\x10\xc2\x06\x12\x15\n\x10\x43OUNTRY_THAILAND\x10\xfc\x05\x12\x11\n\x0c\x43OUNTRY_TOGO\x10\x80\x06\x12\x14\n\x0f\x43OUNTRY_TOKELAU\x10\x84\x06\x12\x12\n\rCOUNTRY_TONGA\x10\x88\x06\x12\x14\n\x0f\x43OUNTRY_TUNISIA\x10\x94\x06\x12\x13\n\x0e\x43OUNTRY_TURKEY\x10\x98\x06\x12\x19\n\x14\x43OUNTRY_TURKMENISTAN\x10\x9b\x06\x12%\n COUNTRY_TURKS_AND_CAICOS_ISLANDS\x10\x9c\x06\x12\x13\n\x0e\x43OUNTRY_TUVALU\x10\x9e\x06\x12\x13\n\x0e\x43OUNTRY_UGANDA\x10\xa0\x06\x12\x14\n\x0f\x43OUNTRY_UKRAINE\x10\xa4\x06\x12!\n\x1c\x43OUNTRY_UNITED_ARAB_EMIRATES\x10\x90\x06\x12\x41\n<COUNTRY_UNITED_KINGDOM_OF_GREAT_BRITAIN_AND_NORTHERN_IRELAND\x10\xba\x06\x12%\n COUNTRY_UNITED_STATES_OF_AMERICA\x10\xc8\x06\x12\x14\n\x0f\x43OUNTRY_URUGUAY\x10\xda\x06\x12\x17\n\x12\x43OUNTRY_UZBEKISTAN\x10\xdc\x06\x12\x14\n\x0f\x43OUNTRY_VANUATU\x10\xa4\x04\x12\x16\n\x11\x43OUNTRY_VENEZUELA\x10\xde\x06\x12\x15\n\x10\x43OUNTRY_VIET_NAM\x10\xc0\x05\x12\x1e\n\x19\x43OUNTRY_WALLIS_AND_FUTUNA\x10\xec\x06\x12\x12\n\rCOUNTRY_YEMEN\x10\xf7\x06\x12\x13\n\x0e\x43OUNTRY_ZAMBIA\x10\xfe\x06\x12\x15\n\x10\x43OUNTRY_ZIMBABWE\x10\xcc\x05\x12\x17\n\x12\x43OUNTRY_GLOBAL_SIP\x10\xe8\x07\"\x06\x08\xf8\x01\x10\xf8\x01\"\x04\x08\x10\x10\x10\"\x06\x08\x94\x05\x10\x94\x05\"\x04\x08\x1c\x10\x1c\"\x04\x08,\x10,\"\x04\x08\x34\x10\x34\"\x06\x08\xab\x04\x10\xab\x04\"\x04\x08J\x10J\"\x04\x08V\x10V\"\x06\x08\x84\x01\x10\x84\x01\"\x04\x08|\x10|\"\x06\x08\x88\x01\x10\x88\x01\"\x06\x08\xa2\x01\x10\xa2\x01\"\x06\x08\xa6\x01\x10\xa6\x01\"\x06\x08\x80\x03\x10\x80\x03\"\x06\x08\xc0\x01\x10\xc0\x01\"\x06\x08\xd4\x01\x10\xd4\x01\"\x06\x08\xd6\x01\x10\xd6\x01\"\x06\x08\xea\x01\x10\xea\x01\"\x06\x08\x84\x02\x10\x84\x02\"\x06\x08\xb4\x02\x10\xb4\x02\"\x06\x08\xbc\x02\x10\xbc\x02\"\x06\x08\xbf\x06\x10\xbf\x06\"\x06\x08\xce\x02\x10\xce\x02\"\x06\x08\xd0\x02\x10\xd0\x02\"\x06\x08\xec\x02\x10\xec\x02\"\x06\x08\xc1\x06\x10\xc1\x06\"\x06\x08\x84\x03\x10\x84\x03\"\x06\x08\xc0\x06\x10\xc0\x06\"\x06\x08\xa8\x02\x10\xa8\x02\"\x06\x08\x98\x03\x10\x98\x03\"\x06\x08\xbe\x03\x10\xbe\x03\"\x06\x08\xaf\x01\x10\xaf\x01\"\x06\x08\xf4\x03\x10\xf4\x03\"\x06\x08\xbe\x04\x10\xbe\x04\"\x06\x08\xc4\x04\x10\xc4\x04\"\x06\x08\xe4\x04\x10\xe4\x04\"\x06\x08\xf6\x04\x10\xf6\x04\"\x06\x08\xfe\x04\x10\xfe\x04\"\x06\x08\x8c\x05\x10\x8c\x05\"\x06\x08\x93\x05\x10\x93\x05\"\x06\x08\x96\x05\x10\x96\x05\"\x06\x08\x97\x05\x10\x97\x05\"\x06\x08\x9e\x05\x10\x9e\x05\"\x06\x08\xa6\x05\x10\xa6\x05\"\x06\x08\xb2\x05\x10\xb2\x05\"\x06\x08\xef\x01\x10\xef\x01\"\x06\x08\xe8\x05\x10\xe8\x05\"\x06\x08\xf2\x04\x10\xf2\x04\"\x06\x08\x8c\x06\x10\x8c\x06\"\x06\x08\xc5\x04\x10\xc5\x04\"\x04\x08\\\x10\\\"\x06\x08\xd2\x06\x10\xd2\x06\"\x06\x08\xdc\x05\x10\xdc\x05*\rCOUNTRY_ALAND*\x16\x43OUNTRY_AMERICAN_SAMOA*\x10\x43OUNTRY_ANGUILLA*\x1b\x43OUNTRY_ANTIGUA_AND_BARBUDA*\x0f\x43OUNTRY_BAHAMAS*\x10\x43OUNTRY_BARBADOS*\x0f\x43OUNTRY_BONAIRE*\x15\x43OUNTRY_BOUVET_ISLAND*&COUNTRY_BRITISH_INDIAN_OCEAN_TERRITORY*\x12\x43OUNTRY_CABO_VERDE*\x0e\x43OUNTRY_CANADA*\x16\x43OUNTRY_CAYMAN_ISLANDS*\x18\x43OUNTRY_CHRISTMAS_ISLAND*\x15\x43OUNTRY_COCOS_ISLANDS*\x14\x43OUNTRY_COTE_DIVOIRE*\x0c\x43OUNTRY_CUBA*\x10\x43OUNTRY_DOMINICA*\x1a\x43OUNTRY_DOMICICAN_REPUBLIC*\x15\x43OUNTRY_FAROE_ISLANDS*#COUNTRY_FRENCH_SOUTHERN_TERRITORIES*\x0f\x43OUNTRY_GRENADA*\x0c\x43OUNTRY_GUAM*\x10\x43OUNTRY_GUERNSEY*)COUNTRY_HEARD_ISLAND_AND_MCDONALD_ISLANDS*\x10\x43OUNTRY_HOLY_SEE*\x0c\x43OUNTRY_IRAN*\x13\x43OUNTRY_ISLE_OF_MAN*\x0f\x43OUNTRY_JAMAICA*\x0e\x43OUNTRY_JERSEY*\x10\x43OUNTRY_KIRIBATI*)COUNTRY_KOREA_DEMOCRATIC_PEOPLES_REPUBLIC*\rCOUNTRY_MACAO*\x0f\x43OUNTRY_MAYOTTE*\x12\x43OUNTRY_MONTSERRAT*\x16\x43OUNTRY_NORFOLK_ISLAND* COUNTRY_NORTHERN_MARIANA_ISLANDS*\x10\x43OUNTRY_PITCAIRN*\x13\x43OUNTRY_PUERTO_RICO*\x0f\x43OUNTRY_REUNION*\x18\x43OUNTRY_SAINT_BARTHELEMY*\x1d\x43OUNTRY_SAINT_KITTS_AND_NEVIS*\x13\x43OUNTRY_SAINT_LUCIA*\x14\x43OUNTRY_SAINT_MARTIN*(COUNTRY_SAINT_VINCENT_AND_THE_GRENADINES*\x1d\x43OUNTRY_SAO_TOME_AND_PRINCIPE*\x12\x43OUNTRY_SEYCHELLES*4COUNTRY_SOUTH_GEORGIA_AND_THE_SOUTH_SANDWICH_ISLANDS*\x10\x43OUNTRY_SVALBARD*\x13\x43OUNTRY_TIMOR_LESTE*\x1b\x43OUNTRY_TRINIDAD_AND_TOBAGO*,COUNTRY_UNITED_STATES_MINOR_OUTLYING_ISLANDS*\x1e\x43OUNTRY_VIRGIN_ISLANDS_BRITISH*\x19\x43OUNTRY_VIRGIN_ISLANDS_US*\x16\x43OUNTRY_WESTERN_SAHARABl\n\x0f\x63om.api.commonsB\x0c\x43ountryProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.country_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.commonsB\014CountryProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_COUNTRY']._serialized_start=43
  _globals['_COUNTRY']._serialized_end=6467
# @@protoc_insertion_point(module_scope)
