# llama-cli.exe
To use `llama-cli.exe` to load a LLaMA model for chat, follow these steps:

### 1. **Ensure Model is Quantized**:
Before you start, ensure that the LLaMA model is quantized. If it isn’t, you can use `llama-quantize.exe` to do so, as described earlier.

### 2. **Run the Command**:
The basic syntax for `llama-cli.exe` is as follows:

```bash
.\llama-cli.exe --model models\7B\ggml-model-q3.gguf --prompt "Your prompt here"
```

This command will load the model and respond based on the provided prompt.

### 3. **Interactive Chat Mode**:
To enable an interactive chat mode where you can continue a conversation, use the `--interactive` flag. The command would look like this:

```bash
.\llama-cli.exe --model models\7B\ggml-model-q3.gguf --interactive
```

This will start a chat session where you can continuously send prompts and get responses from the model.

### 4. **Example Command**:
Assuming your model is located at `models/llama-7b-quantized.gguf` and you want to start an interactive session, the command would be:

```bash
llama-cli.exe --model models/llama-7b-quantized.gguf --interactive
```

### 5. **Add Options for Threads**:
Since you have a system with 6 cores and 12 threads, you can specify the number of threads to optimize performance. Use the `--threads` option to make sure you’re utilizing your CPU fully:

```bash
llama-cli.exe --model models/llama-7b-quantized.gguf --interactive --threads 12
```

This will ensure that the model uses all available threads for faster inference.

### 6. **Additional Options**:
- **Memory setting**: You can use the `--memory` option if you want to allocate a specific amount of memory.
- **Temperature & top-k**: You can control the randomness and diversity of the responses by using `--temperature` and `--top-k` flags, for example:
  ```bash
  llama-cli.exe --model models/llama-7b-quantized.gguf --interactive --threads 12 --temperature 0.8 --top-k 50
  ```

This should set up your chat model properly with `llama-cli.exe`.