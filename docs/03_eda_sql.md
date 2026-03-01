# Phase 3: EDA with SQL — Findings

## Overview
Loaded the SpaceX dataset into a SQLite database and executed 10 SQL queries to explore patterns in launch data.

## Task 1: Unique Launch Sites

| Launch_Site   |
|:--------------|
| CCAFS LC-40   |
| VAFB SLC-4E   |
| KSC LC-39A    |
| CCAFS SLC-40  |

## Task 2: 5 Records with Launch Site Starting 'CCA'

| Date       | Time (UTC)   | Booster_Version   | Launch_Site   | Payload                                                       |   PAYLOAD_MASS__KG_ | Orbit     | Customer        | Mission_Outcome   | Landing_Outcome     |
|:-----------|:-------------|:------------------|:--------------|:--------------------------------------------------------------|--------------------:|:----------|:----------------|:------------------|:--------------------|
| 2010-06-04 | 18:45:00     | F9 v1.0  B0003    | CCAFS LC-40   | Dragon Spacecraft Qualification Unit                          |                   0 | LEO       | SpaceX          | Success           | Failure (parachute) |
| 2010-12-08 | 15:43:00     | F9 v1.0  B0004    | CCAFS LC-40   | Dragon demo flight C1, two CubeSats, barrel of Brouere cheese |                   0 | LEO (ISS) | NASA (COTS) NRO | Success           | Failure (parachute) |
| 2012-05-22 | 7:44:00      | F9 v1.0  B0005    | CCAFS LC-40   | Dragon demo flight C2                                         |                 525 | LEO (ISS) | NASA (COTS)     | Success           | No attempt          |
| 2012-10-08 | 0:35:00      | F9 v1.0  B0006    | CCAFS LC-40   | SpaceX CRS-1                                                  |                 500 | LEO (ISS) | NASA (CRS)      | Success           | No attempt          |
| 2013-03-01 | 15:10:00     | F9 v1.0  B0007    | CCAFS LC-40   | SpaceX CRS-2                                                  |                 677 | LEO (ISS) | NASA (CRS)      | Success           | No attempt          |

## Task 3: Total Payload Mass for NASA (CRS)

|   total_payload_mass |
|---------------------:|
|                45596 |

## Task 4: Average Payload Mass for F9 v1.1

|   avg_payload_mass |
|-------------------:|
|             2928.4 |

## Task 5: First Successful Ground Pad Landing Date

| first_ground_pad_success   |
|:---------------------------|
| 2015-12-22                 |

## Task 6: Boosters with Drone Ship Success (4000-6000 kg)

| Booster_Version   |
|:------------------|
| F9 FT B1022       |
| F9 FT B1026       |
| F9 FT  B1021.2    |
| F9 FT  B1031.2    |

## Task 7: Mission Outcome Counts

| Mission_Outcome                  |   count |
|:---------------------------------|--------:|
| Success                          |      98 |
| Success (payload status unclear) |       1 |
| Success                          |       1 |
| Failure (in flight)              |       1 |

## Task 8: Boosters Carrying Maximum Payload

| Booster_Version   |
|:------------------|
| F9 B5 B1048.4     |
| F9 B5 B1049.4     |
| F9 B5 B1051.3     |
| F9 B5 B1056.4     |
| F9 B5 B1048.5     |
| F9 B5 B1051.4     |
| F9 B5 B1049.5     |
| F9 B5 B1060.2     |
| F9 B5 B1058.3     |
| F9 B5 B1051.6     |
| F9 B5 B1060.3     |
| F9 B5 B1049.7     |

## Task 9: Failed Drone Ship Landings in 2015

|   month | Landing_Outcome      | Booster_Version   | Launch_Site   |
|--------:|:---------------------|:------------------|:--------------|
|      01 | Failure (drone ship) | F9 v1.1 B1012     | CCAFS LC-40   |
|      04 | Failure (drone ship) | F9 v1.1 B1015     | CCAFS LC-40   |

## Task 10: Landing Outcome Ranks (2010-06-04 to 2017-03-20)

| Landing_Outcome        |   count |
|:-----------------------|--------:|
| No attempt             |      10 |
| Success (drone ship)   |       5 |
| Failure (drone ship)   |       5 |
| Success (ground pad)   |       3 |
| Controlled (ocean)     |       3 |
| Uncontrolled (ocean)   |       2 |
| Failure (parachute)    |       2 |
| Precluded (drone ship) |       1 |

### Task 1 — Interpretation
Four distinct launch sites are used by SpaceX across the US — two in Florida (Cape Canaveral area), one at Vandenberg AFB in California, and one at Kennedy Space Center.

### Task 2 — Interpretation
CCAFS SLC 40 is the dominant launch site for SpaceX operations, especially for early Falcon 9 missions.

### Task 3 — Interpretation
NASA CRS (Commercial Resupply Services) missions collectively carried a significant payload to the ISS — these are cargo/crew resupply missions.

### Task 4 — Interpretation
F9 v1.1 was an intermediate booster version. Its average payload gives insight into the typical mission profile before Block 5 upgrades.

### Task 5 — Interpretation
The first successful ground pad (RTLS) landing was a major milestone — it proved SpaceX could return boosters to the launch site.

### Task 6 — Interpretation
Drone ship landings with mid-range payloads (4000-6000 kg) show the versatility of the Falcon 9 for commercial deployments.

### Task 7 — Interpretation
The vast majority of missions achieved their primary objective (payload delivery), even when the booster landing failed.

### Task 8 — Interpretation
The heaviest payloads were carried by the latest booster versions, reflecting improvements in thrust and structural design.

### Task 9 — Interpretation
2015 was a pivotal year — SpaceX was still perfecting drone ship landings, leading to several failures.

### Task 10 — Interpretation
Over the 2010-2017 period, "No attempt" dominates early missions, while successful landings (drone ship and ground pad) increase over time.

