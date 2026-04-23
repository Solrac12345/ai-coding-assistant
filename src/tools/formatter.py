import subprocess


class CodeFormatter:
    """
    EN:
        Wrapper around the Black formatter.
        In Phase 2, this class defines the interface and a basic implementation
        using a subprocess call. It can be replaced or extended later.

    FR:
        Enveloppe autour du formateur Black.
        En Phase 2, cette classe définit l'interface et une implémentation de base
        utilisant un appel subprocess. Elle pourra être remplacée ou étendue plus tard.
    """

    def format_code(self, code: str) -> str:
        """
        EN:
            Format the given Python code using Black via subprocess.
            If formatting fails, the original code is returned.

        FR:
            Formate le code Python fourni en utilisant Black via subprocess.
            En cas d'échec, le code original est renvoyé.
        """
        try:
            process = subprocess.run(
                ["black", "-q", "-"],
                input=code.encode("utf-8"),
                capture_output=True,
                check=False,
            )

            # If Black writes to stdout, use it; otherwise, return original code.
            if process.stdout:
                return process.stdout.decode("utf-8")
        except Exception:
            # EN: Fail-safe: never crash the app because of formatting.
            # FR: Filet de sécurité : ne jamais faire planter l'app à cause du formatage.
            return code

        return code

