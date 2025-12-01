# agents/planner_agent.py
class PlannerAgent:
    @staticmethod
    def create_schedule(topics):
        schedule = []
        for i, topic in enumerate(topics, 1):
            day = (i - 1) // 2 + 1
            session = "Morning" if i % 2 == 1 else "Afternoon"
            schedule.append({
                "session": i,
                "day": f"Day {day} ({session})",
                "topic": topic
            })
        return schedule