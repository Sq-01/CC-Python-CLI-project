# Currency Conversion CLI

This is a command-line interface (CLI) application for working with currency rates and performing currency conversions.

## Description
The Currency Conversion CLI is a versatile tool that allows users to interact with currency rates, perform currency conversions, and manage a local database to store conversion rates. This application is built using Python and several libraries, including Click, Requests, and SQLAlchemy.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Database](#database)

## Features

- **List Supported Currencies**: Users can list the supported currencies for conversion.
- **Set Default Currency**: Allows users to set a default currency for conversions.
- **Display Currency Rates**: Users can retrieve and display the exchange rate for a specific currency.
- **Convert a Currency Amount to Another Currency**: The CLI enables currency conversion between two currencies. A user can convert a specified amount from one currency to another.

## Requirements

To use this CLI application, you need the following requirements:

- Python 
- Pipenv
- Internet connection (for fetching currency rates)

## Installation

1. **Clone this repository to your local machine**:

   ```shell
   git clone git@github.com:Sq-01/CC-Python-CLI-project.git

2. **Navigate to the project directory**:
   ```shell
   cd CC-Python-CLI-project

3. **Install the required dependencies using Pipenv**:
   ```shell
   pipenv install

4. **Activate the virtual environment**:
   ```shell
   pipenv shell

## Usage

- List Supported Currencies
   ```shell
   cli currencies

- Set Default Currency
   ```shell
   cli default CURRENCY_CODE

- Display Currency Rate
   ```shell
   cli rate CURRENCY_CODE
   
- Convert Currency
   ```shell
   cli convert AMOUNT FROM_CURRENCY TO_CURRENCY

## Database
The Currency Conversion CLI stores currency exchange rates in a local SQLite database. The database file is named currency_rates.db and is located in the main directory.

You can find and manage the database in the same directory where you cloned the repository.

Enjoy using the Currency Conversion CLI for all your currency rate-related tasks!
