# fusion/fusion_engine.py
from ncp.ncp_infer import NCPInference

class FusionEngine:
    def __init__(self):
        self.ncp = NCPInference()

    def fuse(self, gcp_context):
        neural_context = self.ncp.predict_cognitive_state(gcp_context)
        gcp_context['neural'] = neural_context
        return gcp_context
