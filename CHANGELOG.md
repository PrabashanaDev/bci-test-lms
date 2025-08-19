# Changelog

All notable changes to this project are documented in this file.

This project follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) guidelines and adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]
- Placeholder for upcoming features and improvements.

## [3.0.0-pre] - 2025-08-19
### Added
- Introduced `Student`, `Course`, and `Employee` class modules with methods for average and salary calculations.
- Implemented `Degree`, `Diploma`, and `Certificate` subclasses in `course.py`, each with specialized average logic.
- Added `Academic` and `NonAcademic` subclasses in `employee.py` with salary calculation functionality.
- Separated logic into modular files: `student.py`, `course.py`, `employee.py`, `findaverage.py`, `findSalary.py`.
- Wrapped demo/test logic in `if __name__ == "__main__":` to prevent unintended execution when importing modules.
- Prepared structured outputs in `findaverage.py` and `findSalary.py` to match assignment requirements.

## [2.0.0] - 2025
### Changed
- Refactored project to split classes into separate files for better modularity.
- Improved readability and maintenance by applying OOP principles across modules.

## [1.0.0] - 2025
### Added
- Initial project setup.
- Basic class structures and simple functions for testing assignment logic.
