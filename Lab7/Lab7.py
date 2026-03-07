import arcpy


#assign bands
source = "C:\\GEOG676\\M6"
band1 = arcpy.sa.Raster(source + "\\blue.tif")
band2 = arcpy.sa.Raster(source + "\\green.tif")
band3 = arcpy.sa.Raster(source + "\\red.tif")
band4 = arcpy.sa.Raster(source + "\\nir08.tif")
combined = arcpy.CompositeBands_management([band1, band2, band3, band4], source + "\\output_combo.tif")

#hillshade
azimuth = 315
altitude = 45
shadows = 'NO_SHADOWS'
z_factor = 1
arcpy.ddd.HillShade(source + r"\\dem_30m.tif", source + "\\output_Hillshade.tif", azimuth, altitude, shadows, z_factor)

#slope
output_measurement = 'DEGREE'
z_factor = 1
arcpy.ddd.Slope(source + "\\dem_30m.tif", source + "\\output_Slope.tif", output_measurement, z_factor)

print("sucess pls")