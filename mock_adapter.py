import random

from adapter_base import ContextAdapter

class MockAdapter(ContextAdapter):
    def get_context(self):
        return {
            "spatial": {
                "room": random.choice(["living_room", "kitchen", "bedroom"]),
                "dimensions": {
                    "width": round(random.uniform(3, 6), 1),
                    "height": 2.5,
                    "depth": round(random.uniform(4, 7), 1)
                },
                "objects": random.sample(["desk", "lamp", "sofa", "TV", "chair"], 3)
            },
            "social": {
                "people_nearby": random.randint(0, 5),
                "interaction_mode": random.choice(["alone", "conversation", "meeting"])
            },
            "environmental": {
                "light_level": random.choice(["low", "medium", "high"]),
                "noise_level": random.choice(["quiet", "low", "high"])
            },
            "user": {
                "gaze_direction": random.choice(["left", "right", "forward"]),
                "activity": random.choice(["working", "relaxing", "moving"])
            }
        }
