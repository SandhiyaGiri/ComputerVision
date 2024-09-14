from PIL import Image, ImageDraw, ImageFont

def create_gif():
    # Define image size and colors
    width, height = 500, 200
    blue = (0, 0, 255)
    white = (255, 255, 255)
    text = "Computer\n   Vision"
    
    # Create frames for the GIF
    frames = []
    for i in range(2):
        # Alternate background and text colors
        if i % 2 == 0:
            bg_color = blue
            text_color = white
        else:
            bg_color = white
            text_color = blue
        
        # Create a new image with the specified background color
        img = Image.new("RGB", (width, height), bg_color)
        draw = ImageDraw.Draw(img)
        
        # Load a font
        try:
            font = ImageFont.truetype("arial.ttf", 40)  # Adjust the font size as needed
        except IOError:
            font = ImageFont.load_default()
        
        # Calculate text size using getbbox
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        # Calculate text position
        text_x = (width - text_width) // 2
        text_y = (height - text_height) // 2
        
        # Draw the text onto the image
        draw.text((text_x, text_y), text, font=font, fill=text_color)
        
        # Append the image to frames
        frames.append(img)

    # Save the frames as a GIF
    frames[0].save('computer_vision.gif',
                   save_all=True,
                   append_images=frames[1:],
                   duration=500,  # Duration of each frame in milliseconds
                   loop=0)  # Loop forever

if __name__ == "__main__":
    create_gif()