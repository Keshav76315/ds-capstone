# Phase 1: Data Collection — Findings

## Data Source
Data was collected from the SpaceX REST API (v4) using a static JSON snapshot hosted by IBM.
The API endpoints used were:
- `/v4/launches/past` — past launch records
- `/v4/rockets/` — rocket/booster details
- `/v4/launchpads/` — launch site coordinates
- `/v4/payloads/` — payload mass and orbit info
- `/v4/cores/` — core landing outcomes and reuse data

## Raw Data Overview
- Total launches retrieved: **94**
- Columns extracted: **17** (FlightNumber, Date, BoosterVersion, PayloadMass, Orbit, LaunchSite, Outcome, Flights, GridFins, Reused, Legs, LandingPad, Block, ReusedCount, Serial, Longitude, Latitude)
- Booster types: **Falcon 1, Falcon 9**
  - Falcon 1 launches: **4**
  - Falcon 9 launches: **90**

## Task 2: Filtering to Falcon 9
- Removed all Falcon 1 launches (early test flights, different rocket architecture)
- Remaining records: **90** Falcon 9 launches
- FlightNumber was reset to sequential 1–90

## Task 3: Handling Missing Values
- Missing values before imputation:
PayloadMass     5
LandingPad     26

- Strategy: Replaced missing `PayloadMass` values with the column mean (**6123.55 kg**)
- After imputation, only `LandingPad` retains None values (intentional — represents launches where no landing pad was used)

## Launch Sites
LaunchSite
CCSFS SLC 40    55
KSC LC 39A      22
VAFB SLC 4E     13

## Orbit Distribution
Orbit
GTO      27
ISS      21
VLEO     14
PO        9
LEO       7
SSO       5
MEO       3
HEO       1
ES-L1     1
SO        1
GEO       1

## Landing Outcomes
Outcome
True ASDS      41
None None      19
True RTLS      14
False ASDS      6
True Ocean      5
False Ocean     2
None ASDS       2
False RTLS      1

## Output
- Exported cleaned dataset to `dataset_part_1.csv` (90 rows × 17 columns)
