# Overview

This repository demonstrates a simple multi-agent orchestration pattern using the OpenAI Python SDK and Python threads. It is inspired in one of the courses of the Udacity nanodegree in Agentic AI.
Here I use multiple expert AI agents in parallel to analyze a prompt from different perspectives, then combines their outputs into a single summarized response.

The script launches several specialized agents, each assigned a different domain perspective:

- **Policy Agent** — global biopharma policy and personalized medicine regulation
- **Cybersecurity Agent** — biopharma data protection and compliance
- **AI Agent** — AI-driven biopharma data analysis and insights
- **Technology Agent** — biopharma innovation, drug development, and personalized medicine
- **Market Agent** — investment, pricing, and demand trends

After all expert agents respond, a **Summary Agent** synthesizes their outputs into one concise answer.

## Repository Structure

```text
.
├── expert_agents_and_summary.py
```

## How It Works

1. Loads environment variables with `python-dotenv`
2. Initializes an OpenAI client
3. Sends the same user prompt to multiple expert agents in parallel
4. Collects each agent’s response
5. Passes all responses to a summary agent
6. Prints the final combined summary

## Configuration

Create a `.env` file in the project root if you want to manage secrets through environment variables:

```env
OPENAI_API_KEY=your_api_key_here
```

> Note: In the current script, the API key is hardcoded as `"OPENAI_API_KEY"` in the client setup. You may want to replace that with `os.getenv("OPENAI_API_KEY")` for safer configuration.

## Usage

Run the script with (once you obtain your API key):

```bash
python expert_agents_and_summary.py
```

By default, the script uses this prompt:

```text
What are current trends shaping the future of the biopharma industry?
```

To experiment, edit the `user_prompt` variable inside `expert_agents_and_summary.py`.

## Example Workflow

- Each expert agent receives the same user question
- Each agent answers from its own specialty
- The summary agent merges all expert answers into one final response

This pattern can be adapted for:
- market research
- policy analysis
- security reviews
- technical trend synthesis
- multi-perspective decision support

## Notes

This project is a concise example of parallel expert-agent prompting rather than a full production framework. It is best suited for experimentation, demos, and learning about multi-agent summarization workflows.

## License

