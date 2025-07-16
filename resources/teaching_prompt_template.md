# Master Teaching Prompt Template

Use this whenever you want the AI to teach you a new data-structure, algorithm, or coding problem. Replace the **Topic / Problem** placeholder before sending.

---
```
IMPORTANT: Create two separate files:
1. A clean .py file in the appropriate week folder with minimal comments and comprehensive test cases in main
2. A detailed .md file in resources/notes/ following the full teaching structure below
Also update all relevant tracking files (progress_board.md, schedule.md, daily logs, etc.)

I'm learning data structures & algorithms from scratch and my background is not CS, so please explain things slowly and concretely.

Topic / Problem:
    <put the exact concept or LeetCode/NeetCode problem name + link here>

My current level:
    • I understand the basic idea of variables, loops, and functions in Python.
    • I'm NOT yet comfortable with formal proofs, asymptotic math, or complex jargon.

What I need from you:
1. Intuitive overview – A plain-English analogy first (no code).
2. Step-by-step explanation – Build from the simplest idea to the full algorithm for the optimal solution.
3. Visual or mental model – Describe how I can picture the optimal solution (e.g., boxes, arrows).
4. Code (Optimal Solution) – Show a clean Python implementation with inline comments.
5. Complexity (Optimal Solution) – Explain time & space in words before giving the Big-O symbols.
6. Alternative Solutions & Trade-offs – Describe other common solutions (e.g., brute-force). For each:
    a. Explain the approach.
    b. Show the code and analyze its complexity (Time and Space).
    c. Discuss the trade-offs (e.g., "simpler but slower").
7. Python Implementation Details – Explain which built-in Python features (e.g., classes, functions, modules) are used to implement the core data structure or algorithm. Mention any common alternative implementations available in Python's standard library.
8. Edge cases – List and clarify at least three tricky inputs and how the algorithm handles them.
9. Tiny quiz – Ask me 3–4 quick questions so I can test if I understood (but don't reveal answers until I try).

Teaching style:
    • Assume zero prior knowledge beyond loops and if-statements.
    • Avoid or define any jargon immediately when it appears.
    • Use bullet points and short paragraphs, not walls of text.
    • Feel free to add ASCII diagrams if helpful.

CRITICAL for non-CS background - Always explain these concepts when they appear:
    • ASCII/Unicode values and ord() function - what they are and why we use them
    • Dictionary keys and why some types work as keys (immutable) vs others don't (mutable)
    • defaultdict vs regular dict - when and why to use each
    • Tuple vs list differences and when to use each
    • Index calculations like ord(char) - ord('a') - step by step with examples
    • Memory concepts like "fixed alphabet" vs "variable length"
    • Any built-in Python functions (sorted, join, etc.) - what they do and return
    • Data structure trade-offs in plain English (not just Big-O)
    • Why certain approaches work (mathematical/logical reasoning)
    • Common CS patterns like "signature-based grouping" - explain the concept first

Please follow this structure every time I ask about a new concept.
```

---
**Revision workflow:** When you ask "update the prompt," we'll tweak, extend, or clarify this template and overwrite the file so you always have the latest version.