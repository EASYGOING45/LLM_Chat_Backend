import gradio as gr
import argparse
from transformers import AutoConfig, AutoModel, AutoTokenizer
import torch
import os

def setup_model(args):
    if args.tokenizer is None:
        args.tokenizer = args.model

    tokenizer = AutoTokenizer.from_pretrained(args.tokenizer, trust_remote_code=True)
    if args.pt_checkpoint:
        config = AutoConfig.from_pretrained(args.model, trust_remote_code=True, pre_seq_len=args.pt_pre_seq_len)
        model = AutoModel.from_pretrained(args.model, config=config, trust_remote_code=True).to(args.device)
        prefix_state_dict = torch.load(os.path.join(args.pt_checkpoint, "pytorch_model.bin"))
        new_prefix_state_dict = {}
        for k, v in prefix_state_dict.items():
            if k.startswith("transformer.prefix_encoder."):
                new_prefix_state_dict[k[len("transformer.prefix_encoder."):]] = v
        model.transformer.prefix_encoder.load_state_dict(new_prefix_state_dict)
    else:
        model = AutoModel.from_pretrained(args.model, trust_remote_code=True).to(args.device)

    return model, tokenizer

def generate_text(prompt, max_length, top_p, temperature, model, tokenizer, args):
    try:
        inputs = tokenizer(prompt, return_tensors="pt")
        inputs = inputs.to(args.device)
        response = model.generate(
            input_ids=inputs["input_ids"],
            max_length=min(max_length, inputs["input_ids"].shape[-1] + args.max_new_tokens),
            top_p=top_p,
            temperature=temperature
        )
        response = response[0, inputs["input_ids"].shape[-1]:]
        return tokenizer.decode(response, skip_special_tokens=True)
    except Exception as e:
        print(f"Error during text generation: {e}")
        return ""

def predict(user_input, chatbot, max_length, top_p, temperature, history, past_key_values):
    response = generate_text(user_input, max_length, top_p, temperature, model, tokenizer, args)
    
    processed_user_input = parse_text(user_input)
    processed_response = parse_text(response)

    history.append((processed_user_input, processed_response))
    return history, history, past_key_values

def parse_text(text):

    return text

def reset_user_input():
    return ""

def reset_state():
    return [], [], None

# 参数
args = argparse.Namespace(
    pt_checkpoint="微调模型的绝对路径",
    model="/root/autodl-tmp/chatglm3-6b",
    tokenizer=None,
    pt_pre_seq_len=128,
    device="cuda" if torch.cuda.is_available() else "cpu",
    max_new_tokens=128
)

model, tokenizer = setup_model(args)

#  Gradio 界面
with gr.Blocks() as demo:
    gr.HTML("""<h1 align="center">ChatGLM3-6B</h1>""")

    chatbot = gr.Chatbot()
    with gr.Row():
        with gr.Column(scale=4):
            with gr.Column(scale=12):
                user_input = gr.Textbox(show_label=False, placeholder="Input...", lines=10).style(container=False)
            with gr.Column(min_width=32, scale=1):
                submitBtn = gr.Button("Submit", variant="primary")
        with gr.Column(scale=1):
            emptyBtn = gr.Button("Clear History")
            max_length = gr.Slider(0, 32768, value=8192, step=1.0, label="Maximum length", interactive=True)
            top_p = gr.Slider(0, 1, value=0.8, step=0.01, label="Top P", interactive=True)
            temperature = gr.Slider(0, 1, value=0.6, step=0.01, label="Temperature", interactive=True)
            
    history = gr.State([])
    past_key_values = gr.State(None)

    submitBtn.click(predict, [user_input, chatbot, max_length, top_p, temperature, history, past_key_values],
                    [chatbot, history, past_key_values], show_progress=True)
    submitBtn.click(reset_user_input, [], [user_input])

    emptyBtn.click(reset_state, outputs=[chatbot, history, past_key_values], show_progress=True)

demo.queue().launch(share=True, server_name="127.0.0.1", server_port=6006, inbrowser=True)