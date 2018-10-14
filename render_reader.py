
# coding=utf-8
from vtk import *

dicom_image_reader = vtk.vtkDICOMImageReader()
dicom_image_reader.SetDirectoryName("D:\\CodeProject\\Hover\\Data\\Dicom\\02ef8f31ea86a45cfce6eb297c274598\\series-000001\\")
dicom_image_reader.SetDataByteOrderToLittleEndian()
dicom_image_reader.SetDataSpacing(3.2, 3.2, 1.5)
dicom_image_reader.Update()

print(dicom_image_reader.GetDataSpacing())
print(dicom_image_reader.GetImagePositionPatient())
print( dicom_image_reader.GetImageOrientationPatient())

print("H:" + str(dicom_image_reader.GetHeight()) + "W:" + str(dicom_image_reader.GetWidth()))

reader_image_cast = vtk.vtkImageCast()
reader_image_cast.SetInputConnection(dicom_image_reader.GetOutputPort())
reader_image_cast.SetOutputScalarTypeToUnsignedShort()
reader_image_cast.Update()