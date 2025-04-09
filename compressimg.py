from PIL import Image
import os

def compress_image(input_path, output_path, quality=30):
    """
    Compress an image and save it to the specified path
    
    Parameters:
    input_path (str): Path to the input image
    output_path (str): Path to save the compressed image
    quality (int): Quality of the compressed image (0-100), lower means more compression
    
    Returns:
    tuple: (original_size, compressed_size) in bytes
    """
    # Open the image
    img = Image.open(input_path)
    
    # Get the original file size
    original_size = os.path.getsize(input_path)
    
    # Save with compression
    img.save(output_path, quality=quality, optimize=True)
    
    # Get the compressed file size
    compressed_size = os.path.getsize(output_path)
    
    return original_size, compressed_size

def main():
    input_path = input("Enter the path to the image to compress: ")
    output_path = input("Enter the path to save the compressed image: ")
    quality = int(input("Enter compression quality (0-100, lower means more compression): "))
    
    try:
        original_size, compressed_size = compress_image(input_path, output_path, quality)
        
        print(f"Original size: {original_size / 1024:.2f} KB")
        print(f"Compressed size: {compressed_size / 1024:.2f} KB")
        print(f"Compression ratio: {original_size / compressed_size:.2f}x")
        print(f"Compressed image saved to: {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()