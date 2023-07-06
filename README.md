# NDVI Calculation and Visualization
This Python script computes and visualizes the Normalized Difference Vegetation Index (NDVI) for two input images: a near-infrared (NIR) image and a red (R) image. The NDVI is a commonly used index to assess vegetation health and vigor based on the difference in reflectance between the NIR and red bands. This script uses the OpenCV library to read and process the input images and NumPy to perform the NDVI calculation.

### NDVI Explanation
NDVI stands for Normalized Difference Vegetation Index. It is a simple index that measures the difference between the reflectance of near-infrared (NIR) and red (R) bands of the electromagnetic spectrum. NDVI is widely used in remote sensing and agriculture to assess vegetation health, vigor, and biomass.

NDVI values range from -1 to +1, with negative values indicating water bodies or clouds, and positive values indicating vegetation. The higher the NDVI value, the more vegetation is present. NDVI values close to zero indicate barren land or non-vegetated areas.

NDVI is calculated using the following formula:

```
NDVI = (NIR - R) / (NIR + R)
```
where NIR is the reflectance in the near-infrared band and R is the reflectance in the red band. The resulting NDVI value is a ratio of the difference between the two reflectances to their sum.

<p align="center">
<img src="https://github.com/paulanoumena/NDVI/blob/main/ndvi_process.png" width="800"/>
</p>

## Requirements
To run the script, you need to have OpenCV and NumPy libraries installed in your Python environment. You can install them using pip:

```
pip install opencv-python
pip install numpy
```

## Usage
To run the script, specify the paths to the NIR and R images in the nir_image_path and r_image_path variables, respectively. You can also set the COLORMAP variable to True if you want to visualize the NDVI value with a colormap.

```
python ndvi.py
```
The script will compute the NDVI and display the resulting image. You can close the image window by pressing any key.
NDVI values can be displayed as grayscale images or using a colormap, where different colors represent different NDVI values. In this script, the visualize_ndvi function can apply a colormap to the NDVI image if the COLORMAP variable is set to True.



