from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = 'gpt2'
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

def suggest_phrases(prompt, max_length=50, num_suggestions=5):
    inputs = tokenizer(prompt, return_tensors='pt')
    if num_suggestions > 1:
        # Use beam search to get multiple suggestions
        outputs = model.generate(
            inputs.input_ids,
            max_length=max_length,
            num_return_sequences=num_suggestions,
            num_beams=num_suggestions,
            early_stopping=True
        )
    else:
        # Use greedy decoding for a single suggestion
        outputs = model.generate(
            inputs.input_ids,
            max_length=max_length,
            num_return_sequences=num_suggestions
        )
    
    suggestions = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
    return suggestions
