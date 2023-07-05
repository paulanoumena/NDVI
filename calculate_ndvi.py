import argparse
import cv2
import numpy as np


def compute_ndvi(nir_image_path: str, r_image_path: str) -> np.ndarray:
    
    # Read R and NIR image
    nir_image = cv2.imread(nir_image_path, cv2.IMREAD_GRAYSCALE)
    r_image = cv2.imread(r_image_path, cv2.IMREAD_GRAYSCALE)

    # Check image sizes are equal
    if nir_image.shape != r_image.shape:
        raise ValueError('Images sizes are not equal')

    # Calculate NDVI
    try:
        nir = np.float32(nir_image)
        r = np.float32(r_image)

        ndvi = (nir - r) / (nir + r)

        return ndvi

    except Exception as e:
        raise ValueError("Error computing NDVI: {}".format(str(e)))


def visualize_ndvi(ndvi: np.ndarray, colormap: bool = True) -> None:
    
    # Apply colormap
    if colormap:
        ndvi = cv2.applyColorMap((ndvi * 255).astype(np.uint8), cv2.COLORMAP_RAINBOW)

    # Show ndvi image
    cv2.imshow('NDVI image', ndvi)

    # Waits for user to press any key
    cv2.waitKey(0)

    # Closing all open windows
    cv2.destroyAllWindows()


if __name__ == '__main__':

    COLORMAP = True # set variable true if you want to visualize the NDVI value with a colormap
    
    nir_image_path = "/path/to/NIR/image"
    r_image_path = "/path/to/R/image"

   
    # Compute NDVI
    try:
        ndvi = compute_ndvi(nir_image_path, r_image_path)

        # Visualize NDVI
        visualize_ndvi(ndvi, COLORMAP)


    except ValueError as e:
        print(f"Error: {str(e)}")