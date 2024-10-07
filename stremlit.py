import streamlit as st
from PIL import Image, ImageFilter
import io

# Title of the app
st.title("Image Upload and Processing")

# Instructions
st.write("Upload an image file (JPEG, PNG) to display it and apply filters.")

# Image upload
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# If an image is uploaded
if uploaded_file is not None:
    # Open the image
    image = Image.open(uploaded_file)

    # Display the original image
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Display image metadata
    st.write(f"File Name: {uploaded_file.name}")
    st.write(f"File Type: {uploaded_file.type}")
    st.write(f"File Size: {uploaded_file.size / 1024:.2f} KB")
    st.write(f"Image dimensions: {image.size[0]} x {image.size[1]} pixels")

    # Image processing options
    st.write("### Choose a filter to apply:")
    filter_option = st.selectbox("Select Filter", ["None", "Grayscale", "Blur"])

    # Process the image based on the selected filter
    if filter_option == "Grayscale":
        processed_image = image.convert("L")
    elif filter_option == "Blur":
        processed_image = image.filter(ImageFilter.BLUR)
    else:
        processed_image = image

    # Display the processed image
    st.write("### Processed Image:")
    st.image(processed_image, caption=f'Processed Image with {filter_option} filter', use_column_width=True)

    # Create a download button for the processed image
    buf = io.BytesIO()
    processed_image.save(buf, format="PNG")
    byte_im = buf.getvalue()
    st.download_button(
        label="Download Processed Image",
        data=byte_im,
        file_name=f"processed_{uploaded_file.name}",
        mime="image/png"
    )

    # Display original and processed images side by side
    col1, col2 = st.columns(2)
    with col1:
        st.write("### Original Image:")
        st.image(image, caption='Uploaded Image', use_column_width=True)
    with col2:
        st.write("### Processed Image:")
        st.image(processed_image, caption=f'Processed Image with {filter_option} filter', use_column_width=True)

