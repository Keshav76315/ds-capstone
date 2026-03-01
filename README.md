# SpaceX Falcon 9 First Stage Landing Prediction

This is my capstone project for the **IBM Data Science Professional Certificate** — specifically the **Applied Data Science Capstone** course. The goal was to predict whether the Falcon 9 first stage would successfully land after a launch, using real data from SpaceX.

The motivation is straightforward: SpaceX advertises Falcon 9 launches at $62 million, while competitors charge upwards of $165 million. The cost savings come from reusing the first stage. If we can predict whether a landing will succeed, we can estimate launch costs — useful for any company looking to compete with SpaceX in the launch market.

## How I approached this

I followed the standard data science workflow: collect data, clean it, explore it, and then build models.

### Data Collection

I pulled data from the SpaceX REST API (v4), hitting endpoints for launches, rockets, launchpads, payloads, and cores. After filtering out the older Falcon 1 flights, I was left with **90 Falcon 9 launches** spanning 2010 to 2020. There were a few missing payload mass values which I filled in with the column mean.

### Data Wrangling

The raw landing outcomes from the API are granular — things like "True ASDS" (successful drone ship landing), "False RTLS" (failed ground pad landing), "None None" (no landing attempt), etc. I collapsed these into a binary label: 1 for a successful landing, 0 for anything else.

The split came out to **60 successes and 30 failures**, giving a baseline success rate of about 66.7%.

### Exploratory Analysis

This is where things got interesting. I ran SQL queries against the dataset and built a bunch of visualizations to understand what drives landing success.

One of the clearest patterns was the **yearly trend**:

![Yearly success trend](docs/viz_06_yearly_trend.png)

Early flights had very low success rates, which makes sense — SpaceX was still figuring out how to land these things. By 2019-2020, they were landing nearly every time.

**Orbit type matters a lot.** Some orbits like GEO, HEO, and ES-L1 had 100% landing success, while GTO (the most common orbit for commercial satellites) had the lowest success rate among frequently-used orbits.

![Success rate by orbit](docs/viz_03_success_by_orbit.png)

**Launch site also plays a role.** KSC LC-39A (the historic Kennedy Space Center pad) showed the highest success proportion, especially for later flights. VAFB SLC-4E in California only handled payloads under about 10,000 kg.

![Flight number vs launch site](docs/viz_01_flightnum_vs_site.png)

![Payload mass vs launch site](docs/viz_02_payload_vs_site.png)

Looking at flight number against payload mass, there's a visible pattern — as SpaceX gained experience (higher flight numbers), they started landing successfully even with heavier payloads.

![Flight number vs payload mass](docs/viz_00_flightnum_vs_payload.png)

### Interactive Maps

I used Folium to map out the launch sites and color-code each launch by success (green) or failure (red). A few things stood out:

- All launch sites are right on the coast, which is a safety measure — failed rockets fall into the ocean
- The Florida sites sit near the equator (~28.5 N), which gives a speed boost for equatorial orbits
- Vandenberg in California is used mainly for polar orbits where that boost doesn't matter

I also measured distances from CCAFS SLC-40 to nearby features: the coastline is less than 1 km away, while the nearest city (Cocoa Beach) is about 19 km out. Railway and highway access are close by for logistics.

The interactive maps are saved in `docs/` as HTML files if you want to explore them.

### Machine Learning

For the prediction task, I engineered features using one-hot encoding on categorical columns (orbit type, launch site, landing pad, serial number), which expanded the feature space to 83 columns. I standardized everything with StandardScaler and split 80/20 for train/test.

I tried four classifiers, each with GridSearchCV (cv=10) for hyperparameter tuning:

| Model               | Best CV Score | Test Accuracy |
| ------------------- | ------------- | ------------- |
| Logistic Regression | 0.846         | 0.833         |
| SVM                 | 0.848         | 0.833         |
| Decision Tree       | 0.863         | 0.833         |
| KNN                 | 0.848         | 0.833         |

![Model comparison](docs/ml_model_comparison.png)

All four models converged to the same test accuracy of 83.3%. With only 18 test samples, that means 3 were misclassified. The Decision Tree had the highest cross-validation score at 0.863.

Here's the confusion matrix for Logistic Regression as an example — the main error type was false positives (predicting a landing when it actually failed):

![Logistic Regression confusion matrix](docs/ml_cm_logistic_regression.png)

## What I found

1. **Landing success is predictable.** All four models hit ~83% accuracy, which is solid given the small dataset.
2. **Flight experience is the biggest factor.** Later flights succeed far more often than early ones. SpaceX clearly got better at this over time.
3. **Orbit and payload mass matter.** Heavier payloads going to challenging orbits (like GTO) are harder to land after.
4. **Launch site correlates with success**, partly because KSC LC-39A was used more for later, higher-confidence missions.
5. **The models agree.** The fact that four different algorithms all land on the same accuracy suggests the signal in the data is consistent and not dependent on model choice.

## Project structure

```
ds-capstone/
  jupyter-labs-spacex-data-collection-api.ipynb   # Data collection from SpaceX API
  labs-jupyter-spacex-Data wrangling.ipynb         # Data cleaning and label creation
  jupyter-labs-eda-sql-coursera_sqllite.ipynb      # SQL-based exploration
  edadataviz.ipynb                                 # Visualizations and feature engineering
  lab_jupyter_launch_site_location.ipynb           # Folium interactive maps
  SpaceX_Machine Learning Prediction_Part_5.ipynb  # ML models and evaluation
  dataset_part_1.csv                               # Cleaned Falcon 9 data
  dataset_part_2.csv                               # With binary class labels
  dataset_part_3.csv                               # Feature-engineered for ML
  docs/                                            # All findings, visualizations, and maps
```

## Tools used

- Python (pandas, numpy, matplotlib, seaborn, scikit-learn, folium)
- SQLite for SQL queries
- Jupyter Notebook
