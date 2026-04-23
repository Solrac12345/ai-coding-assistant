from src.logging.logger import Logger
from src.state.state import State


class Supervisor:
    """Orchestrates the execution of all agents with logging and error handling."""

    def __init__(self, agents: list[object]) -> None:
        self.agents = agents

    def run(self, state: State) -> State:
        Logger.info("Supervisor started pipeline", agent="Supervisor")

        for agent in self.agents:
            agent_name = agent.__class__.__name__
            Logger.info(f"Starting {agent_name}", agent=agent_name)

            try:
                state = agent.run(state)
                Logger.info(f"Completed {agent_name}", agent=agent_name)

            except Exception as exc:
                error_msg = f"{agent_name} failed: {exc}"
                Logger.error(error_msg, agent=agent_name)
                state.errors.append(error_msg)

        Logger.info("Supervisor finished pipeline", agent="Supervisor")
        return state
