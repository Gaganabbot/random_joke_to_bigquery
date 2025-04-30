<!-- Badges -->
[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/)  
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](#)  

## Overview

A lightweight Python pipeline that **fetches random jokes** from a free API, **parses** them into a pandas DataFrame, and (Part 2) **loads** them into BigQuery on a schedule. Perfect for beginner data engineers learning API extraction, DataFrame handling, and cloud ingestion. :contentReference[oaicite:6]{index=6}

## Features

- Fetches a new joke every run via HTTP GET :contentReference[oaicite:7]{index=7}  
- Parses JSON into a pandas DataFrame with timestamp :contentReference[oaicite:8]{index=8}  
- (Part 2) Authenticates and loads data into a partitioned BigQuery table  
- Easily swap in other free APIs (e.g., icanhazdadjoke, ChuckNorris) :contentReference[oaicite:9]{index=9}  

## Tech Stack

| Component            | Technology           |
| -------------------- | -------------------- |
| Language             | Python 3.7+          |
| DataFrame Library    | pandas               |
| HTTP Client          | requests             |
| Cloud Ingestion (Pt 2)| Google BigQuery      |
| Scheduler            | cron / Task Scheduler |

## Demo

![Output Sample](https://raw.githubusercontent.com/<your-username>/random_joke_to_bigquery/main/demo.png)  
*DataFrame printed with ID, type, setup, punchline, and extraction timestamp.* :contentReference[oaicite:10]{index=10}

## Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/<your-username>/random_joke_to_bigquery.git
   cd random_joke_to_bigquery
   ``` :contentReference[oaicite:11]{index=11}  
2. **Create & activate venv**  
   ```bash
   python -m venv env
   # macOS/Linux
   source env/bin/activate  
   # Windows PowerShell
   .\env\Scripts\Activate.ps1  
   ``` :contentReference[oaicite:12]{index=12}  
3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ``` :contentReference[oaicite:13]{index=13}  

## Usage

Run once to fetch and display a joke:
```bash
python main.py
