document.getElementById('completeText').addEventListener('click', async () => {
    const prompt = document.getElementById('inputText').value;
    const response = await fetch('/complete', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt })
    });
    const data = await response.json();
    document.getElementById('output').innerText = data.text;
});

document.getElementById('suggestPhrases').addEventListener('click', async () => {
    const prompt = document.getElementById('inputText').value;
    const response = await fetch('/suggest', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt })
    });
    const data = await response.json();
    document.getElementById('output').innerText = data.suggestions.join('\n');
});

document.getElementById('checkErrors').addEventListener('click', async () => {
    const text = document.getElementById('inputText').value;
    const response = await fetch('/check', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text })
    });
    const data = await response.json();
    document.getElementById('output').innerText = JSON.stringify(data.corrections);
});

document.getElementById('summarizeText').addEventListener('click', async () => {
    const text = document.getElementById('inputText').value;
    const response = await fetch('/summarize', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text })
    });
    const data = await response.json();
    document.getElementById('output').innerText = data.summary;
});
