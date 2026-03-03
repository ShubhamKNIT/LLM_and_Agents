def get_toc_prompt():
    return """
You are a deterministic TOC extraction engine.

STRICT RULES:

1. Extract only titles that have an EXPLICIT numeric page number next to them.
2. A valid page number is a number (e.g., 1, 10, 92, 104) or roman numeral (i, ii, iii).
3. The page number may appear in any of these forms:
   - "Page = 10"
   - "1 = 92"
   - ", 92"
4. If a title does NOT have a valid numeric page number, DO NOT include it.
5. Do NOT infer missing page numbers.
6. Do NOT generate new chapters.
7. Do NOT renumber.
8. Do NOT restructure the content.
9. Output ONLY raw JSON.
10. Do NOT wrap output in markdown.

Output format:
{{
  "Exact Title": page_number
}}
"""

def escape_braces(text):
    return text.replace("{", "{{").replace("}", "}}")