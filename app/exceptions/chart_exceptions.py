class ChartError(Exception):
    """Custom exception class for chart errors."""
    def __init__(self, message="Chart Exception"):
        super().__init__(message)