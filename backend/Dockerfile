FROM python:3.10-slim

WORKDIR /app

# system deps
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# ===== INSTALL PYTHON LIBS (CACHE LAYER QUAN TRỌNG) =====
COPY requirements.txt .

RUN pip install -U pip setuptools wheel && \
    pip install --prefer-binary -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

# ===== INSTALL ARGOS MODELS =====
COPY install_languages.py .
RUN python install_languages.py

# ===== COPY SOURCE CODE LAST =====
COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
