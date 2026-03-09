def get_toc_prompt():
    return escape_braces("""
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

{
  "Exact Title 1": "page_number",
  "Exact Title 2": "page_number",
  "Exact Title 3": "page_number"
}

The output must be a single flat JSON object.
""")

def get_keyword_extraction_prompt():
   return escape_braces("""
You are an intelligent content analyzer whose task is to extract meaningful keywords from a given text. These keywords should represent the main topics and subtopics from a user's perspective, capturing the essence of the content in a way that would be useful for search, retrieval, or recommendation systems.

Follow these instructions:

1. **User-Centric Perspective:** Identify keywords and phrases as if a user is trying to search for, understand, or retrieve this content. Avoid technical jargon unless it is central to the topic.
2. **Hierarchy of Relevance:** Prioritize main topics first, then list subtopics or secondary concepts that are closely related to the main topics.
3. **Concise and Informative:** Use 1–5 word phrases where possible. Do not include entire sentences.
4. **Distinct Keywords:** Avoid repetition or synonyms unless they add meaningful context.
5. **Contextual Sensitivity:** Extract keywords that are significant within the context of the content, ignoring trivial words or generic terms.
6. **Format:** Return keywords as a structured JSON object with two levels: `main_topics` and `subtopics`. Example:

{
  "main_topics": ["Artificial Intelligence", "Natural Language Processing"],
  "subtopics": ["Machine Learning Models", "Text Classification", "Sentiment Analysis"]
}

Always prioritize clarity and relevance from a human reader's point of view.
""")

def get_summarization_prompt():
    return escape_braces("""
You are an intelligent summarization engine. Your task is to create a very short and clear summary of the provided text while preserving the original meaning and context.

Instructions:
1. Extract the core concepts, main ideas, and key points.
2. Keep the summary **brief and to the point**; do not make it long.
3. Use clear and simple language; maintain logical flow.
4. Do not add new information or change the original meaning.

Output Format (strict JSON):

{
  "summary": "<very short summary of the text>",
  "main_ideas": ["<main idea 1>", "<main idea 2>", "..."],
  "key_points": ["<key point 1>", "<key point 2>", "..."]
}

- `"summary"`: extremely concise summary of the text.
- `"main_ideas"`: list of the main concepts or themes.
- `"key_points"`: list of the most important facts, arguments, or conclusions.
- Do not include any explanations or formatting outside this JSON.
""")

def escape_braces(text):
    return text.replace("{", "{{").replace("}", "}}")