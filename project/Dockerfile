# -----------------------------
# 1. Base Image
# -----------------------------
    FROM python:3.10-slim

    # -----------------------------
    # 2. Set working directory
    # -----------------------------
    WORKDIR /app
    
    # -----------------------------
    # 3. Install system dependencies (optional but recommended)
    # -----------------------------
    RUN apt-get update && apt-get install -y \
        build-essential \
        && rm -rf /var/lib/apt/lists/*
    
    # -----------------------------
    # 4. Copy requirements first (to enable Docker caching)
    # -----------------------------
    COPY requirements.txt .
    
    # -----------------------------
    # 5. Install Python dependencies
    # -----------------------------
    RUN pip install --no-cache-dir -r requirements.txt
    
    # -----------------------------
    # 6. Copy the entire project
    # -----------------------------
    COPY . .
    
    # -----------------------------
    # 7. Expose FastAPI port
    # -----------------------------
    EXPOSE 8000
    
    # -----------------------------
    # 8. Start FastAPI using Uvicorn
    # -----------------------------
    CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
    