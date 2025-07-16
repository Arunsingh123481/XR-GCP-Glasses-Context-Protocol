class NCPInference:
    def predict_cognitive_state(self, context_data):
        noise = context_data.get("environmental", {}).get("noise_level", "")
        people = context_data.get("social", {}).get("people_nearby", 0)

        if noise == "high" and people > 3:
            return {"intent": "distracted", "mental_load": "high", "mood": "anxious"}
        elif noise == "quiet" and people == 0:
            return {"intent": "focus", "mental_load": "low", "mood": "calm"}
        else:
            return {"intent": "neutral", "mental_load": "medium", "mood": "normal"}
