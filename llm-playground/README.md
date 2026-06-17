# LLM Playground

A CLI tool for testing LLM behavior across sampling parameters.

## What it does
- Streams responses token by token
- Compares outputs at different temperatures
- Supports custom system prompts
- Tracks approximate token usage

## What I learned building this
- Temperature 0.0 is deterministic — identical output every run
- Temperature 0.5+ introduces variance — useful for creative tasks
- Streaming requires flush=True to print tokens as they arrive
- The Groq API is stateless — every call is independent

## Tech stack
- Python, Groq API, Llama 3.1 8B
- python-dotenv for key management

## How to run
```bash
pip install groq python-dotenv
# add GROQ_API_KEY to .env
python llm_playground.py
```

## Architecture decision
Why Groq over OpenAI? Groq's LPU inference chips make it 10x faster for streaming — tokens appear nearly instantly vs 1-2 second delay on standard GPU inference.
