# Diagnostic Answers

## Question 1: What is the difference between a simple reflex agent and a goal-based agent?

**Simple Reflex Agent**  
- Acts only on the current percept.  
- Uses a set of condition‑action rules (or a mapping from percepts to actions).  
- No internal state or memory of past percepts.  
- No notion of future consequences or goals; it just reacts.

**Goal‑Based Agent**  
- Also reacts to percepts, but its behavior is guided by a *goal* (desired state).  
- Maintains an internal state or model of the world.  
- Evaluates actions based on how they move the agent toward the goal (often using search or planning).  
- Can consider future consequences and choose actions that lead to the goal, not just immediate reactions.

In short: a simple reflex agent only reacts to the present; a goal‑based agent plans to reach a desired future state.

*Tokens used: 322*

## Question 2: Why is a chatbot's environment considered partially observable even though it sees every message the user types?

Because “seeing every message” only gives the chatbot a *subset* of the true state of the world.  
In a conversational setting the relevant state includes:

* **The user’s internal state** – goals, preferences, emotions, prior knowledge, and intentions that are never directly observable.  
* **External context** – facts about the user’s environment, recent events, or other agents that influence the conversation.  
* **Ambiguity and incompleteness** – a user’s utterance may be vague, sarcastic, or deliberately misleading, so the chatbot cannot infer the exact meaning without additional information.  
* **History limits** – practical systems truncate or compress the dialogue history, so earlier turns that could disambiguate current intent may be lost.

Thus, although the chatbot receives every typed message, it still lacks full knowledge of all variables that determine the next best action. This is the hallmark of a **partially observable** environment.

*Tokens used: 493*

## Question 3: What role does the system prompt play in turning a large language model into an intelligent agent?

The system prompt is the *instruction set* that turns a vanilla LLM into an agent.  
It:

1. **Defines the agent’s role and goals** – e.g., “You are a helpful assistant that plans and executes tasks.”  
2. **Imposes constraints and safety policies** – e.g., “Never reveal personal data; follow the privacy policy.”  
3. **Specifies tool‑use and workflow** – e.g., “Use the search tool before answering; log each step.”  
4. **Sets up context handling** – e.g., “Maintain a short‑term memory buffer of the last 5 turns.”  

By embedding these directives in the system prompt, the model is guided to behave consistently, reason, plan, and interact as an autonomous intelligent agent rather than just generating text.

*Tokens used: 469*


---
**Total Tokens Used Across All Questions:** 1284
