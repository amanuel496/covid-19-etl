# COVID-19 ETL Pipeline

The COVID-19 ETL (Extract, Transform, Load) project is a Python-based pipeline designed to extract COVID-19 related data from multiple sources, transform it for analytical purposes, and load it into a structured data storage system. This project aims to facilitate efficient data processing for monitoring and analyzing the impact of COVID-19 globally.

## Features

- **Data Extraction**: Collects COVID-19 case statistics, vaccination data, and testing rates from various APIs and online sources.
- **Data Transformation**: Cleans, formats, and normalizes raw data for consistency and accuracy.
- **Data Loading**: Stores the processed data into a relational database or data warehouse for further analysis.
- **Automated Scheduling**: Supports automation via cron jobs or Apache Airflow for scheduled data updates.
- **Visualization Support**: Provides processed data in formats that can be easily integrated with visualization tools such as Tableau or Power BI.

## Project Structure

- `extract.py`: Handles the extraction of data from external APIs and CSV sources.
- `transform.py`: Cleans and normalizes extracted data for consistency and accuracy.
- `load.py`: Loads the processed data into a database or storage system.
- `config.py`: Stores configuration settings such as API keys and database credentials.
- `main.py`: The main script orchestrating the ETL pipeline execution.

## Setup and Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/amanuel496/covid-19-etl.git
   ```

2. **Install Dependencies**:

   Navigate to the project directory and install the required packages:

   ```bash
   cd covid-19-etl
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:

   Create a `.env` file in the project root directory and add the necessary API keys and database credentials:

   ```env
   COVID_API_KEY=your_api_key_here
   DATABASE_URL=your_database_connection_string_here
   ```

4. **Run the ETL Pipeline**:

   Execute the main script to start the ETL process:

   ```bash
   python main.py
   ```

## Usage

- **Modify Data Sources**: Update `extract.py` to include additional APIs or data sources.
- **Customize Data Transformations**: Modify `transform.py` to apply specific cleaning and processing rules.
- **Change Storage Destination**: Update `load.py` to load data into different databases or warehouses.
- **Automate Execution**: Use cron jobs or Airflow to schedule the ETL process at desired intervals.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request with enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

*Note: Ensure compliance with API usage policies and data privacy regulations when handling COVID-19 data.*

