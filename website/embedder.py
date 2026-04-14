import base64
import os

def get_base64_string(filepath, mime_type):
    with open(filepath, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode('utf-8')
    return f"data:{mime_type};base64,{encoded_string}"

def create_single_file():
    print("Reading lv.html...")
    # Reading your original file
    with open("lv.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    # Convert and embed the 8 images
    for i in range(1, 9):
        img_name = f"Image{i}.jpg"
        if os.path.exists(img_name):
            print(f"Embedding {img_name}...")
            b64_img = get_base64_string(img_name, "image/jpeg")
            html_content = html_content.replace(img_name, b64_img)
        else:
            print(f"Warning: {img_name} not found.")

    # Convert and embed the audio
    if os.path.exists("music.mp3"):
        print("Embedding music.mp3...")
        b64_audio = get_base64_string("music.mp3", "audio/mpeg")
        html_content = html_content.replace("music.mp3", b64_audio)
    else:
        print("Warning: music.mp3 not found.")

    # Save the final standalone file
    output_filename = "lv_whatsapp.html"
    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(html_content)
    
    print(f"\nSuccess! You can now send '{output_filename}' directly via WhatsApp.")

if __name__ == "__main__":
    create_single_file()