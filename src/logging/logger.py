import json
from datetime import UTC, datetime


class Logger:
    """Structured JSON logger for consistent, machine-readable logs."""

    @staticmethod
    def _log(level: str, message: str, agent: str | None = None) -> None:
        entry = {
            # Modern approach: datetime.utcnow() is deprecated
            "timestamp": datetime.now(UTC).isoformat(),
            "level": level,
            "agent": agent or "system",
            "message": message,
        }
        print(json.dumps(entry))

    @staticmethod
    def info(message: str, agent: str | None = None) -> None:
        Logger._log("INFO", message, agent)

    @staticmethod
    def warning(message: str, agent: str | None = None) -> None:
        Logger._log("WARNING", message, agent)

    @staticmethod
    def error(message: str, agent: str | None = None) -> None:
        Logger._log("ERROR", message, agent)

    @staticmethod
    def debug(message: str, agent: str | None = None) -> None:
        Logger._log("DEBUG", message, agent)
