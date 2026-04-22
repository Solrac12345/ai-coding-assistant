from dataclasses import dataclass, field
from typing import Optional, Dict, Any


@dataclass
class State:
    """
    Global shared state for the AI Coding Assistant.

    EN:
        This class represents the shared state that flows through the
        Supervisor and all agents (Analyzer, Optimizer, DocAgent).
        Each agent reads and updates specific fields as the workflow progresses.

    FR:
        Cette classe représente l'état partagé qui circule entre le
        Superviseur et tous les agents (Analyzer, Optimizer, DocAgent).
        Chaque agent lit et met à jour certains champs au fur et à mesure.
    """

    # EN: Raw code provided by the user.
    # FR: Code brut fourni par l'utilisateur.
    code_input: str

    # EN: Human-readable analysis of the input code (issues, smells, patterns).
    # FR: Analyse lisible du code (problèmes, mauvaises pratiques, motifs).
    analysis: Optional[str] = None

    # EN: Improved / refactored version of the original code.
    # FR: Version améliorée / refactorisée du code original.
    optimized_code: Optional[str] = None

    # EN: Generated documentation (docstrings, comments, explanations).
    # FR: Documentation générée (docstrings, commentaires, explications).
    documentation: Optional[str] = None

    # EN: Extra metadata for scalability (language, complexity, tags, etc.).
    # FR: Métadonnées supplémentaires pour la scalabilité (langage, complexité, tags, etc.).
    metadata: Dict[str, Any] = field(default_factory=dict)
