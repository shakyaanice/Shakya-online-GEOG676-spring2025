#Import arcpy module
import arcpy

#Create a geodatabase and garage features
arcpy.env.workspace = r'E:\Coursework\Semester_II\GEOG676_HC\Topic\04\codes_env'
folder_path = r'E:\Coursework\Semester_II\GEOG676_HC\Topic\04'
gdb_name = 'GISLab.gdb'
gdb_path = folder_path + '\\' + gdb_name
arcpy.CreateFileGDB_management(folder_path, gdb_name)

#Extract csv data and convert to feature data
csv_path = r'C:\Users\shaky\OneDrive - Texas A&M University\Documents\GitHub\Shakya-online-GEOG676-spring2025\Lab_4\garages.csv'
garage_layer_name = 'Garage_Points'
garages = arcpy.MakeXYEventLayer_management(csv_path, 'X', 'Y', garage_layer_name)

input_layer = garages
arcpy.FeatureClassToGeodatabase_conversion(input_layer,gdb_path)
garage_points = gdb_path + '\\' + garage_layer_name

#Open Campus geodatabase and copy building features to our geodatabase
campus = r'C:\Users\shaky\OneDrive - Texas A&M University\Documents\GitHub\Shakya-online-GEOG676-spring2025\Lab_4\Campus.gdb'
build_campus = campus + '\Structures'
buildings = gdb_path + '\\' + 'Buildings'

arcpy.Copy_management(build_campus, buildings)

#Reproject features such that the buffer distances are in meters
spatial_ref = arcpy.Describe(buildings).spatialReference
arcpy.Project_management(garage_points, gdb_path + '\Garage_points_reprojected', spatial_ref)

#Buffer the garages based on inputs provided by user
#Setup user input variable
bufferSize_input = int(input("Please enter a buffer size: "))
garageBuffer= arcpy.Buffer_analysis(gdb_path + '\Garage_points_reprojected', gdb_path + '\Garage_points_buffered', bufferSize_input)

#Intersect buffer regions with buildings
arcpy.Intersect_analysis([garageBuffer,buildings], gdb_path + '\Garage_Building_Intersection', 'ALL')

#Save output as csv 
arcpy.TableToTable_conversion(gdb_path + '\Garage_Building_Intersection.dbf', folder_path, 'nearbyBuildings.csv')


