from PIL import Image
import os

def xor_images(image1_path, image2_path, output_path):
    try:
        # Open the images
        with Image.open(image1_path) as img1, Image.open(image2_path) as img2:
            # Ensure both images are in RGB mode
            img1 = img1.convert('RGB')
            img2 = img2.convert('RGB')
            
            # Check if images have the same size
            if img1.size != img2.size:
                raise ValueError("Images must have the same dimensions")
            
            # Create a new image for the result
            result = Image.new('RGB', img1.size)
            
            # Get the pixel data
            pixels1 = img1.load()
            pixels2 = img2.load()
            pixels_result = result.load()
            
            # Perform XOR operation on each pixel
            for x in range(img1.width):
                for y in range(img1.height):
                    r1, g1, b1 = pixels1[x, y]
                    r2, g2, b2 = pixels2[x, y]
                    
                    # XOR each color channel
                    r = r1 ^ r2
                    g = g1 ^ g2
                    b = b1 ^ b2
                    
                    pixels_result[x, y] = (r, g, b)
            
            # Save the result
            result.save(output_path)
            print(f"XOR result saved as {output_path}")
    
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except PermissionError:
        print(f"Error: Permission denied when trying to save {output_path}")
    except OSError as e:
        print(f"Error: OS error occurred - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Define input and output paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image1_path = os.path.join(current_dir, "lemur.png")
    image2_path = os.path.join(current_dir, "flag.png")
    output_path = os.path.join(current_dir, "result.png")
    
    # Check if input files exist
    if not os.path.exists(image1_path):
        print(f"Error: {image1_path} not found")
    elif not os.path.exists(image2_path):
        print(f"Error: {image2_path} not found")
    else:
        xor_images(image1_path, image2_path, output_path)
