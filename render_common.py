import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')


"""
This file is mainly to VolumeRendering to Get Image2D using vtkGPURaycastingMapper and vtkRender
This interface  follows such rules:
a. Logger
"""
