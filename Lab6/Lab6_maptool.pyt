# -*- coding: utf-8 -*-

import arcpy
import time


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [GraduatedColorsRenderer]


class GraduatedColorsRenderer(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Graduated Color"
        self.description = "Creates a graduated colored map based on layer attribute"
        self.canRunInBackground = False
        

    def getParameterInfo(self):
        """Define the tool parameters."""
        # original project name
        param0 = arcpy.Parameter(
            displayName="Input ArcGIS Pro Project Name",
            name="aprxInputName",
            datatype="DEFile",
            parameterType="Required",
            direction="Input"
        )

        # specify which layer to use to create color map
        param1 = arcpy.Parameter(
            displayName="Input Layer",
            name="LayerInput",
            datatype="GPLayer",
            parameterType="Required",
            direction="Input"
        )

        # output folder location
        param2 = arcpy.Parameter(
            displayName="Output Location",
            name="OutputLocation",
            datatype="DEFolder",
            direction="Input"
        )

        # output project name
        param3 = arcpy.Parameter(
            displayName="Output Project Name",
            name="OutputProjectName",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        params = [param0, param1, param2, param3]
        return params

    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        # define progressor variables 
        readTime = 3 # time for users to read the progress
        start = 0   # beginning position of the progressor
        max = 100   # end position
        step = 33   # progress interval to move progressor along 

        # set up progressor
        arcpy.SetProgressor("step", "Validating Project File...", start, max, step)
        time.sleep(readTime) # pause the execution for 3 secs

        # add message to the Results Pane
        arcpy.AddMessage("Validating Project File...")

        # access to input project file
        project = arcpy.mp.ArcGISProject(parameters[0].valueAsText) # param0 is the input project file 

        # grab first instance of a map from the .aprx
        campus = project.listMaps('Map')[0]

        # increment progressor
        arcpy.SetProgressorPosition(start + step)
        arcpy.SetProgressorLabel("Finding your map layer...")
        time.sleep(readTime)
        arcpy.AddMessage("Finding your map layer...")

        # loop through layers of map 
        for layer in campus.listLayers():
            # check if the layer is a feature layer
            if layer.isFeatureLayer:
                # copy the layer's symbology
                symbology = layer.symbology
                # make sure the symbology has renderer attribute
                if hasattr(symbology, 'renderer'):
                    # check layer name 
                    if layer.name == parameters[1].valueAsText: # check if layer name match input layer 

                        # increment progressor
                        arcpy.SetProgressorPosition(start + step*2) # now is 66% completed 
                        arcpy.SetProgressorLabel("Calculating and classifying...")
                        time.sleep(readTime)
                        arcpy.AddMessage("Calculating and classifying...")

                        # update the copy's renderer to "Graduated Colors Renderer"
                        symbology.updateRenderer('GraduatedColorsRenderer')

                        # tell arcpy which field to base chloropleth off of 
                        symbology.renderer.classificationField = "Shape_Area"

                        # # increment progressor
                        # arcpy.SetProgressorPosition(start + step*2) # now is 66% completed 
                        # arcpy.SetProgressorLabel("Cleaning up...")
                        # time.sleep(readTime)
                        # arcpy.AddMessage("Cleaning up...")

                        # set how many classes for map
                        symbology.renderer.breakCount = 5

                        # set color ramp
                        symbology.renderer.colorRamp = project.listColorRamps('Oranges (5 Classes)')[0]

                        # set layer's symboloby equal to the copy's 
                        layer.symbology = symbology
                        
                        arcpy.AddMessage("Finnish generating layer...")

                    else:
                        print("No layers found")

        # increment progressor
        arcpy.SetProgressorPosition(start + step*3) # now is 99% completed
        arcpy.SetProgressorLabel("Saving...")
        time.sleep(readTime)
        arcpy.AddMessage("Saving...")

        project.saveACopy(parameters[2].valueAsText + '\\' + parameters[3].valueAsText + '.aprx')
        # param2 is folder location and param3 is name of new project

        return None


