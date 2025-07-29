# Crash Detection Tool

**A Python-based tool for extracting and classifying crash indicators from automotive log files.**

## 📖 Project Overview

- **Goal:** Analyze Aurix, ISOC/SAIL, and DLT logs to detect and report crash events.
- **Key Features:**
  - Modular log readers (text, DLT, etc.)
  - YAML-driven pattern engine
  - Structured output (CSV/JSON)
  - CI/CD with automated testing

## 🚧 Development Roadmap

| Phase                | Step                                               | Status   |
| -------------------- | -------------------------------------------------- | -------- |
| **Phase 0: Setup**   | Step 1: Environment Check                          | ✅ Done  |
|                      | Step 2: Git & Virtual Environment                  | ✅ Done  |
|                      | Step 3: Dependencies & Pre‑commit Hooks            | ✅ Done  |
|                      | Step 4: Project Structure & Initial Logging        | ✅ Done  |
|                      | Step 5: Sample Fixtures & RTM Skeleton             | ✅ Done  |
|                      | Step 6: CI Smoke Test                              | ✅ Done  |
| **Phase 1: Readers** | Step 1: BaseLogReader Interface                    | ✅ Done  |
|                      | Step 2: TextLogReader Implementation               | ✅ Done  |
|                      | **Step 3: Reader Factory (Coming Next)**           | ⏳ In Progress |
| **Phase 2+**         | Indicator Engine, Normalization, Reporting, etc.   | ⏳ Planned|

## ✅ Completed Steps

1. Verified Python 3.8+ and Git installation  
2. Initialized Git repo and Python venv  
3. Installed and pinned dependencies; set up pre‑commit hooks  
4. Created project folders (`src/`, `tests/`, `docs/`, `configs/`); configured Loguru  
5. Added sample log fixtures and RTM skeleton  
6. Added CI smoke test via GitHub Actions  
7. Defined `BaseLogReader` interface  
8. Implemented `TextLogReader`

## 🚀 Next Steps

- **Phase 1, Step 3: Reader Factory**  
  Build a factory function to select the correct reader based on file extension or magic number.

- **Phase 1, Step 4: DLT Reader**  
  Implement binary DLT log reader using `dlt-python`.

## 📄 How to Contribute

1. Fork the repo and create a feature branch.  
2. Write code and add tests under `tests/`.  
3. Ensure all pre‑commit hooks pass.  
4. Submit a pull request against `main`.

