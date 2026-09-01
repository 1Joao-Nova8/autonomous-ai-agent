#!/usr/bin/env python
"""Main entry point for manual proposal generation."""

import sys
from pathlib import Path

from core.observer import Observer
from core.detector import Detector
from core.proposer import Proposer
from core.prioritizer import Prioritizer


def main():
    """Run a full cycle: observe -> detect -> propose -> prioritize."""
    print("🤖 Agent IA Autonome - Génération de propositions\n")
    print("="*60)
    
    # Step 1: Observe
    print("\n📚 OBSERVATION du projet...")
    observer = Observer()
    state = observer.observe()
    observer.save_state()
    print(f"État sauvegardé dans data/project_state.json")
    
    # Step 2: Detect
    print("\n🔍 DÉTECTION des risques et opportunités...")
    detector = Detector()
    detections = detector.detect(state)
    print(f"Trouvé {len(detections['critical_issues'])} problèmes critiques")
    print(f"Trouvé {len(detections['opportunities'])} opportunités")
    
    # Step 3: Propose
    print("\n💡 GÉNÉRATION des propositions...")
    proposer = Proposer()
    proposals = proposer.propose(detections)
    
    # Step 4: Prioritize
    print("\n⚡ PRIORISATION des propositions...")
    prioritizer = Prioritizer()
    best_proposals = prioritizer.select_best(proposals, count=5)
    
    # Output
    print("\n" + "="*60)
    print("\n🤖 PROPOSITIONS D'AUJOURD'HUI\n")
    
    if not best_proposals:
        print("✅ Aucune proposition urgente. Projet en bon état!")
    else:
        for i, proposal in enumerate(best_proposals, 1):
            print(f"{i}️⃣  {proposer.format_proposal(proposal)}\n")
    
    print("="*60)
    print("\n✨ Propositions générées et sauvegardées.")


if __name__ == "__main__":
    main()
