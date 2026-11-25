# PEAS Analysis: Campus Info Bot

## 1. PEAS Description

| Component | Description for Campus Info Bot |
| :--- | :--- |
| **Performance Measure** | Accurate answers grounded strictly in provided department facts; polite refusal and redirection when information is missing; no hallucinated office hours or locations; clear, concise responses under 3–4 sentences. |
| **Environment** | New students interacting via a command-line terminal, supported by a static local knowledge file (`facts.md`) containing department office locations, hours, and contacts. |
| **Actuators** | Text output displayed in the terminal (cannot register courses, book appointments, send emails, or modify student records). |
| **Sensors** | Typed text messages from the student in the terminal, conversation history in memory, and the contents loaded from `facts.md`. |

## 2. Environment Properties

1. **Partially Observable:** The bot sees the student's typed text and `facts.md`, but cannot observe the student's academic records, registration status, or unstated intent.
2. **Stochastic:** Student queries are unpredictable in phrasing, spelling, and topic, and LLM token sampling introduces slight response variability.
3. **Sequential:** Earlier turns in the conversation provide context (such as pronouns like "they" or "that office") needed to answer follow-up questions accurately.
4. **Static (semidynamic):** While the bot generates a reply during a turn, the underlying `facts.md` and department schedule do not change mid-response.
5. **Discrete:** Interaction occurs in distinct, turn-by-turn text messages rather than continuous real-time sensor streams.
6. **Single-Agent (or Multi-Agent with human user):** From the bot's perspective, there are no competing or cooperating AI agents in the terminal—only the human user providing inputs.