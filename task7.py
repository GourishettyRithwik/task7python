import os
from PIL import Image

# Settings
input_folder = "images"
output_folder = "resized"
resize_size = (800, 800)  # Width, Height

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Resize
        img_resized = img.resize(resize_size)

        # Convert format (optional)
        # img_resized = img_resized.convert("RGB")  # Use if converting PNG to JPG

        # Save resized image
        output_path = os.path.join(output_folder, filename)
        img_resized.save(output_path)

        print(f"Resized and saved: {output_path}")

print("✅ All images resized.")
