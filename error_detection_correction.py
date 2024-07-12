import language_tool_python

def grammarChecker(text):
    tool = language_tool_python.LanguageTool('en-US')
    result = tool.check(text)
    return result

def check_errors(text):
    errors = []
    grammar_errors = grammarChecker(text)
    for error in grammar_errors:
        error_detail = (
            f"Error: {error.message}"
            f"Context: {error.context}"
            f"Position: {error.offsetInContext}"
            f"Suggestions: {' , '.join(error.replacements)}"
        )
        errors.append(error_detail)
    return {"text": text, "corrections": errors}
