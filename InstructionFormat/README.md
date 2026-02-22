# Instruction Format Prompt Style (Llama-2)

Llama-2 uses a specific instruction format for prompts:

**Basic Structure:**
```
[INST] <<SYS>>
{system_message}
<</SYS>>

{user_instruction} [/INST]
{model_response}
```

**Simple Example:**
```
[INST] What is machine learning? [/INST]
Machine learning is a subset of artificial intelligence...
```

**With System Message:**
```
[INST] <<SYS>>
You are a helpful AI assistant.
<</SYS>>

Explain photosynthesis in simple terms. [/INST]
Photosynthesis is the process by which plants convert sunlight into energy...
```

**Key Points:**
- `[INST]` and `[/INST]` wrap user instructions
- `<<SYS>>` and `<</SYS>>` wrap system messages (optional)
- Model response comes after `[/INST]`
- Used by Llama-2 and Llama-3 models
- Clear separation between instructions and responses
