
echo "[$(date)]: START"
echo "[$(date)]: Creating virtual environment with Python 3.8"
python -m venv ./env
echo "[$(date)]: Activate env"
source ./env
echo "[$(date)]: Installing dev requirements"
pip install -r requirements_dev.txt
echo "[$(date)]: END"

