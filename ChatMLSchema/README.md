# ChatML Prompting Style

ChatML uses special tokens to structure conversations:

**Tokens:**
- `<|im_start|>` - Start of message
- `<|im_end|>` - End of message
- `system` - System instructions
- `user` - User message  
- `assistant` - AI response

**Basic Format:**
```
<|im_start|>system
You are a helpful assistant.
<|im_end|>
<|im_start|>user
Hello!
<|im_end|>
<|im_start|>assistant
Hi there! How can I help you?
<|im_end|>
```

**Key Points:**
- Each message wrapped in start/end tokens
- Role specified after start token
- Maintains conversation context
- Works well with OpenAI-compatible APIs
