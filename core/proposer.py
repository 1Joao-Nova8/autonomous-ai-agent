"""Proposer Module - Generates actionable proposals"""

from typing import List
from dataclasses import dataclass


@dataclass
class Proposal:
    """A single actionable proposal."""
    title: str
    reason: str
    next_step: str
    urgency: str  # "critical", "week", "opportunistic"
    category: str


class Proposer:
    """Generates concrete, actionable proposals based on detections."""
    
    def __init__(self):
        self.proposals: List[Proposal] = []
    
    def propose(self, detections: dict) -> List[Proposal]:
        """Generate proposals from detections."""
        self.proposals = []
        
        # Convert detections to proposals
        for issue in detections.get("critical_issues", []):
            self._create_proposal_from_issue(issue)
        
        for opportunity in detections.get("opportunities", []):
            self._create_proposal_from_opportunity(opportunity)
        
        return self.proposals
    
    def _create_proposal_from_issue(self, issue: dict):
        """Convert a detected issue to a proposal."""
        pass
    
    def _create_proposal_from_opportunity(self, opportunity: dict):
        """Convert an opportunity to a proposal."""
        pass
    
    def format_proposal(self, proposal: Proposal) -> str:
        """Format a proposal for display."""
        urgency_icon = {
            "critical": "🔴",
            "week": "🟡",
            "opportunistic": "🟢",
        }.get(proposal.urgency, "❓")
        
        return f"""
📋 {proposal.title}
🔍 Pourquoi maintenant : {proposal.reason}
➡️ Prochaine étape : {proposal.next_step}
⚠️ Urgence : {urgency_icon} {proposal.urgency.upper()}
        """.strip()
