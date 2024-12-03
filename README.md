
# 🚀 Cryptocurrency Market  Tracker

## 🎯 Project Purpose

In the volatile world of cryptocurrency, having timely and accurate market information is crucial. This project aims to:
- Democratize cryptocurrency market data access
- Provide instant market 
- Support informed investment decision-making
- Offer a robust, extensible market tracking solution

## 🌟 Key Features


### 1. Live Crypto Data Sheet
**Purpose**: Raw Market Information
- Contains complete data for top 50 cryptocurrencies
- Columns include:
  - Cryptocurrency Name
  - Symbol
  - Current Price
  - Market Capitalization
  - Trading Volume
  - 24-hour Price Change

### 2. Top 5 Cryptocurrencies Sheet
**Purpose**: Market Leaders Snapshot
- Displays top 5 cryptocurrencies by market capitalization
- Detailed metrics for leading cryptocurrencies
- Helps quickly identify market dominance

### 3. Market Summary Sheet
**Purpose**: Comprehensive Market Overview
- Timestamp of data collection
- Total cryptocurrencies tracked
- Average cryptocurrency price
- Total market capitalization
- Total 24-hour trading volume

### 4. Performance Highlights Sheet
**Purpose**: Cryptocurrency Performance Analysis
- Best performing cryptocurrency
- Highest 24-hour price change
- Worst performing cryptocurrency
- Lowest 24-hour price change

## 📊 Alternative Implementation Approaches

### 1. Excel-Based Tracking (Current Implementation)
- Local file-based tracking
- No additional infrastructure cost
- Easy to set up and use
- Limited real-time collaboration

### 2. Google Sheets Live Tracking (Premium Approach)
#### Features
- Real-time collaborative updates
- Cloud-based storage
- Multiple user access
- Advanced sharing capabilities

#### Implementation Requirements
- Google Cloud Premium Account
- Google Sheets API
- Additional authentication setup
- Potential cost implications

#### Code Modification Needed
```python
# Pseudo-code for Google Sheets integration
from google.oauth2 import service_account
import gspread

def update_google_sheet(data):
    # Authenticate and connect to Google Sheets
    credentials = service_account.Credentials.from_service_account_file(
        'path/to/credentials.json',
        scopes=['https://spreadsheets.google.com/feeds']
    )
    client = gspread.authorize(credentials)
    
    # Update specific sheet with cryptocurrency data
    sheet = client.open('Crypto Tracker').worksheet('Live Data')
    sheet.update('A2:F51', data)  # Update range with new data
```

### 3. Database-Driven Approach
- PostgreSQL/MongoDB backend
- Historical data retention
- Advanced querying capabilities
- Scalable infrastructure

## 🗂️ Project Structure

```
cryptocurrency-tracker/
│
├── main.py               # Primary execution script
├── api.py                # API data retrieval module
├── analysis.py           # Data analysis and processing
├── excel_writer.py       # Excel report generation
├── logger.py             # Logging configuration
│
├── logs/                 # Logging directory
│   └── crypto_tracker_*.log
│
├── crypto_tracker.xlsx   # Generated Excel report with 4 sheets
│   ├── Live Crypto Data
│   ├── Top 5 Cryptos
│   ├── Market Summary
│   └── Performance Highlights
│
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```


## 🛠 Technical Stack

- **Language**: Python 3.8+
- **Data Processing**: Pandas
- **API Integration**: Requests
- **Reporting**: OpenPyXL
- **Logging**: Python's logging module

## 🚀 Local Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Stable internet connection

### Installation Steps
```bash
# Clone repository
git clone https://github.com/yourusername/cryptocurrency-tracker.git

# Navigate to project directory
cd cryptocurrency-tracker

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Unix/macOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run the tracker
python main.py
```

## 🔍 Logging Strategy

### Purpose of Logging
- Debugging and error tracking
- Performance monitoring
- Audit trail maintenance
- Operational transparency

### Log File Characteristics
- Timestamped filenames
- Multi-level logging (INFO, WARNING, ERROR)
- Detailed execution context
- Storage in dedicated `logs/` directory
