--==================================
-- CREATE TABLE FOR DATA IMPORTATION
--==================================

CREATE TABLE staging_hr_data (
    employee_id VARCHAR(50),
    age INT,
    department VARCHAR(100),
    job_level INT,
    years_at_company INT,
    monthly_income INT,
    job_satisfaction INT,
    work_life_balance INT,
    over_time VARCHAR(10),
    distance_from_home NUMERIC,
    promotion_last_5_years VARCHAR(10),
    performance_rating INT,
    training_hours_last_year INT,
    attrition VARCHAR(10));

SELECT *
FROM staging_hr_data
LIMIT 10

--=========================
-- CREATION OF STAR SCHEMA 
--=========================

BEGIN;


-- 1. CREATE DIMENSION TABLES

CREATE TABLE dim_employee (
    employee_id VARCHAR(50) PRIMARY KEY,
    age INT,
    distance_from_home NUMERIC
);

CREATE TABLE dim_department (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(100) UNIQUE NOT NULL
);

-- New: Survey Profile Junk Dimension
CREATE TABLE dim_survey_profile (
    survey_id SERIAL PRIMARY KEY,
    job_satisfaction INT,
    work_life_balance INT,
    performance_rating INT
);

-- New: HR Flags Junk Dimension
CREATE TABLE dim_hr_flags (
    flag_id SERIAL PRIMARY KEY,
    over_time VARCHAR(10),
    promotion_last_5_years VARCHAR(10)
);

-- ==========================================
-- 2. CREATE FACT TABLE
-- ==========================================

CREATE TABLE fact_employee_metrics (
    fact_id SERIAL PRIMARY KEY,
    employee_id VARCHAR(50) REFERENCES dim_employee(employee_id),
    department_id INT REFERENCES dim_department(department_id),
    survey_id INT REFERENCES dim_survey_profile(survey_id),
    flag_id INT REFERENCES dim_hr_flags(flag_id),
    
    -- Numerical Facts / Measures
    job_level INT,
    monthly_income INT,
    years_at_company INT,
    training_hours_last_year INT,
    
    -- Target Variable
    attrition VARCHAR(10) NOT NULL
);

-- ==========================================
-- 3. POPULATE DIMENSION TABLES FROM STAGING
-- ==========================================

INSERT INTO dim_employee (employee_id, age, distance_from_home)
SELECT DISTINCT employee_id, age, distance_from_home FROM staging_hr_data;

INSERT INTO dim_department (department_name)
SELECT DISTINCT department FROM staging_hr_data WHERE department IS NOT NULL;

-- Find all unique combinations of survey scores
INSERT INTO dim_survey_profile (job_satisfaction, work_life_balance, performance_rating)
SELECT DISTINCT job_satisfaction, work_life_balance, performance_rating FROM staging_hr_data;

-- Find all unique combinations of HR flags
INSERT INTO dim_hr_flags (over_time, promotion_last_5_years)
SELECT DISTINCT over_time, promotion_last_5_years FROM staging_hr_data;

-- ==========================================
-- 4. POPULATE FACT TABLE WITH JOINS
-- ==========================================

INSERT INTO fact_employee_metrics (
    employee_id, department_id, survey_id, flag_id, 
    job_level, monthly_income, years_at_company, training_hours_last_year, attrition
)
SELECT 
    s.employee_id, 
    d.department_id,
    sp.survey_id,
    hf.flag_id,
    s.job_level, 
    s.monthly_income, 
    s.years_at_company, 
    s.training_hours_last_year, 
    s.attrition
FROM staging_hr_data s
-- Join dimensions to grab the auto-generated surrogate keys
JOIN dim_department d ON s.department = d.department_name
JOIN dim_survey_profile sp ON 
    s.job_satisfaction = sp.job_satisfaction AND 
    s.work_life_balance = sp.work_life_balance AND 
    s.performance_rating = sp.performance_rating
JOIN dim_hr_flags hf ON 
    s.over_time = hf.over_time AND 
    s.promotion_last_5_years = hf.promotion_last_5_years;

COMMIT;
