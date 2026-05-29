import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

import threading
import traceback

# Load environment variables and initialize OpenAI client
load_dotenv()

# Choose client based on BASE_URL
client = OpenAI(
    base_url="https://openai.vocareum.com/v1",
    # Uncomment one of the following
    api_key="OPENAI_API_KEY"
)

# Shared dict for thread-safe collection
agent_outputs = {}

# The shared user prompt
user_prompt = "What are current trends shaping the future of the biopharma industry?"
print(f"Using parallel agents to answer prompt: {user_prompt}")

# Agent classes using the new OpenAI v1+ SDK
class PolicyAgent:
    def run(self, prompt):
        print(f"Policy Agent resolving prompt: {prompt}")
        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a policy expert in global biopharma policy and personalized medicine regulations."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            agent_outputs["policy"] = response.choices[0].message.content
        except Exception as e:
            print("Policy Agent error:", e)
            agent_outputs["policy"] = f"[error: {e}]"

class CybersecAgent:
    def run(self, prompt):
        print(f"Cybersec Agent resolving prompt: {prompt}")
        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a cybersecurity expert specializing in biopharma data protection and compliance."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            agent_outputs["cybersec"] = response.choices[0].message.content
        except Exception as e:
            print("Cybersec Agent error:", e)
            agent_outputs["cybersec"] = f"[error: {e}]"

class AIAgent:
    def run(self, prompt):
        print(f"AI Agent resolving prompt: {prompt}")
        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an AI expert specializing in biopharma data analysis and insights."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            agent_outputs["ai"] = response.choices[0].message.content
        except Exception as e:
            print("AI Agent error:", e)
            agent_outputs["ai"] = f"[error: {e}]"

class TechnologyAgent:
    def run(self, prompt):
        print(f"Technology Agent resolving prompt: {prompt}")
        try:
            response = client.chat.completions.create(
                model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert in biopharma innovations, drug development, and personalized medicine."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
            agent_outputs["tech"] = response.choices[0].message.content
        except Exception as e:
            print("Technology Agent error:", e)
            agent_outputs["tech"] = f"[error: {e}]"

class MarketAgent:
    def run(self, prompt):
        print(f"Market Agent resolving prompt: {prompt}")
        try:
            response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a biopharma market analyst focused on global investment, pricing, and demand trends."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
            agent_outputs["market"] = response.choices[0].message.content
        except Exception as e:
            print("Market Agent error:", e)
            agent_outputs["market"] = f"[error: {e}]"

class SummaryAgent:
    def run(self, prompt, inputs):
        combined_prompt = (
            f"The user asked: '{prompt}'\n\n"
            f"Here are the expert responses:\n"
            f"- Policy Expert: {inputs['policy']}\n\n"
            f"- Technology Expert: {inputs['tech']}\n\n"
            f"- Market Expert: {inputs['market']}\n\n"
            f"- Cybersecurity Expert: {inputs['cybersec']}\n\n"
            f"- AI Expert: {inputs['ai']}\n\n"
            "Please summarize the combined insights into a single clear and concise response."
        )
        print(f"Summary Agent resolving prompt: {combined_prompt}")

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a biopharma strategist skilled at synthesizing expert insights."},
                {"role": "user", "content": combined_prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content

# Run the agents
def main():
    policy_agent = PolicyAgent()
    tech_agent = TechnologyAgent()
    cybersec_agent = CybersecAgent()
    market_agent = MarketAgent()
    ai_agent = AIAgent()
    summary_agent = SummaryAgent()

    threads = [
        threading.Thread(target=policy_agent.run, args=(user_prompt,)),
        threading.Thread(target=cybersec_agent.run, args=(user_prompt,)),
        threading.Thread(target=ai_agent.run, args=(user_prompt,)),
        threading.Thread(target=tech_agent.run, args=(user_prompt,)),
        threading.Thread(target=market_agent.run, args=(user_prompt,))
    ]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    final_summary = summary_agent.run(user_prompt, agent_outputs)

    print("\n=== FINAL SUMMARY ===\n")
    print(final_summary)

if __name__ == "__main__":
    main()
