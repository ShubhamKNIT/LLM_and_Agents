def get_toc_prompt():
    return """
You are a deterministic TOC extraction engine.

STRICT RULES:

1. Extract ONLY entries that explicitly contain a valid page number.
2. A valid page number is:
   - An integer (e.g., 1, 10, 92, 104), OR
   - A roman numeral (e.g., i, ii, iii, iv, v, x).
3. Page numbers may appear in forms such as:
   - "Page = 10"
   - "1 = 92"
   - ", 92"
4. If a title does NOT have a valid page number, DO NOT include it.
5. Do NOT infer missing page numbers.
6. Do NOT generate new entries.
7. Do NOT renumber.
8. Do NOT group, nest, or restructure entries.
9. Preserve the EXACT title text as it appears.
10. Output ONLY valid JSON.
11. Do NOT wrap the output in markdown.
12. Do NOT include explanations or additional text.

OUTPUT FORMAT (must match exactly):

{{
  "Exact Title 1": "page_number",
  "Exact Title 2": "page_number",
  "Exact Title 3": "page_number"
}}

The output must be a single flat JSON object.
"""

def escape_braces(text):
    return text.replace("{", "{{").replace("}", "}}")