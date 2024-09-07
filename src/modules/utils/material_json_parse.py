import os
import json
import requests

# Load the JSON data
with open('data\pbr_reference\materials.json', 'r') as f:
    materials_data = json.load(f)

# Directory where all material folders will be created
base_dir = 'data\pbr_reference\materials'

# Create the base directory if it doesn't exist
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

# Iterate through each material in the JSON data
for material in materials_data:
    material_name = material['name']
    
    # Create a directory for the material
    material_dir = os.path.join(base_dir, material_name)
    if not os.path.exists(material_dir):
        os.makedirs(material_dir)
    
    # Save material data to a file
    material_file_path = os.path.join(material_dir, f'{material_name}.json')
    with open(material_file_path, 'w') as material_file:
        json.dump(material, material_file, indent=4)
    
    # Download the reference image if available
    if 'reference' in material and material['reference']:
        image_url = material['reference'][0]
        image_name = os.path.join(material_dir, f'{material_name}.jpeg')
        
        # Download the image
        try:
            response = requests.get(image_url, stream=True)
            if response.status_code == 200:
                with open(image_name, 'wb') as img_file:
                    for chunk in response.iter_content(1024):
                        img_file.write(chunk)
            else:
                print(f"Failed to download image for {material_name}: {image_url}")
        except Exception as e:
            print(f"Error downloading image for {material_name}: {e}")

print("Materials data and images have been successfully saved.")