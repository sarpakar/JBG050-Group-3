# -*- coding: utf-8 -*-
"""
Created on Wed May 17 16:49:38 2023

@author: Goshko
"""


import shapely as shp
import geopandas as gpd


path_borders = 'C:\\Users\\Goshko\\Desktop\\DC 2\\JBG050-Group-3\\data_borders\\Data\\GB\\district_borough_unitary_ward_region.shp'

data = gpd.read_file(path_borders)

wards = ['Childs Hill Ward', 'Edgware Ward', 'Colindale North Ward', 'Barnet Vale Ward',
       'Brunswick Park Ward', 'Burnt Oak Ward', 'Colindale South Ward', 'Cricklewood Ward',
       'East Barnet Ward', 'East Finchley Ward', 'Edgwarebury Ward',
       'Finchley Church End Ward', 'Friern Barnet Ward', 'Garden Suburb Ward',
       'Golders Green Ward', 'West Finchley Ward', 'Hendon Ward', 'High Barnet Ward',
       'Mill Hill Ward', 'Totteridge & Woodside Ward', 'Underhill Ward', 'West Hendon Ward',
       'Whetstone Ward', 'Woodhouse Ward']

borders_barnet = data[data['NAME'].isin(wards)]
borders_barnet = borders_barnet[['NAME', 'AREA_CODE', 'geometry']]
borders_barnet = borders_barnet[borders_barnet['AREA_CODE'] == 'LBW']
borders_barnet.drop(index = [6376], inplace=True)
borders_barnet.reset_index(inplace=True)


path_sas = 'C:\\Users\\Goshko\\Desktop\\DC 2\\JBG050-Group-3\\stop_and_search.csv'
sas = gpd.read_file(path_sas)

geometry = gpd.points_from_xy(sas['Longitude'], sas['Latitude'], crs='OSGB36')


sas['geometry'] = geometry.to_crs(epsg=4277)
borders_barnet['geometry'] = borders_barnet['geometry'].to_crs(epsg=4277)



intersection = gpd.overlay(borders_barnet, sas, how='intersection', keep_geom_type=False)
intersection = intersection[['NAME','Type','Date']]

intersection.to_csv('stop_and_search_preprocessed.csv')


    
    
