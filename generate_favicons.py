"""
Script to generate different favicon sizes from the existing favicon.ico file.
Requires Pillow: pip install Pillow
"""
from PIL import Image
import os

def generate_favicons():
    # Path to the favicon.ico file
    favicon_path = 'static/img/favicon.ico'
    output_dir = 'static/img'
    
    try:
        # Open the favicon.ico file
        favicon = Image.open(favicon_path)
        
        # Convert to PNG and save in different sizes
        sizes = {
            'favicon-16x16.png': (16, 16),
            'favicon-32x32.png': (32, 32),
            'apple-touch-icon.png': (180, 180)
        }
        
        for filename, size in sizes.items():
            resized_favicon = favicon.resize(size)
            output_path = os.path.join(output_dir, filename)
            resized_favicon.save(output_path)
            print(f"Generated {output_path}")
            
        print("All favicons generated successfully!")
        
    except Exception as e:
        print(f"Error generating favicons: {e}")

if __name__ == "__main__":
    generate_favicons() 