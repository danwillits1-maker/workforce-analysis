# Workforce Attrition Analysis

A workforce analytics project exploring patterns associated with employee attrition using Python, PostgreSQL, and Power BI.

## Project question

Which employee, role, and work patterns are associated with attrition, and where could retention efforts be focused?

## Dashboard

<!-- Add a screenshot here once you upload it to the repository -->
![Workforce dashboard preview](3_Power%20BI/images/dashboard_page_1.png)
## Key findings

- Overall attrition was 9.03% across 10,000 employees.
- Engineering had the highest attrition rate of 9.58% with the HR department comparatively low at 7.27%. 
- Employees working overtime showed a 1.56x higher likelihood of attrition across all employees analysed.

These are descriptive patterns in the dataset. They do not show that any factor caused employees to leave.

## Project workflow

1. Python: cleaned and prepared the source data.
2. PostgreSQL: stored and structured the data for analysis.
3. Power BI: created the dashboard and DAX measures.

## Estimated attrition cost

The estimate applies this assumption to employees marked as having left:

`monthly income × 12 × 1.5`

The 1.5 multiplier is an assumption. This is an estimated cost proxy, not a recorded company cost.

## Repository contents

- `1_Python/clean_data.ipynb` — data preparation scripts
- `2_SQL/create_dataset.sql` — database and transformation scripts
- `3_Power BI/workforce_dashboard.pbix` — Power BI report
- `3_Power BI/images/dashboard_page_1-3.png` — dashboard screenshots

## Data and limitations

- Dataset: ![Raw Dataset](4_Dataset/employee_dataset_raw.csv)
- The data represents a realistic, synthetic dataset sources from ![Kaggle](https://www.kaggle.com/datasets/personacarved/employee-attrition-dataset).
- The analysis shows associations, not causes.
- Findings and recommendations should be interpreted within the limits of this dataset.

## Tools

Python · Pandas · PostgreSQL · Power BI · DAX
