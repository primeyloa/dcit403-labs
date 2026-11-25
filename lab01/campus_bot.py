import os
from pathlib import Path
from dotenv import load_dotenv
from litellm import completion

load_dotenv()
MODEL = os.getenv("LLM_MODEL")

def load_facts() -> str:
    facts_path = Path(__file__).parent / "facts.md"
    return facts_path.read_text(encoding="utf-8")

def build_system_prompt(facts: str) -> str:
    return f"""You are the Campus Info Bot for the Department of Computer Science.

PERFORMANCE RULES (How your success is judged):
- Answer student questions accurately using ONLY the Department Facts provided below.
- Keep replies concise, polite, and helpful (2 to 4 sentences max).
- If a question is not covered by the facts below, do NOT guess or invent details. Say you do not have that information and direct the student to visit the Department General Office (Room 101) or email cs-office@ug.edu.gh.

ACTUATOR LIMITS (What you can and cannot do):
- You can ONLY provide text answers.
- You CANNOT register students for courses, book appointments, check grades, or modify any records. If asked to perform an action, clearly explain that you are an information-only assistant and tell them which office to visit.

DEPARTMENT FACTS:
{facts}
"""

def main():
    if not MODEL:
        print("Error: LLM_MODEL is not set in your .env file.")
        return

    facts = load_facts()
    messages = [{"role": "system", "content": build_system_prompt(facts)}]

    print("Campus Info Bot ready! Ask about offices, hours, or contacts. Type 'quit' to exit.\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue
        if user_input.lower() == "quit":
            print("Bot: Goodbye! Have a great day on campus.")
            break

        messages.append({"role": "user", "content": user_input})

        resp = completion(
            model=MODEL,
            messages=messages,
            temperature=0,
        )
        reply = resp.choices[0].message.content.strip()
        messages.append({"role": "assistant", "content": reply})

        print(f"Bot: {reply}\n")

if __name__ == "__main__":
    main()