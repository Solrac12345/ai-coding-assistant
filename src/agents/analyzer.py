from src.logging.logger import Logger
from src.state.state import State


class AnalyzerAgent:
    """Analyzes input code and populates state.analysis."""

    def run(self, state: State) -> State:
        Logger.info("Analyzing code", agent="AnalyzerAgent")
        # analysis logic...
        return state
