# Food-Waste-Monitoring-Tool
**Offline command-line tool for tracking, analyzing, and reporting food waste patterns in low-resource institutional feeding environments.**

# Overview

The Food Waste Monitoring Tool is a lightweight, offline Python-based command-line application designed to track and analyze food waste generated in structured feeding environments such as NYSC camps, institutions, and community kitchens.

This tool was developed as part of a National Youth Service Corps (NYSC) community development initiative focused on reducing food waste, improving meal planning efficiency, and supporting sustainable resource use in line with the Sustainable Development Goals (SDG 12: Responsible Consumption and Production).

It enables simple data logging, waste pattern analysis, and report generation in offline environments where digital infrastructure may be limited.

# Problem Statement

Food waste in institutional feeding systems often occurs due to:

* Overproduction of meals
* Poor demand estimation
* Meal preference mismatch
* Service timing inefficiencies
* Portion control issues

However, most small-scale feeding operations lack structured systems to:

* Track food waste consistently
* Identify recurring waste patterns
* Understand root causes of waste
* Generate simple operational reports

This tool provides a basic, practical solution to support data-driven decision-making in food management.

# Features
# Data Logging

* Add new food waste records via CLI
* Record meal type, food item, quantity, and reason

# Data Analysis

* View total food waste
* Analyze waste by food type
* Analyze waste by meal type
* Analyze waste by reason category

# Reporting

* Generate structured text-based reports
* Save reports locally for documentation and review

---

# Project Structure

```
food-waste-monitoring-tool/
├── food_waste_monitor.py
├── data/
│   └── food_waste.csv
├── reports/
│   └── waste_report.txt
├── README.md
└── requirements.txt
```

---

# Data Format

The tool uses a CSV file (`data/food_waste.csv`) to store food waste records.

# Example:

```
date,meal_type,food_item,quantity_wasted_kg,reason,notes
2026-01-29,Dinner,Jollof Rice,3.0,Low turnout,Impromptu social night activities
2026-01-30,Lunch,Rice and Stew,2.8,Large portions,Overestimated attendance
```

---

### Field Descriptions:

* **date**: Date of waste occurrence
* **meal_type**: Meal category (Breakfast, Lunch, Dinner)
* **food_item**: Type of food served
* **quantity_wasted_kg**: Quantity of food wasted (in kilograms)
* **reason**: Primary reason for waste
* **notes**: Additional context or observation
  

# Installation

# Requirements

* Python 3.x installed
* No external libraries required

# Clone the repository

```bash
git clone <your-repo-link>
cd food-waste-monitoring-tool
```

---

# Usage

All commands are executed from the terminal inside the project directory.

# View total food waste

```bash
python food_waste_monitor.py --total
```

# Analyze waste by food type

```bash
python food_waste_monitor.py --by-food
```

# Analyze waste by meal type

```bash
python food_waste_monitor.py --by-meal
```

### Analyze waste by reason

```bash
python food_waste_monitor.py --by-reason
```

# Add a new record

```bash
python food_waste_monitor.py --add
```

# Generate report

```bash
python food_waste_monitor.py --report
```

# Example Workflow
1. Record daily food waste using the CLI
2. Periodically analyze waste patterns
3. Identify operational inefficiencies
4. Adjust meal planning and portion control strategies
5. Generate reports for documentation and review

# Use Case
This tool is designed for:
* NYSC CDS community development projects
* Institutional feeding programs
* Camp and hostel meal management systems
* Small-scale kitchen and catering operations
* Offline or low-connectivity environments

# Future Improvements
* Interactive menu-based interface
* Visual dashboards for waste trends
* Daily/weekly analytics summaries
* SMS-based reporting system for offline environments
* Integration with mobile data collection forms

# Author

Developed as part of a Community Development Service (CDS) initiative under the SDGs-focused Environmental and Food Systems Project during the NYSC Rivers State Orientation Camp 2026 Batch A1. The project focuses on improving food resource efficiency, reducing waste, and supporting sustainable institutional feeding systems in low-resource environments.

# License

This project is intended for educational and non-commercial use.


# About

Offline command-line tool for tracking, analyzing, and reporting food waste in structured feeding environments using Python and CSV-based storage.

