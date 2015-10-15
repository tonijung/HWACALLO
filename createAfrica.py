#!/usr/bin/env python

import arcpy
from arcpy import env

# Set directory
env.workspace = "C:/hwacallo/countries/"

# Local variables:
countries = ["ABW", "AFG", "AIA", "ALA", "ALB", "AND", "ARE", "ARG", "ARM", "ASM",
             "ATA", "ATF", "ATG", "AUS", "AUT", "AZE", "BEL", "BES", "BGD", "BGR",
             "BHR", "BHS", "BIH", "BLM", "BLR", "BLZ", "BMU", "BOL", "BRA", "BRB",
             "BRN", "BTN", "BVT", "BWA", "CA-", "CAN", "CCK", "CHE", "CHL", "CHN",
             "CL-", "COG", "COK", "COL", "CPV", "CRI", "CUB", "CUW", "CXR", "CYM",
             "CYP", "CZE", "DEU", "DJI", "DMA", "DNK", "DOM", "DZA", "ECU", "EGY",
             "ERI", "ESH", "ESP", "EST", "FIN", "FJI", "FLK", "FRA", "FRO", "FSM",
             "GBR", "GEO", "GGY", "GIB", "GLP", "GRC", "GRD", "GRL", "GTM", "GUF",
             "GUM", "GUY", "HKG", "HMD", "HND", "HRV", "HTI", "HUN", "IDN", "IMN",
             "IND", "IOT", "IRL", "IRN", "IRQ", "ISL", "ISO", "ISR", "ITA", "JAM",
             "JEY", "JOR", "JPN", "KAZ", "KGZ", "KHM", "KIR", "KNA", "KO-", "KOR",
             "KWT", "LAO", "LBN", "LBY", "LCA", "LIE", "LKA", "LTU", "LUX", "LVA",
             "MAC", "MAF", "MAR", "MCO", "MDA", "MDV", "MEX", "MHL", "MKD", "MLT",
             "MMR", "MNE", "MNG", "MNP", "MRT", "MSR", "MTQ", "MUS", "MYS", "MYT",
             "NCL", "NFK", "NIC", "NIU", "NLD", "NOR", "NPL", "NRU", "NZL", "OMN",
             "PAK", "PAN", "PCN", "PER", "PHL", "PLW", "PNG", "POL", "PRI", "PRK",
             "PRT", "PRY", "PSE", "PYF", "QAT", "REU", "ROU", "RUS", "SAU", "SGP",
             "SGS", "SHN", "SJM", "SLB", "SLV", "SMR", "SMX", "SP-", "SPM", "SRB",
             "SSD", "STP", "SUR", "SVK", "SVN", "SWE", "SYC", "SYR", "TCA", "THA",
             "TJK", "TKL", "TKM", "TLS", "TON", "TTO", "TUN", "TUR", "TUV", "TWN",
             "UKR", "UMI", "URY", "USA", "UZB", "VAT", "VCT", "VEN", "VGB", "VIR",
             "VNM", "VUT", "WLF", "WSM", "YEM"]
GADM2_shp = "/gadm2.shp"
copy_shp = "/copy.shp"
africa_shp = "/africa.shp"

# Create new Africa shapefile
arcpy.CopyFeatures_management(GADM2_shp, copy_shp)
print "Created intermediate shapefile"

# Delete unused countries
features = arcpy.UpdateCursor(r"copy.shp")
for feature in features:
    for country in countries:
        if feature.ISO == country:
            features.deleteRow(feature)
del feature,features
print "Deleted unnecessary features (countries)"

# Dissolve smaller administrative levels to administrative level 1
arcpy.Dissolve_management(copy_shp, africa_shp,
                          "ID_0;ISO;NAME_0;ID_1;NAME_1", "",
                          "MULTI_PART", "DISSOLVE_LINES")
print "Dissolved Africa to administrative level 1"

print "FIN"
