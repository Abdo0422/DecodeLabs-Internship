# Brainstorming: Project 1 - Rule-Based AI Chatbot 

### **What is this?**

This is the foundation phase of my **Artificial Intelligence Engineer** role at **DecodeLabs**. Instead of "learning" on its own, this chatbot uses a **Logic Engine** to follow my exact instructions.

---

**The Plan (IPO Model)** 

#### 1. Input (The Data Inflow) 
 
**Goal:** Get text from the user.

**The Problem:** People type differently (e.g., "HELLO", " hello ", "Hello").

* 
**The Fix (Sanitization):** Use `.lower()` and `.strip()` to make the input "clean".



#### 2. Process (The Logic Skeleton) 
 
**Goal:** Match the user's intent to a response.

**The Tool:** Use **if-else logic** (Deterministic Guardrails).


* **The Rules:**
* Recognize **Greetings** (Hi/Hello).


* Recognize **Exit Commands** (Bye/Exit) to stop the program.


* Provide a **Fallback** for unknown words to ensure "Traceability" (no guessing).





#### 3. Output (The Feedback Loop) 

**Goal:** Print the answer and keep the conversation going.

**The Tool:** A `while` loop to create a continuous digital interaction.



---

### **Why am I doing this?**

* 
**Safety:** It has zero "hallucination" risk because it is 100% hard-coded.


* 
**Control:** This "White Box" architecture is essential for sensitive fields like Finance or Healthcare.


* 
**Foundation:** This logic layer acts as a "Guardrail" for modern AI models.



---

### **Task Checklist**

* [ ] Set up a `while` loop.


* [ ] Clean user input with `.lower()` and `.strip()`.


* [ ] Write `if-else` rules for "hello" and "exit".


* [ ] Verify the quality to **Earn My Badge**.