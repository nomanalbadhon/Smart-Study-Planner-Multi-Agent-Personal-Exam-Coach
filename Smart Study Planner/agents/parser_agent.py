# agents/parser_agent.py
import re

class ParserAgent:
    def extract_topics(self, raw_text: str) -> list[str]:
        if not raw_text or len(raw_text) < 200:
            return ["Introduction", "Main Concepts", "Advanced Topics"]

        # Normalize text
        text = raw_text
        lines = [line.strip() for line in text.split('\n') if line.strip()]

        candidates = set()

        # Pattern 1: Numbered topics (1., 1.1, 2) etc.
        numbered = re.findall(r'\b(\d+[.\d]*)\s*[\.\)]\s*([A-Z][\w\s&,:;\(\)\-\'\"]+?)(?:\n|$)', text)
        for num, title in numbered:
            clean = re.sub(r'\s+', ' ', title).strip('.:-– ')
            if 15 < len(clean) < 120:
                candidates.add(clean.title())

        # Pattern 2: Bold/Title case lines (common in real PDFs)
        for line in lines:
            if (len(line) > 20 and len(line) < 130 and
                line[0].isupper() and
                sum(1 for c in line if c.isupper()) > 3 and
                not line.endswith(('.', '?', '!', ':'))):
                clean = re.sub(r'^[0-9\.\-\)\s]+', '', line)
                clean = re.sub(r'\s+', ' ', clean).strip('.:-– ')
                if clean and any(c.islower() for c in clean):
                    candidates.add(clean)

        # Pattern 3: Lines that start with "Topic:", "Unit:", "Module:", etc.
        keywords = ['TOPIC', 'UNIT', 'MODULE', 'CHAPTER', 'SECTION', 'WEEK', 'LECTURE']
        for line in lines:
            for kw in keywords:
                if kw in line.upper():
                    match = re.search(rf'{kw}\s*\d*[:\.\-\s]+(.+)', line, re.IGNORECASE)
                    if match:
                        title = match.group(1).strip()
                        if 15 < len(title) < 120:
                            candidates.add(title.title())

        # Pattern 4: ALL CAPS topics (common in syllabi)
        for line in lines:
            if (line.isupper() and 15 < len(line) < 100 and
                not any(word in line for word in ['PAGE', 'SYLLABUS', 'COURSE', 'CODE', 'SEMESTER'])):
                candidates.add(line.strip())

        # Clean up and order by appearance
        final = []
        seen = set()
        for line in lines:
            cleaned = re.sub(r'\s+', ' ', line).strip()
            for cand in list(candidates):
                if cand.lower() in cleaned.lower() and cand not in seen:
                    final.append(cand)
                    seen.add(cand)

        # Add remaining candidates if less than 5
        for cand in candidates:
            if cand not in seen and len(final) < 20:
                final.append(cand)
                seen.add(cand)

        # Final cleanup
        final = [re.sub(r'\s+', ' ', t).strip('.:-– ') for t in final]
        final = [t for t in final if len(t) > 10 and t not in ["Table Of Contents", "References", "Assessment"]]

        # Deduplicate while preserving order
        unique = []
        for t in final:
            if t not in unique:
                unique.append(t)

        return unique[:20] if unique else ["Basic Concepts", "Core Principles", "Advanced Topics", "Applications"]