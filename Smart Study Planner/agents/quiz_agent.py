# agents/quiz_agent.py

class QuizAgent:
    @staticmethod
    def generate_quizzes(topics):
        templates = [
            ("What is the main focus of {topic}?", "Understanding core principles"),
            ("Which concept is central to {topic}?", "The foundational idea"),
            ("How are elements typically managed in {topic}?", "Using built-in operations"),
            ("What is a key advantage of learning {topic}?", "Improved problem-solving"),
            ("In {topic}, what should you avoid doing?", "Common beginner mistakes"),
            ("What is the correct way to implement {topic}?", "Following best practices"),
            ("Which of the following best describes {topic}?", "An essential programming concept"),
        ]

        distractors_pool = [
            ["Deprecated in modern code", "Only used in interviews", "Rarely needed", "Advanced topic only"],
            ["Causes runtime errors", "Slows down execution", "Not supported anymore", "Memory intensive"],
            ["Optional feature", "Legacy syntax", "Not recommended", "For experts only"],
        ]

        quizzes = {}
        for idx, topic in enumerate(topics):
            q1_template = templates[idx % len(templates)]
            q2_template = templates[(idx + 2) % len(templates)]

            q1 = q1_template[0].format(topic=topic)
            a1 = q1_template[1]
            q2 = q2_template[0].format(topic=topic)
            a2 = "Proper understanding and application"

            dist1 = distractors_pool[idx % len(distractors_pool)]
            dist2 = distractors_pool[(idx + 1) % len(distractors_pool)]

            quizzes[topic] = [
                {
                    "question": f"{q1}?",
                    "options": [
                        f"Option A: {a1}",
                        f"Option B: {dist1[0]}",
                        f"Option C: {dist1[1]}",
                        f"Option D: {dist1[2]}"
                    ],
                    "answer": "Option A"
                },
                {
                    "question": f"{q2}?",
                    "options": [
                        f"Option A: {a2}",
                        f"Option B: {dist2[0]}",
                        f"Option C: {dist2[1]}",
                        f"Option D: {dist2[2]}"
                    ],
                    "answer": "Option A"
                }
            ]
        return quizzes