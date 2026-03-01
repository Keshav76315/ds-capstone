# Presentation Visuals Guide

Which visualizations to use for each slide in the IBM DS Capstone presentation.

## Slide: Executive Summary

- `viz_06_yearly_trend.png` — shows the clear upward trend in landing success

## Slide: Data Collection Methodology

- No visualization needed — describe API data pipeline

## Slide: EDA with SQL

- Tables from `03_eda_sql.md` (Task 3: NASA CRS payload, Task 5: first ground landing date, Task 10: outcome rankings)

## Slide: EDA Visualization

- `viz_03_success_by_orbit.png` — success rate by orbit (shows ES-L1, GEO, HEO at 100%)
- `viz_01_flightnum_vs_site.png` — flight number vs launch site pattern
- `viz_02_payload_vs_site.png` — payload mass differences across sites

## Slide: Interactive Map Analysis

- Screenshot from `folium_launch_outcomes.html` (green/red markers)
- Screenshot from `folium_distances.html` (proximity lines)

## Slide: Dashboard Analysis (Plotly Dash)

- `Slide_39.png` — All Sites Pie Chart showing total success launches
- `Slide_40.png` — KSC LC-39A Pie Chart showing highest success ratio
- `Slide_41.png` — Scatter Plot showing correlation between payload mass and success

## Slide: Predictive Analysis

- `ml_model_comparison.png` — all 4 models side-by-side
- One confusion matrix (pick `ml_cm_decision_tree.png` — it has the highest CV score)

## Slide: Methodology

- `viz_00_flightnum_vs_payload.png` — overview scatter plot

## Slide: Conclusion

- `viz_06_yearly_trend.png` — landing success improves over time
- `ml_model_comparison.png` — all models achieve ~83% test accuracy

## All Available Visualizations

| File                              | Phase | Description                          |
| --------------------------------- | ----- | ------------------------------------ |
| `viz_00_flightnum_vs_payload.png` | 4     | Flight Number vs Payload Mass        |
| `viz_01_flightnum_vs_site.png`    | 4     | Flight Number vs Launch Site         |
| `viz_02_payload_vs_site.png`      | 4     | Payload Mass vs Launch Site          |
| `viz_03_success_by_orbit.png`     | 4     | Success Rate by Orbit Type           |
| `viz_04_flightnum_vs_orbit.png`   | 4     | Flight Number vs Orbit Type          |
| `viz_05_payload_vs_orbit.png`     | 4     | Payload Mass vs Orbit Type           |
| `viz_06_yearly_trend.png`         | 4     | Launch Success Yearly Trend          |
| `ml_cm_logistic_regression.png`   | 6     | Logistic Regression Confusion Matrix |
| `ml_cm_svm.png`                   | 6     | SVM Confusion Matrix                 |
| `ml_cm_decision_tree.png`         | 6     | Decision Tree Confusion Matrix       |
| `ml_cm_knn.png`                   | 6     | KNN Confusion Matrix                 |
| `ml_model_comparison.png`         | 6     | Model Comparison Bar Chart           |
| `folium_launch_sites.html`        | 5     | Launch Sites Map                     |
| `folium_launch_outcomes.html`     | 5     | Success/Fail Markers Map             |
| `folium_distances.html`           | 5     | Proximity Distance Map               |
| `Slide_39.png`                    | -     | Dashboard: All Sites Pie Chart       |
| `Slide_40.png`                    | -     | Dashboard: KSC Pie Chart             |
| `Slide_41.png`                    | -     | Dashboard: Payload Scatter Plot      |
