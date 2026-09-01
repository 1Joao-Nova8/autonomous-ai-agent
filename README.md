# Agent IA Autonome 🤖

Un agent IA autonome et proactif, membre actif de ton équipe. Il n'attend pas les questions — il observe, détecte, et propose du travail constant.

## 🎯 Mission

À chaque activation, l'agent produit **3 à 5 propositions concrètes** (tâches, idées, améliorations, alertes) qui font avancer le projet, sans intervention humaine requise.

## 🧠 Comment ça marche

### Cycle de raisonnement

1. **Observe** → État du projet, avancement, blocages, dernières actions
2. **Détecte** → Ce qui traîne, ce qui manque, risques, opportunités
3. **Priorise** → Par urgence/impact, pas par ordre chrono
4. **Propose** → Actions claires et actionnables

### Format de chaque proposition

```
📋 [Titre court orienté action]
🔍 Pourquoi maintenant : [déclencheur/opportunité — 1 phrase]
➡️ Prochaine étape : [action concrète à valider]
⚠️ Urgence : 🔴 critique | 🟡 cette semaine | 🟢 opportuniste
```

## 📋 Règles de comportement

- ✅ **Toujours proposer quelque chose** — le silence n'existe pas
- ✅ **Rester concret** — pas de généralités, des actions précises
- ✅ **Signaler les risques d'abord** — blocages avant cosmétique
- ✅ **Rester bref** — 3-4 lignes par proposition max
- ✅ **Ne pas répéter** — si déjà proposé, ajouter nouvelle info ou passer
- ✅ **Respecter la portée** — suggestions externes = clairement marquées

## ⏰ Activation

L'agent s'active :
- À intervalles réguliers (à définir)
- Après événements clés du projet
- À la demande manuelle

## 📁 Structure du projet

```
autonomous-ai-agent/
├── core/                    # Moteur principal de l'agent
│   ├── observer.py         # Module d'observation du projet
│   ├── detector.py         # Détection de risques/opportunités
│   ├── proposer.py         # Génération de propositions
│   └── prioritizer.py      # Priorisation intelligente
├── config/                 # Configuration et déclencheurs
│   ├── activation.yaml     # Quand s'activer
│   └── rules.yaml          # Règles de comportement
├── data/                   # État du projet, historique
│   ├── project_state.json  # Snapshot actuel
│   └── history.log         # Propositions antérieures
├── outputs/                # Propositions générées
├── tests/                  # Tests unitaires
└── README.md               # Ce fichier
```

## 🚀 Démarrage rapide

```bash
# Installation des dépendances
pip install -r requirements.txt

# Lancer une génération manuelle
python run.py

# Activer le mode surveillance (intervalles réguliers)
python daemon.py
```

## 📊 Exemple de sortie

```
🤖 PROPOSITIONS D'AUJOURD'HUI (3 items)

1️⃣ 📋 Configurer l'automatisation des tests avant merge
   🔍 Pourquoi : Aucun test n'a roulé sur les 3 derniers commits
   ➡️ Prochaine étape : Ajouter GitHub Actions workflow `.github/workflows/test.yml`
   ⚠️ 🔴 CRITIQUE

2️⃣ 📋 Documenter l'API des modules core/
   🔍 Pourquoi : 3 fonctions sans docstring, risque de confusion
   ➡️ Prochaine étape : Ajouter docstrings + générer doc auto avec Sphinx
   ⚠️ 🟡 CETTE SEMAINE

3️⃣ 📋 Explorer intégration avec {service X}
   🔍 Pourquoi : Feature requestée 2x, faisable avant sprint suivant
   ➡️ Prochaine étape : Créer issue exploratoire, estimer effort
   ⚠️ 🟢 OPPORTUNISTE
```

## 📝 État du projet

- ✅ Dépôt créé
- ✅ Architecture initialisée
- ⏳ Modules core en développement
- ⏳ Tests et intégration

---

**Créé avec ❤️ pour l'autonomie productive.**