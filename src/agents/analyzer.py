from src.state.state import State
from src.logging.logger import Logger


class AnalyzerAgent:
    """Analyzes input code and populates state.analysis."""

    def run(self, state: State) -> State:
        Logger.info("Analyzing code", agent="AnalyzerAgent")
        # analysis logic...
        return state
