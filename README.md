# agentic-ai-experiment

This repo features an experiment with OpenAI's agentic AI tools, inspired by the recent OpenAI sandbox escape - https://openai.com/index/hugging-face-incident-and-the-road-ahead/

Basic idea for project:
1. Generate a set of functions (or use a set in the standard library)
2. Explore combinatorics of inputs of each function
3. Deduce correct outputs for each input set 
4. Generate test set
5. Run tests


Step 3 requires either code comprehension or NLP on documentation to understand how the function works, e.g. what a search() function returns, to generate a plausible output.
This (input, output) tuple then requires some human-in-the-loop to check for logical coherence.
