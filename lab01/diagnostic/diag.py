import os
from pathlib import Path
from dotenv import load_dotenv
from litellm import completion

load_dotenv()
MODEL = os.getenv("LLM_MODEL")

def main():
    if not MODEL:
        print("Error: LLM_MODEL environment variable is not set. Check your .env file.")
        return

    base_dir = Path(__file__).parent
    questions_file = base_dir / "questions.txt"
    answers_file = base_dir / "answers.md"

    if not questions_file.exists():
        print(f"Error: {questions_file} not found.")
        return

    questions = [line.strip() for line in questions_file.read_text(encoding="utf-8").splitlines() if line.strip()]
    total_tokens = 0
    output_lines = ["# Diagnostic Answers\n"]

    for idx, q in enumerate(questions, start=1):
        resp = completion(
            model=MODEL,
            messages=[
                {"role": "system", "content": "Answer clearly and concisely."},
                {"role": "user", "content": q},
            ],
            temperature=0,
        )
        ans = resp.choices[0].message.content.strip()
        tokens = resp.usage.total_tokens if resp.usage else 0
        total_tokens += tokens

        output_lines.append(f"## Question {idx}: {q}\n")
        output_lines.append(f"{ans}\n")
        output_lines.append(f"*Tokens used: {tokens}*\n")

    output_lines.append(f"\n---\n**Total Tokens Used Across All Questions:** {total_tokens}\n")
    answers_file.write_text("\n".join(output_lines), encoding="utf-8")
    print(f"Done! Wrote answers to {answers_file} (Total tokens: {total_tokens}).")

if __name__ == "__main__":
    main()