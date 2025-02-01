import trimesh
import numpy as np


def generate_tree():
   
    
    trunk = trimesh.creation.cone(radius=0.5, height=2.0, sections=32)
    trunk.apply_translation([0, 0, 1])  

    
    foliage = trimesh.creation.icosphere(radius=1.5)
    foliage.apply_translation([0, 0, 3]) 

    
    return trunk + foliage


def generate_house():
    
    base = trimesh.creation.box(extents=[4, 4, 2])
    base.apply_translation([0, 0, 1])  

   
    roof_vertices = np.array([
        [-2, -2, 2], [2, -2, 2], [2, 2, 2], [-2, 2, 2],  
        [0, 0, 4]  
    ])
    roof_faces = np.array([
        [0, 1, 4], [1, 2, 4], [2, 3, 4], [3, 0, 4], 
        [0, 1, 2], [0, 2, 3]  
    ])
    roof = trimesh.Trimesh(vertices=roof_vertices, faces=roof_faces)

    return base + roof


def generate_shape_from_prompt(prompt):
   
    prompt = prompt.lower()

    if "cube" in prompt:
        size = float(input("Enter the size of the cube (edge length): ").strip())
        return trimesh.creation.box(extents=[size, size, size])

    elif "sphere" in prompt:
        radius = float(input("Enter the radius of the sphere: ").strip())
        return trimesh.creation.icosphere(radius=radius)

    elif "cylinder" in prompt:
        radius = float(input("Enter the radius of the cylinder: ").strip())
        height = float(input("Enter the height of the cylinder: ").strip())
        return trimesh.creation.cylinder(radius=radius, height=height)

    elif "tree" in prompt:
        return generate_tree()

    elif "house" in prompt:
        return generate_house()

    else:
        print(f"Sorry, I don't understand how to create a shape for '{prompt}'. Generating a default cube.")
        return trimesh.creation.box(extents=[1, 1, 1])  


def main():
    
    try:
        
        prompt = input("Enter the shape you want to generate (e.g., 'a tree', 'a house', 'a cube'): ").strip()

       
        shape = generate_shape_from_prompt(prompt)

        
        if shape:
            output_file = "generated_shape.stl"
            shape.export(output_file)
            print(f"Shape successfully generated and saved as: {output_file}")
        else:
            print("Failed to generate the shape.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
