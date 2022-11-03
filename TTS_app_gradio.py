import gradio as gr
import os


def inference():
    # os.system("paddlespeech tts --input '" + text + "' --output output.wav")
    return "output.wav"



def clear_all():
    return None,None,None



with gr.Blocks() as demo:
    gr.Markdown("Text to Speech")

    with gr.Column(scale=1, min_width=100):
        text_input = gr.Textbox(placeholder="Type here...", lines=10)


        with gr.Row():
            btn1 = gr.Button("Clear")
            btn2 = gr.Button("Submit")

        audio_output = gr.Audio(type="file", label="Output")

        # text_input = gr.Textbox(placeholder="Type here...", lines=4)

        default01= ["china", "jiuuh"]

        # img_out = gr.Image(shape=(200, 200), label="输出图片").style(height=200)
        json_out = gr.JSON(label="jsonOutput")

    btn2.click(fn=inference, inputs = text_input, outputs= None , scroll_to_output= True)
    btn1.click(fn=clear_all, inputs=None, outputs=[text_input,audio_output, json_out])#清除

    # btn1.click(fn=clear_all, inputs=None, outputs=audio_input)

    gr.Button.style(1)

# demo.launch()
# gr.Interface(
#     inference,
#     gr.inputs.Textbox(label="input text", lines=10),
#     gr.outputs.Audio(type="file", label="Output"),
#     title=title,
#     description=description,
#     article=article,
#     enable_queue=True,
#     examples=examples
# ).launch(debug=True)
demo.launch()



