import gradio as gr

def transcribe(audio):
    return f"the audio in text: {audio} !"

# demo = gr.Interface(
#     fn=greet,
#     inputs=["text", "slider"],
#     outputs=["text"],
# )

# demo = gr.Interface(
#     fn=transcribe,
#     inputs=[
#         gr.Audio(source="microphone", type="filepath", label="Record Audio")
#     ],
#     outputs=[
#         "text"
#     ],
# )

demo = gr.Interface(
    fn=transcribe,
    # inputs="audio",
    inputs=gr.Audio(sources=["microphone"]),
    # inputs=gr.Audio(sources="microphone", type="filepath"),
    outputs="text"
)
demo.launch()
