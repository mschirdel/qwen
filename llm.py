import gradio as gr
from mlx_lm import load, generate

# Load the model and tokenizer
model, tokenizer = load('mlx/Qwen2.5-7B-Instruct', tokenizer_config={"eos_token": "<|im_end|>"})

def generate_response(message, chatbot):
    messages = [
        {"role": "system", "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."}
    ]
    
    # Convert chatbot history to message format
    for user_msg, assistant_msg in chatbot:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": assistant_msg})
    
    # Add current message
    messages.append({"role": "user", "content": message})
    
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    
    # Add user message to chatbot
    chatbot.append((message, ""))
    
    # Generate and stream the response
    partial_response = ""
    response = generate(model, tokenizer, prompt=text, verbose=True, max_tokens=512)
    for char in response:
        partial_response += char
        chatbot[-1] = (message, partial_response)
        yield "", chatbot

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox(placeholder="Type your message here...")
    clear = gr.Button("Clear")

    msg.submit(generate_response, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: None, None, chatbot, queue=True)

def run():
    demo.queue()
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860
    )

if __name__ == "__main__":
    run()
