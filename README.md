# Inflam
![Continuous Integration build in GitHub Actions](https://github.com/<your_github_username>/python-intermediate-inflammation/actions/workflows/main.yml/badge.svg?branch=main)
Inflam is a data management system written in Python that manages trial data used in clinical inflammation studies.

## Main features

Here are some key features of Inflam:

- Provide basic statistical analyses over clinical trial data.

- Work with trial data in Comma-Separated Value (CSV) format.

- Support inflammation data in JSON format.

- Generate plots of trial data.

- Extend analytical functions and views using a Model-View-Controller (MVC) architecture.

Prerequisites

Inflam requires Python 3 and the following packages:

- [NumPy](https://www.numpy.org/) - makes use of NumPy's statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) - uses Matplotlib to generate statistical plots.

The following packages are required for testing:

- [pytest](https://docs.pytest.org/en/stable/) - Inflam's unit tests are written using pytest
- [pytest-cov](https://pypi.org/project/pytest-cov/) - Adds test coverage stats to unit testing

## Installation

Clone the repository:

git clone git@github.com:francesca-riccio/python-intermediate-inflammation.git
cd python-intermediate-inflammation

Create and activate a Python virtual environment:

python3 -m venv venv
source venv/bin/activate

Install the project and its dependencies:

python3 -m pip install -e .

Basic usage

Run the application with a CSV file:

python3 inflammation-analysis.py data/inflammation-01.csv

Run the full data analysis:

python3 inflammation-analysis.py --full-data-analysis data/inflammation-01.csv

Display the command-line options:

python3 inflammation-analysis.py --help

Testing

Run the test suite using pytest:

python3 -m pytest tests/ -v

Generate a test coverage report:

python3 -m pytest tests/ --cov=inflammation



## Contributing

Contributions, bug reports and suggestions are welcome.

Please create a feature branch, add appropriate tests and submit a Pull Request for review.

## Licence

See LICENCE.md for licensing information.