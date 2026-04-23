from datetime import UTC, datetime
from typing import Any

from src.logging.logger import Logger
from src.state.state import State


class Supervisor:
    """Orchestrates the execution of all agents with advanced error handling."""

    def __init__(self, agents: list[Any]) -> None:
        self.agents = agents

    def _record_failure(self, state: State, agent_name: str, exc: Exception) -> None:
        """Store structured error metadata."""
        failure = {
            "agent": agent_name,
            "error": f"{type(exc).__name__}: {exc}",
            # Fixed: datetime.utcnow() is deprecated; use timezone-aware version
            "timestamp": datetime.now(UTC).isoformat(),
        }
        state.metadata.setdefault("agent_failures", []).append(failure)

    def _apply_fallback(self, state: State, agent_name: str) -> State:
        """Graceful fallback logic for each agent."""
        Logger.warning(f"Applying fallback for {agent_name}", agent="Supervisor")

        match agent_name:
            case "AnalyzerAgent":
                state.analysis = "Analysis unavailable due to internal error."

            case "OptimizerAgent":
                state.optimized_code = state.code  # return original code

            case "DocAgent":
                state.documentation = "Documentation unavailable due to internal error."

        return state

    def run(self, state: State) -> State:
        Logger.info("Supervisor started pipeline", agent="Supervisor")

        for agent in self.agents:
            agent_name = agent.__class__.__name__
            Logger.info(f"Starting {agent_name}", agent=agent_name)

            try:
                state = agent.run(state)
                Logger.info(f"Completed {agent_name}", agent=agent_name)

            except Exception as exc:  # noqa: BLE001
                error_msg = f"{agent_name} failed: {exc}"
                Logger.error(error_msg, agent=agent_name)

                # Record structured metadata
                self._record_failure(state, agent_name, exc)

                # Add to state.errors
                state.errors.append(error_msg)

                # Apply fallback logic
                state = self._apply_fallback(state, agent_name)

                Logger.info(
                    f"Recovered from {agent_name} failure using fallback",
                    agent="Supervisor",
                )

        Logger.info("Supervisor finished pipeline", agent="Supervisor")
        return state
