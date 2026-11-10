# rv32-linux-soc

Projet personnel : concevoir un cœur RISC-V 32 bits **in-order** (pas superscalaire), l'intégrer à un **SoC** et lui faire démarrer **Linux**.

Le projet est mené en simulation, de la spécification au démarrage de Linux. Tout le parcours est documenté dans ce dépôt.

## Organisation

| Dossier | Contenu |
|---|---|
| `doc/` | Fiche projet et spécifications |
| `rtl/` | Code matériel (SystemVerilog) |
| `dv/` | Vérification et tests |
| `sw/` | Logiciel (programmes de test, firmware, noyau) |
| `tools/` | Scripts et outils |
| `journal/` | Journal de bord |

## Auteur

Mouad Zouhdi
