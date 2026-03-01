# Phase 2: Data Wrangling — Findings

## Objective
Convert raw landing outcomes into binary training labels for the ML model.

## Dataset
- Loaded from IBM-hosted `dataset_part_1.csv` (consistent with course)
- Shape: **90 rows × 18 columns**
- Missing values: PayloadMass (0.0%), LandingPad (28.9%)

## Task 1: Launches Per Site
| Launch Site | Count |
|---|---|
| CCAFS SLC 40 | 55 |
| KSC LC 39A | 22 |
| VAFB SLC 4E | 13 |

**CCSFS SLC 40** dominates with 55 launches — it's SpaceX's primary operational pad at Cape Canaveral.

## Task 2: Orbit Distribution
| Orbit | Count |
|---|---|
| GTO | 27 |
| ISS | 21 |
| VLEO | 14 |
| PO | 9 |
| LEO | 7 |
| SSO | 5 |
| MEO | 3 |
| HEO | 1 |
| ES-L1 | 1 |
| SO | 1 |
| GEO | 1 |

**GTO** (Geostationary Transfer Orbit) is most common — these are typically commercial satellite deliveries. **ISS** missions are the second most frequent, reflecting SpaceX's cargo/crew resupply contracts with NASA.

## Task 3: Landing Outcomes
| Outcome | Count |
|---|---|
| True ASDS | 41 |
| None None | 19 |
| True RTLS | 14 |
| False ASDS | 6 |
| True Ocean | 5 |
| False Ocean | 2 |
| None ASDS | 2 |
| False RTLS | 1 |

- **True ASDS** = successful drone ship landing (most common success type)
- **True RTLS** = successful ground pad landing
- **None None** = no landing attempt (early flights)

Bad outcomes (unsuccessful landings):
- False ASDS
- False Ocean
- False RTLS
- None ASDS
- None None

## Task 4: Binary Classification Labels
- **Class 1** (successful landing): **60** launches
- **Class 0** (unsuccessful): **30** launches
- **Overall success rate: 66.7%**

This ~66.7% success rate means the classes are moderately imbalanced but workable for classification without heavy resampling.

## Output
- Exported `dataset_part_2.csv` (90 rows × 18 columns, including the new `Class` column)
