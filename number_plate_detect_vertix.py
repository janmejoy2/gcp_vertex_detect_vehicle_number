import vertexai
from vertexai.preview.vision_models import Image, ImageTextModel

project_id = <PROVIDE_YOUR_PROJECT_ID>
input_file = "C:\AWSHackthon\Car Image\TataNexon\Front.jpg"
question = "What is the registration number"  # The question about the contents of the image.

vertexai.init(project=project_id, location="us-central1")

model = ImageTextModel.from_pretrained("imagetext@001")
source_img = Image.load_from_file(location=input_file)

answers = model.ask_question(
    image=source_img,
    question=question,
    # Optional parameters
    number_of_results=1,
)

print(answers)
