# run_demo.py
import os
from pathlib import Path
from tools.pdf_tool import PDFTool
from agents.parser_agent import ParserAgent
from agents.planner_agent import PlannerAgent
from agents.quiz_agent import QuizAgent

def main():
    print("Syllabus → Study Schedule & Quiz Generator")
    print("=" * 56)

    # === AUTOMATIC PDF DETECTION ===
    sample_dir = Path("sample_data")
    pdf_files = list(sample_dir.glob("*.pdf")) if sample_dir.exists() else []

    if pdf_files:
        # Use the FIRST PDF found in sample_data/
        pdf_path = pdf_files[0]
        print(f"Found your uploaded PDF: {pdf_path.name}")
    else:
        # No PDF → use built-in demo
        pdf_path = None
        print("No PDF in sample_data/ → using built-in demo syllabus")

    print("Loading PDF...", end=" ")
    raw_text = PDFTool.read_pdf(str(pdf_path) if pdf_path else None)
    print("Done!\n")

    # Rest unchanged
    print("Extracting topics from your syllabus...")
    parser = ParserAgent()
    topics = parser.extract_topics(raw_text)

    print(f"\nFound {len(topics)} topics:\n")
    for i, t in enumerate(topics, 1):
        print(f"  {i:2d}. {t}")
    print("\n" + "—" * 60)

    print("Creating your personalized study schedule...")
    planner = PlannerAgent()
    schedule = planner.create_schedule(topics)

    print("\nYOUR STUDY SCHEDULE")
    print("—" * 60)
    for item in schedule:
        print(f"{item['day']:<18} | Session {item['session']:2d} | {item['topic']}")
    print()

    print("Generating 2 MCQs per topic...")
    quiz_agent = QuizAgent()
    quizzes = quiz_agent.generate_quizzes(topics)

    print("YOUR GENERATED QUIZZES")
    print("=" * 70)
    for topic in topics:
        print(f"Topic: – {topic}")
        for i, q in enumerate(quizzes[topic], 1):
            print(f" Q{i}: {q['question']}")
            for opt in q['options']:
                print(f"    - {opt}")
            print(f" Answer: {q['answer']}")
        print()
    print("All done! Happy studying!")

if __name__ == "__main__":
    main()