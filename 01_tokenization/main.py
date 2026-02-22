import tiktoken

enc = tiktoken.encoding_for_model("gpt-3.5-turbo")
text = "Hello, how are you doing today?"
tokens = enc.encode(text)
print(tokens)
dec = enc.decode(tokens)
print(dec)
# Output:[15496, 11, 703, 389, 345, 338