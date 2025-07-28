# Use NVIDIA PyTorch container as base (includes CUDA, cuDNN, PyTorch)
FROM nvcr.io/nvidia/pytorch:23.10-py3

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    ffmpeg \
    libsndfile1 \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy all project files
COPY . .

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Command to start Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
