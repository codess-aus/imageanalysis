import os
import requests
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = ImageAnalysisClient(
    endpoint=os.getenv("IMAGE_ENDPOINT"),
    credential=AzureKeyCredential(os.getenv("IMAGE_KEY"))
)

image_url = "https://raw.githubusercontent.com/codess-aus/imageanalysis/main/images/circus.png"

# Download the image and get the image data
response = requests.get(image_url)
image_data = response.content

result = client.analyze(
    image_data=image_data,  # Pass the image data
    visual_features=[VisualFeatures.CAPTION, VisualFeatures.READ],
    gender_neutral_caption=True,
    language="en",
)

# Print the result
print(result)