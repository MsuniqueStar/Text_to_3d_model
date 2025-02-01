# 3D Shape Generation from Text Prompts

This project allows the user to generate 3D shapes based on text prompts. By inputting a description such as "a tree", "a house", or "a cube", the program creates the corresponding 3D shape and saves it in the STL format, which can be used for 3D printing or visualization purposes.

## Features
- **Text-based Shape Generation**: The user can input various text prompts to generate different 3D shapes (e.g., cubes, spheres, trees, houses).
- **Interactive Inputs**: The user provides additional details such as size, radius, or height for the shapes, making the generation dynamic.
- **STL Export**: Once the shape is generated, it is exported as an STL file, which can be used in CAD software or 3D printing tools.

## Supported Shapes
- **Cube**: Generates a 3D cube based on user-defined size.
- **Sphere**: Generates a 3D sphere based on user-defined radius.
- **Cylinder**: Generates a 3D cylinder based on user-defined radius and height.
- **Tree**: Combines a cone for the trunk and a sphere for the foliage to create a tree.
- **House**: Combines a cube for the base and a pyramid for the roof to create a house.
- **Other Custom Shapes**: You can easily extend the functionality by adding more shape generation functions.

## Installation
1. Install Python 3.x and the following dependencies:
   - `trimesh`: For 3D shape generation.
   - `numpy`: For numerical operations (used in generating shapes).

2. To install the required packages, run the following command:
   ```bash
   pip install trimesh numpy
