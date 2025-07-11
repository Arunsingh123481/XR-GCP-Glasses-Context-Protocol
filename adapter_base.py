class ContextAdapter:
    def get_context(self):
        """
        Return data in XR GCP context format.
        Override this in concrete adapters.
        """
        raise NotImplementedError
