Find every bug in the given Python file. Read each function's docstring and check every line carefully—especially comparison operators (`<`, `>`, `<=`, `>=`, `==`), boundary/limit conditions, arithmetic operations, edge-case inputs (empty lists, empty strings, zero), and security issues.

For each bug you find, output a report using this exact plain-text format:

Line: 12
Problem: is_adult returns False for someone who is exactly 18, but the docstring says "18 or older".
Example: is_adult(18) returns False, expected True.
Fix: return age >= 18

Strict formatting rules:
- Start each field at the beginning of a new line with exact prefixes: `Line: `, `Problem: `, `Example: `, `Fix: `.
- `Line:` must contain only a single integer (never a range like `12-14`).
- Do NOT use bold (`**`), bullet points (`-` or `*`), headings (`#`), or code fences (```).
- Separate multiple bug reports with a single blank line and write nothing else.
