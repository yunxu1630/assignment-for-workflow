# ---------------------
# Template for WPS function
# ---------------------
from osgeo import ogr

def title():
    return "intersection of geometries" # title of the function

def abstract():
    return "A function that calculates the intersection of geometries." # short description of the function

def inputs():
    return [
            ['geomA', 'Input geometry A', 'the feature in the same reference system.', 'application/json', True],
            ['geomB', 'Input geometry B', 'the feature in the same reference system.', 'application/json', True]
    ]

def outputs():
    return [['intersection_result', 'intersected geometry','the result of intersection of geometries','application/json']]

def execute(parameters):
    geomA = parameters.get('geomA')
    geomB = parameters.get('geomB')
    if (geomA is not None) and (geomB is not None):
        geomA = geomA['value']
        geomB = geomB['value']
    
    sourceA = ogr.CreateGeometryFromJson(geomA)
    sourceB = ogr.CreateGeometryFromJson(geomB)
    
    intersection = sourceA.Intersection(sourceB)
    print("Content-type: application/json")
    print()
    print(intersection.ExportToJson())
