from transformers import GPT2LMHeadModel, GPT2Tokenizer

MODEL_NAME = 'gpt2'
MAX_LENGTH = 50
NUM_SUGGESTIONS = 3

tokenizer = GPT2Tokenizer.from_pretrained(MODEL_NAME)
model = GPT2LMHeadModel.from_pretrained(MODEL_NAME)

def suggest_phrases(prompt, num_suggestions=NUM_SUGGESTIONS):
    input_text = tokenizer(prompt, return_tensors='pt')
    
    outputs = model.generate(
        input_text.input_ids,
        max_length=MAX_LENGTH,
        num_return_sequences=num_suggestions,
        num_beams=5,
        temperature=0.7,  
        top_k=50,         
        top_p=0.95,       
        early_stopping=True,
        pad_token_id=tokenizer.eos_token_id
    )
    
    suggestions = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
    return suggestions
