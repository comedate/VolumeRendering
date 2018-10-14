# coding=utf-8
from vtk import *

import render_reader

opactiyTransferFunction = vtk.vtkPiecewiseFunction()
opactiyTransferFunction.AddPoint(120, 0.0)
opactiyTransferFunction.AddPoint(250, 1.0)
opactiyTransferFunction.AddPoint(520, 1.0)
opactiyTransferFunction.AddPoint(650, 0.0)

colorTransferFunction = vtk.vtkColorTransferFunction()
colorTransferFunction.AddRGBPoint(120, 255 / 255.0, 98 / 255.0, 98 / 255.0)
colorTransferFunction.AddRGBPoint(250, 255 / 255.0, 255 / 255.0, 180 / 255.0)
colorTransferFunction.AddRGBPoint(520, 1.0, 1.0, 1.0)
colorTransferFunction.AddRGBPoint(650, 1.0, 1.0, 1.0)

gradientTransferFunction = vtk.vtkPiecewiseFunction()
gradientTransferFunction.AddPoint(120, 2.0)
gradientTransferFunction.AddPoint(250, 2.0)
gradientTransferFunction.AddPoint(520, 0.1)
gradientTransferFunction.AddPoint(650, 0.1)

volumeProperty = vtk.vtkVolumeProperty()
volumeProperty.SetColor(colorTransferFunction)
volumeProperty.SetScalarOpacity(opactiyTransferFunction)
volumeProperty.SetGradientOpacity(gradientTransferFunction)
volumeProperty.ShadeOn()   # 阴影
volumeProperty.SetInterpolationTypeToLinear()   # 直线与样条插值之间逐发函数
volumeProperty.SetAmbient(0.2)   # 环境光系数
volumeProperty.SetDiffuse(0.9)   # 漫反射
volumeProperty.SetSpecular(0.2)   # 高光系数
volumeProperty.SetSpecularPower(10)   # 高光强度

#compositeRaycastFunction = vtk.vtkVolumeRayCastCompositeFunction()

volumeMapper = vtk.vtkFixedPointVolumeRayCastMapper() # vtkFixedPointVolumeRayCastMapper  vtkVolumeRayCastMapper
# volumeMapper.SetVolumeRayCastFunction(compositeRaycastFunction)   # 载入体绘制方法
volumeMapper.SetInputConnection(render_reader.reader_image_cast.GetOutputPort())
# fixedPointVolumeMapper = vtkFixedPointVolumeRayCastMapper::New()
# fixedPointVolumeMapper.SetInput(dicomImagereader.GetOutput())

volume =  vtk.vtkVolume()
volume.SetMapper(volumeMapper)
volume.SetProperty(volumeProperty)   # 设置体属性

ren1 = vtk.vtkRenderer()
ren1.AddVolume(volume)
ren1.SetBackground(1, 1, 1)

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren1)
renWin.SetSize(800, 800)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

renWin.Render()
iren.Start()
