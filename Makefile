install:
	pip install --upgrade pip
	pip install -r requirements.txt

test:
	pytest test_greedy_coin.py