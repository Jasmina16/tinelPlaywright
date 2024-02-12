1. Download and Install Python https://www.python.org/downloads/
2. Install pytest from CLI: pip install -U pytest
3. Install Playwright Pytest plugin from CLI: pip install pytest-playwright
4. Install the required browsers from CLI: playwright install
5. Fetch code from Github: git clone https://github.com/Jasmina16/tinelPlaywright
6. Position into ...\tinelPlaywright\src
7. Install plugins for html report:
   pip install pytest-reporter-html1
   pip install pytest-rerunfailures
   pip install pytest-metadata
   pip install pytest-xdist
8. Run test cases:   python -m pytest test/ --template=html1/index.html --report=TinelReport.html
9. Check generated html report in src/ folder