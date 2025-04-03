"""
Script to generate a favicon.ico file
"""
from PIL import Image, ImageDraw, ImageFont
import os

def create_favicon():
    # Create a 32x32 pixel image with black background
    img = Image.new('RGB', (32, 32), color=(0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw a cyan circle to match the accent color
    draw.ellipse((4, 4, 28, 28), fill=(0, 184, 212))
    
    # Save the image as favicon.ico
    output_dir = 'static/img'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    img.save(os.path.join(output_dir, 'favicon.ico'))
    print("Favicon created successfully!")

if __name__ == "__main__":
    create_favicon() 