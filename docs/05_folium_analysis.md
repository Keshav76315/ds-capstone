# Phase 5: Interactive Visual Analytics (Folium) — Findings

## Overview
Used Folium to create interactive maps visualizing launch sites, success/failure outcomes, and geographic proximities.

## Task 1: Launch Site Locations
All 4 SpaceX launch sites were marked on an interactive map.

| Launch Site | Latitude | Longitude |
|---|---|---|
| CCAFS LC-40 | 28.5623 | -80.5774 |
| CCAFS SLC-40 | 28.5632 | -80.5768 |
| KSC LC-39A | 28.5733 | -80.6469 |
| VAFB SLC-4E | 34.6328 | -120.6107 |

**Geographic observations:**
- All launch sites are located near the coast — this is essential for safety (failed rockets fall into the ocean)
- Florida sites (CCAFS, KSC) are near the equator (~28.5°N), providing a velocity boost from Earth's rotation for equatorial orbits
- VAFB in California (~34.6°N) is used primarily for polar/sun-synchronous orbits where equatorial boost is irrelevant

## Task 2: Success/Failure Markers
Color-coded markers (green = success, red = failure) were added using MarkerClusters.

| Launch Site | Successes | Total | Success Rate |
|---|---|---|---|
| CCAFS LC-40 | 7 | 26 | 26.9% |
| CCAFS SLC-40 | 3 | 7 | 42.9% |
| KSC LC-39A | 10 | 13 | 76.9% |
| VAFB SLC-4E | 4 | 10 | 40.0% |

**KSC LC-39A has the highest success rate** — this is NASA's historic pad (Apollo, Shuttle) and SpaceX uses it for high-profile missions.

## Task 3: Proximity Distances (CCAFS SLC-40)
| Feature | Distance |
|---|---|
| Coastline | 0.98 km |
| City | Cocoa Beach (19.26 km) |
| Railway | 1.36 km |
| Highway | 0.60 km |

**Key proximity insights:**
- Launch sites are very close to the coastline (< 1 km) for ocean-drop safety
- Sites maintain distance from major cities for population safety
- Railway and highway access are nearby for logistics (transporting rocket stages)

## Interactive Maps (HTML)
- `folium_launch_sites.html` — all 4 sites with labels
- `folium_launch_outcomes.html` — success/fail color-coded markers
- `folium_distances.html` — proximity lines to coast, city, railway, highway
