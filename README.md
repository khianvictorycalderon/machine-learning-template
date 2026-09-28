# Machine Learning Template

### Prerequisites
- Python *(Recommended version: 3.12)*

### Setup :

1. Create your virtual environment by running `python -m venv venv`. *(You may use `py -3.12 -m venv venv` if you want to create a virtual environment with that specific version of python)*.
2. Activate your virtual environment with `.\venv\Scripts\activate` (for Windows).
3. Install all the necessary dependencies with `pip install -r requirements.txt`.
4. Run `python -m flask --app api.index run --debug`.

**NOTE**: Always run `python -m pip freeze > requirements.txt` or simply `pip freeze > requirements.txt` whenever installing a new package or library.