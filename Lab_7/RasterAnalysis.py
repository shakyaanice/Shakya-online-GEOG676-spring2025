import arcpy

#Assign bands
path = r"E:\Coursework\Semester_II\GEOG676_HC\Topic\07"
band2 = arcpy.sa.Raster (path + r"\Band2.tif") #blue
band3 = arcpy.sa.Raster (path + r"\Band3.tif") #green
band4 = arcpy.sa.Raster (path + r"\Band4.tif") #red
band5 = arcpy.sa.Raster (path + r"\Band5.tif") #NIR

combined = arcpy.CompositeBands_management([band2,band3, band4, band5], path + r"\output_combined.tif")

#Hillshade
azimuth = 315
altitude = 45
shadows = 'NO_SHADOWS'
z_factor = 1
arcpy.ddd.HillShade(path + r"\DEM_GC.tif", path + r"\output_Hillshade.tif", azimuth, altitude, shadows, z_factor)

#Slope
output_measurement = 'DEGREE'
z_factor = 1
arcpy.ddd.Slope(path + r"\DEM_GC.tif", path + r"\output_Slope.tif", output_measurement, z_factor)
print("Success!!")