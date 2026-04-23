import re
from typing import Final

from src.logging.logger import Logger
from src.state.state import State

# === Strict limits ===
MAX_CODE_LENGTH: Final[int] = 10_000  # Maximum characters allowed
MAX_LINE_COUNT: Final[int] = 300  # Maximum number of lines
MAX_AVG_LINE_LENGTH: Final[int] = 300  # Heuristic for extremely long lines


# === Dangerous patterns (strict mode) ===
DANGEROUS_PATTERNS: Final[list[re.Pattern[str]]] = [
    re.compile(r"\beval\s*\(", re.IGNORECASE),
    re.compile(r"\bexec\s*\(", re.IGNORECASE),
    re.compile(r"\bcompile\s*\(", re.IGNORECASE),
    re.compile(r"\bos\.system\s*\(", re.IGNORECASE),
    re.compile(r"\bsubprocess\.", re.IGNORECASE),
    re.compile(r"\bopen\s*\(", re.IGNORECASE),
    re.compile(r"\bimport\s+os\b", re.IGNORECASE),
    re.compile(r"\bimport\s+subprocess\b", re.IGNORECASE),
    re.compile(r"while\s+True\s*:", re.IGNORECASE),  # infinite loop heuristic
]


def sanitize_input(code: str) -> str:
    """Normalize and sanitize raw user input."""
    sanitized = code.replace("\x00", "")  # remove null bytes
    sanitized = sanitized.replace("\r\n", "\n").replace("\r", "\n")
    sanitized = sanitized.strip()
    return sanitized


def enforce_limits(state: State) -> None:
    """Enforce strict size limits to prevent abuse."""
    code = state.code

    # Character limit
    if len(code) > MAX_CODE_LENGTH:
        msg = f"Input too large: {len(code)} characters"
        Logger.error(msg, agent="Security")
        state.errors.append(msg)

    # Line count limit
    lines = code.split("\n")
    if len(lines) > MAX_LINE_COUNT:
        msg = f"Too many lines: {len(lines)}"
        Logger.error(msg, agent="Security")
        state.errors.append(msg)

    # Average line length heuristic
    # Fixed: renamed 'l' to 'line' to avoid E741
    avg_len = sum(len(line) for line in lines) / max(len(lines), 1)
    if avg_len > MAX_AVG_LINE_LENGTH:
        msg = f"Average line length too large: {avg_len:.2f}"
        Logger.error(msg, agent="Security")
        state.warnings.append(msg)


def detect_malicious_patterns(state: State) -> None:
    """Detect dangerous or malicious code patterns."""
    code = state.code

    for pattern in DANGEROUS_PATTERNS:
        if pattern.search(code):
            msg = f"Potentially dangerous pattern detected: {pattern.pattern}"
            Logger.error(msg, agent="Security")
            state.errors.append(msg)


def secure_process(state: State) -> State:
    """Full security pipeline applied before agents run."""
    Logger.info("Running security checks", agent="Security")

    # Step 1: sanitize
    state.code = sanitize_input(state.code)

    # Step 2: size limits
    enforce_limits(state)

    # Step 3: malicious pattern detection
    detect_malicious_patterns(state)

    Logger.info("Security checks completed", agent="Security")
    return state
