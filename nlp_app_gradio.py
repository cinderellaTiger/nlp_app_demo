import gradio as gr
from transformers import pipeline


def model_inference(text):
    json_out = {
        "base64": "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAIBAQEBAQIBAQECAg...",
        "result": "123456"
    }
    return text, json_out


examples = [
    ["The Moon's orbit around Earth has"],
    ["The smooth Borealis basin in the Northern Hemisphere covers 40%"],
]


def clear_all():
    return None, None, None


with gr.Blocks() as demo:
    gr.Markdown("Text Generation")

    with gr.Column(scale=1, min_width=100):
        text_input = gr.Textbox(placeholder="Type here...", lines=4)

        with gr.Row():
            btn1 = gr.Button("Clear")
            btn2 = gr.Button("Submit")

        text_output = gr.Textbox(placeholder="Type here...", lines=4)
        #img_out = gr.Image(shape=(200, 200), label="输出图片").style(height=200)
        json_out = gr.JSON(label="jsonOutput")

    btn2.click(fn=model_inference, inputs=text_input, outputs=[text_output, json_out])
    btn1.click(fn=clear_all, inputs=None, outputs=[text_input, text_output, json_out])
    gr.Button.style(1)



# define what will run when the button is clicked, here the textbox is used as both an input and an output
#btn.click(fn=complete_with_gpt, inputs=textbox, outputs=textbox, queue=False)

demo.launch()
