install:
	pip install -r requirements.txt
train:
	python -m src.models.train
api:
	uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000
dash:
	streamlit run src/dashboard/app.py --server.port 8501
test:
	pytest tests/
lint:
	black src/ tests/ && flake8 src/ tests/