"""Prioritizer Module - Prioritizes proposals by urgency and impact"""

from typing import List
from .proposer import Proposal


class Prioritizer:
    """Prioritizes proposals by urgency and impact."""
    
    PRIORITY_WEIGHTS = {
        "critical": 100,
        "week": 50,
        "opportunistic": 10,
    }
    
    def prioritize(self, proposals: List[Proposal]) -> List[Proposal]:
        """Sort proposals by priority."""
        return sorted(
            proposals,
            key=lambda p: self.PRIORITY_WEIGHTS.get(p.urgency, 0),
            reverse=True
        )
    
    def select_best(self, proposals: List[Proposal], count: int = 5) -> List[Proposal]:
        """Select the N best proposals."""
        prioritized = self.prioritize(proposals)
        return prioritized[:count]
