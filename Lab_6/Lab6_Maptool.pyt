# -*- coding: utf-8 -*-

import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [GraduatedColorRenderer]


class GraduatedColorRenderer(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Graduated color"
        self.description = "creates a graduated colored map based on a specific attribute of a layer"
        self.canRunInBackground = False
        self.category = "MapTools"

    def getParameterInfo(self):
        """Define the tool parameters."""
        #original project name
        param0 = arcpy.Parameter(  
            displayName = "Input ArcGIS Pro Project Name",
            name = "aprxInputName",
            datatype= "DEFile",
            parameterType= "Required",
            direction= "Input"
        )

        #choose a layer to classify to create graduated color map
        param1 = arcpy.Parameter(  
            displayName = "Layer to Classify",
            name = "LayertoClassify",
            datatype= "GPLayer",
            parameterType= "Required",
            direction= "Input"
        )

        #create an output folder location
        param2 = arcpy.Parameter(  
            displayName = "Output Location",
            name = "OutputLocation",
            datatype= "DEFolder",
            parameterType= "Required",
            direction= "Input"
        )

        #output project name
        param3 = arcpy.Parameter(  
            displayName = "Output Project Name",
            name = "OutputProjectName",
            datatype= "GPString",
            parameterType= "Required",
            direction= "Input"
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
        #Define progressor variables
        readTime = 3  #the time for users to read the progress 
        start = 0     #beginning position
        max = 100     #end position
        step = 33     #the progress interval to move the progressor along 

        #Setup Progressor
        arcpy.SetProgressor("step", "Validating Project File....", start,max,step)
        time.sleep(readTime) 
        arcpy.AddMessage("Validating Project File....")

        #Project File
        project = arcpy.mp.ArcGISProject(parameters[0].valueAsText)

        #Intakes the first instance of a map from the .aprx
        campus = project.listMaps('Map')[0]

        #Increment Progressor
        arcpy.SetProgressorPosition(start + step)
        arcpy.SetProgressorLabel("Finding your map layer...")
        time.sleep(readTime)
        arcpy.AddMessage("Finding your map layer...")

        #Loop through the layers of the map
        for layer in campus.listLayers():
            # Check if layer is a feature layer
            if layer.isFeatureLayer:
                # Obtain a copy of the layer's symbology
                symbology = layer.symbology
                # Check if it has a 'renderer' attribute
                if hasattr(symbology, 'renderer'):
                    # Check layer name
                    if layer.name == parameters[1].valueAsText:

                        #Increment Progressor
                        arcpy.SetProgressorPosition(start + step*2) #now is 66% completed
                        arcpy.SetProgressorLabel("Calculating and classifying...")
                        time.sleep(readTime)
                        arcpy.AddMessage("Calculating and classifying...")

                        # Update the copy's renderer to be 'GraduatedColorsRenderer'
                        symbology.updateRenderer('GraduatedColorsRenderer')
                        
                        # Tell arcpy which field to base our choropleth off of
                        symbology.renderer.classificationField = "Shape_Area"
                
                        # Set how many classes to have 
                        symbology.renderer.breakCount = 5
                        
                        # Set the color ramp
                        symbology.renderer.colorRamp = project.listColorRamps('Blues (5 classes)')[0]
                        
                        # Set the layer's actual symbology equal to the copy's
                        layer.symbology = symbology 

                        arcpy.AddMessage("Finishing Generating Layer...")
                    else:
                        print("No layers found")

        #Increment Progressor
        arcpy.SetProgressorPosition(start + step*3) #now is 99% completed
        arcpy.SetProgressorLabel("Saving...")
        time.sleep(readTime)
        arcpy.AddMessage("Saving...")               

        project.saveACopy(parameters[2].valueAsText + "\\" + parameters[3].valueAsText + ".aprx")
        #param 2 = folder location and param 3 = name of new project
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
