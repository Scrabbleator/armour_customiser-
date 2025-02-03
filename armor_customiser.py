import openai  # If using DALL·E
import requests
from PIL import Image
from io import BytesIO

# OpenAI API Key (Replace with your own)
openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_armor_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    image_url = response['data'][0]['url']
    return image_url

# Button to Generate Image
if st.button("Generate Armor Image"):
    with st.spinner("Generating..."):
        image_url = generate_armor_image(prompt)
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
        st.image(image, caption="AI-Generated Armor")
