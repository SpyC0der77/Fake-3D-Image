from gradio_client import Client, handle_file
import os

# Define file paths
input_image_path = 'image.png'  # Replace with your image file path
output_depth_map_path = 'depth.png'
if os.path.exists(output_depth_map_path):
  os.remove(output_depth_map_path)
else:
  print("Depth file does not exist. Skipping...")

# Initialize the Gradio client
client = Client("depth-anything/Depth-Anything-V2")

# Perform the prediction and obtain the result
result = client.predict(
    image=handle_file(input_image_path),
    api_name="/on_submit"
)

print("Depth map returned.")
# Check if the result is valid
if result:
    # Get the file paths from the result
    depth_map_file = result[1]  # Grayscale depth map

    if depth_map_file:
        # Save the depth map to the local directory
        depth_map_file_path = os.path.join(os.getcwd(), output_depth_map_path)

        # Write the file to the local directory
        with open(depth_map_file, 'rb') as src_file:
            with open(depth_map_file_path, 'wb') as dst_file:
                dst_file.write(src_file.read())

        print(f"Depth map saved to: {depth_map_file_path}")
    else:
        print("No depth map was returned by the API.")
else:
    print("No result was returned by the API.")
