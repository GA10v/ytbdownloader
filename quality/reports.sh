#!/bin/bash
echo "Cleanup Coverage folder..."
rm -rf ./reports
rm .coverage
echo "Installing Dependencies..."
pip3 install -r ./requirements/requirements-test.txt
echo "Running Tests..."
pytest --junitxml=reports/junit/junit.xml --html=reports/junit/report.html
echo "Generating Test badge..."
genbadge tests -o ./reports/junit/junit-badge.svg
echo "Running Coverage..."
coverage run -m pytest -v ..
echo "Creating Coverage report..."
coverage report
echo "Creating XML-formatted Coverage report..."
coverage xml -o ./reports/coverage/coverage.xml
echo "Creating HTML-formatted Coverage report..."
coverage html -d ./reports/coverage/html
echo "Generating Coverage badge..."
genbadge coverage -o ./reports/coverage/coverage-badge.svg
