# Hannah Diaz
# GEOG 676 GIS Programming
# Spring 2026
# 19 February 2026

# Lab 4 - Fun with ArcPy

import arcpy
arcpy.env.workspace = r'C:\GEOG676\M5'

# create new gdb, 'newGeoDB.gdb'
# use fxn CreateFileGDB_management()
folderPath = r'C:\GEOG676\M5'
gdbName = 'newGeoDB.gdb'
gdbPath = folderPath + '\\' + gdbName
arcpy.CreateFileGDB_management(folderPath, gdbName) # creation of new gdb


# create new feature layer w X/Y coords of garages using garage.csv file
# use fxn MakeXYEventLayer_management()
# note: the new feature layer will be stored in this script under variable named 'garages'
csvPath = r'C:\GEOG676\M5\garages.csv'
garageLayerName = 'Garage_Points'
garages = arcpy.MakeXYEventLayer_management(csvPath, 'X', 'Y', garageLayerName)


# next need to actually save the feature into the new gdb
# use fxn FeatureClassToGeodatabase_conversion()
arcpy.FeatureClassToGeodatabase_conversion(garages, gdbPath)

garageLayerPath = gdbPath + '\\' + garageLayerName


# using Campus.gdb, use Structures layer > copy into new gdb
# use fxn Copy_management()
campus = r'C:\GEOG676\M5\Campus.gdb'
campus_Buildings = campus + '\\Structures'
newGeoDB_Buildings = gdbPath + '\\' + 'Buildings'
arcpy.Copy_management(campus_Buildings, newGeoDB_Buildings)


# units of X/Y coords in csv is degrees; just geographic coords, not projected
# Campus.gdb Structure layer uses projected coordinate system
# need to reproject garage layer (that was retrieved from csv) so that Buildings layer 
# and Garage_Points layer share same spatial reference

# step 1: extract spat ref from buildings layer
spatial_ref = arcpy.Describe(newGeoDB_Buildings).spatialReference
# step 2: re-project 
arcpy.Project_management(garageLayerName, gdbPath + '\\Garage_Points_reprojected', spatial_ref)

# now can buffer
bufferInput = int(input("Please enter a buffer size: "))
garageBuffered = arcpy.Buffer_analysis(gdbPath + '\\Garage_Points_reprojected', gdbPath + '\\Garage_Points_buffered', bufferInput)

# intesect 
arcpy.Intersect_analysis([garageBuffered, newGeoDB_Buildings], gdbPath + '\\Garage_Building_intersection', 'ALL')

# save attribute table of Garage_Building_intersection feature to seperate csv file 
# note: 1st param doesn't use feature itself, uses .dbf
arcpy.TableToTable_conversion(gdbPath + '\\Garage_Building_intersection.dbf', 'C:\\GEOG676\\M5', 'nearbyBuildings.csv')






