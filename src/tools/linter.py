import subprocess
from typing import List


class CodeLinter:
    """
    EN:
        Wrapper around the Ruff linter.
        In Phase 2, this class exposes a simple interface to run Ruff on
        a given code string and return the reported issues.

    FR:
        Enveloppe autour du linter Ruff.
        En Phase 2, cette classe expose une interface simple pour exécuter Ruff
        sur une chaîne de code et renvoyer les problèmes signalés.
    """

    def lint_code(self, code: str) -> List[str]:
        """
        EN:
            Run Ruff on the provided code using subprocess.
            Returns a list of diagnostic messages (as strings).

        FR:
            Exécute Ruff sur le code fourni en utilisant subprocess.
            Renvoie une liste de messages de diagnostic (sous forme de chaînes).
        """
        try:
            process = subprocess.run(
                ["ruff", "-"],
                input=code.encode("utf-8"),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
            )

            output = process.stdout.decode("utf-8").strip()
            if not output:
                return []

            return output.splitlines()
        except Exception:
            # EN: On any failure, return an empty list instead of raising.
            # FR: En cas d'échec, renvoyer une liste vide au lieu de lever une exception.
            return []
