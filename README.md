# Netflix EDA Using Apache Spark

This project demonstrates the process of performing Exploratory Data Analysis (EDA) on the Netflix dataset using Apache Spark. The dataset contains information about movies and TV shows available on Netflix, such as show ID, title, director, cast, release year, rating, and more.

## Project Overview

In this project, I used Apache Spark running in a Docker container to analyze the dataset. I performed basic EDA tasks like checking the dataset info, handling missing values, and exploring trends like the distribution of genres and release years.

## Dataset

The dataset used for this analysis is `netflix_titles.csv`. It contains the following columns:
- `show_id`: Unique identifier for the show.
- `type`: Type of content (Movie/TV Show).
- `title`: Title of the show.
- `director`: Director(s) of the show.
- `cast`: Cast members.
- `country`: Country of origin.
- `date_added`: Date when the show was added to Netflix.
- `release_year`: Year the show was released.
- `rating`: Rating of the show.
- `duration`: Duration of the show (in minutes for movies).
- `listed_in`: Categories the show belongs to.
- `description`: A brief description of the show.

## Steps Performed

### 1. **Setting up Spark Environment in Docker**
   - Used a Docker container to set up Apache Spark and Python.
   - Mounted the working directory and copied the `netflix_titles.csv` into the container.

### 2. **Exploratory Data Analysis (EDA)**
   - **Data Loading**: Loaded the dataset into a Spark DataFrame.
   - **Dataset Info**: Checked the structure and summary of the dataset using Spark and Pandas.
   - **Missing Values**: Identified missing values in several columns (e.g., `director`, `cast`, `country`, etc.).
   - **Distribution Analysis**:
     - Analyzed the distribution of movies and TV shows by genre (`listed_in` column).
     - Analyzed the distribution of release years to see trends over time.

### 3. **Python Script: `netflix_eda.py`**
   - The script performed the following:
     - Loaded and displayed the dataset's info.
     - Cleaned the data by handling missing values.
     - Generated basic visualizations and statistics like genre distribution and release year distribution.

### 4. **Pushing the Project to GitHub**
   - Created a GitHub repository to store the project and dataset.
   - Initialized a Git repository inside the Docker container and committed the Python script and dataset.
   - Pushed the committed changes to GitHub using a Personal Access Token (PAT) for authentication.

### 5. **Issues Faced**
   - Encountered issues with GitHub authentication since password authentication is no longer supported. Resolved it by using a Personal Access Token (PAT) for Git operations.
   - The `git` tool was not initially installed in the Docker container, which required installation before proceeding with commits.

## How to Run the Project

### Prerequisites
- Docker installed on your machine.
- Apache Spark and Python set up in a Docker container.
- GitHub account for uploading the code.

### Steps to Run:
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/emsherry/spark-eda-netflix.git
