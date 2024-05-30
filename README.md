# Mini Search Engine

## Description

This project is a mini search engine designed to search for AI-related documents. It works by crawling information from various tech news websites, indexing the text and data using the TF-IDF function, and providing advanced search capabilities through the `txtai` library.

The search engine is not limited to the command line interface. A user-friendly frontend has been developed to provide a more interactive and accessible way to use the search engine. This allows users to easily search for and read the data without needing to interact with the CLI.

The goal of this project is to make it easier to find and access technical related news and information from various sources in one place.

## Installation

1. Clone the project from GitHub:

```
git clone https://github.com/dunliang0513/mini-search-engine.git
```

2. Navigate to the project directory:

```
cd mini-search-engine
```

3. Run the `start.sh` script to setup the environment and satrt the application:

```
./start.sh
```
This script installs the required Python packages, sets the necessary environment variables, and starts the application. If you encounter a permission error, make the script executable with 
```
chmod +x start.sh 
```
and try again step 3.
