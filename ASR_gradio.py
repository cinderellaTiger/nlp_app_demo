import gradio as gr
import os


def inference():
    # os.system("paddlespeech tts --input '" + text + "' --output output.wav")
    return "output.wav"



def clear_all():
    return None,None,None,None


with gr.Blocks() as demo:
    gr.Markdown("ASR")

    with gr.Column(scale=1, min_width=100):
        audio_input = gr.Audio(type="file", label=" Input From File")
        inputs = gr.inputs.Audio(source="microphone", type='filepath',label="Input From Mic")



        with gr.Row():
            btn1 = gr.Button("Clear")
            btn2 = gr.Button("Submit")


        text_output = gr.Textbox(placeholder="Result...", lines=10)
        # text_input = gr.Textbox(placeholder="Type here...", lines=4)

        default01= ["china", "jiuuh"]


        json_out = gr.JSON(label="jsonOutput")

    btn2.click(fn=inference, inputs = [audio_input,inputs], outputs= None , scroll_to_output= True)
    btn1.click(fn=clear_all, inputs=None, outputs=[inputs,text_output,audio_input, json_out])

    # btn1.click(fn=clear_all, inputs=None, outputs=[text_output, audio_input, json_out])
    # btn2.click(fn=inference, inputs=audio_input, outputs=None, scroll_to_output=True)

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




