
import arcpy
from arcpy import env
from arcpy.sa import *
arcpy.env.workspace = r"C:\Projects\Wetlands\2018UintaBasinLidar\extracted\tifs" ##workspace

arcpy.env.overwriteOutput = False
outfolder=r'C:\Projects\Wetlands\2018UintaBasinLidar'


arcpy.CheckOutExtension("Spatial")
rasters = arcpy.ListRasters() ### or arcpy.ListFeatureClasses
print (rasters)
for raster in rasters:
    arcpy.MosaicToNewRaster_management(raster, outfolder,"out_mos.img") ##input arcpy geoprocessing tool

arcpy.CheckInExtension("Spatial")

