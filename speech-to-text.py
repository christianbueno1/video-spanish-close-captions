import openai

# Set up OpenAI API credentials
openai.api_key = "YOUR_API_KEY"

# Read the MP3 file
with open("path/to/your/file.mp3", "rb") as file:
    audio_data = file.read()

# Convert audio to text using the OpenAI API
response = openai.Completion.create(
    engine="davinci",
    prompt=audio_data,
    max_tokens=100,
    temperature=0.7,
    n=1,
    stop=None,
)

# Get the generated text
text = response.choices[0].text.strip()

# Save the text or subtitles to a file
with open("texts/miracles-blind/subtitles.txt", "w") as file:
    file.write(text)
