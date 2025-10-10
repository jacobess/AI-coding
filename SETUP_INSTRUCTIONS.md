# Python Environment Setup Instructions

## Option 1: Using venv (Recommended for beginners)

### Step 1: Create a Virtual Environment
```bash
# Navigate to your project directory
cd /Users/ernesto.ortega/Documents/Ernesto/Courses/Cursor/ParabolicShot

# Create a virtual environment named 'venv'
python3 -m venv venv
```

### Step 2: Activate the Virtual Environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
# Upgrade pip first
pip install --upgrade pip

# Install project dependencies
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python tiro_parabolico.py
```

### Step 5: Deactivate When Done
```bash
deactivate
```

---

## Option 2: Using conda (Recommended for data science)

### Step 1: Create a Conda Environment
```bash
# Navigate to your project directory
cd /Users/ernesto.ortega/Documents/Ernesto/Courses/Cursor/ParabolicShot

# Create a conda environment with Python 3.9
conda create -n tiro-parabolico python=3.9

# Activate the environment
conda activate tiro-parabolico
```

### Step 2: Install Dependencies
```bash
# Install matplotlib and numpy via conda (faster)
conda install matplotlib numpy

# Or install via pip
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
python tiro_parabolico.py
```

### Step 4: Deactivate When Done
```bash
conda deactivate
```

---

## Option 3: Using pipenv (Modern approach)

### Step 1: Install pipenv (if not already installed)
```bash
pip install pipenv
```

### Step 2: Create and Install Dependencies
```bash
# Navigate to your project directory
cd /Users/ernesto.ortega/Documents/Ernesto/Courses/Cursor/ParabolicShot

# Install dependencies and create Pipfile
pipenv install matplotlib numpy

# Or install from requirements.txt
pipenv install -r requirements.txt
```

### Step 3: Activate and Run
```bash
# Activate the virtual environment
pipenv shell

# Run the application
python tiro_parabolico.py

# Or run directly without activating
pipenv run python tiro_parabolico.py
```

---

## Quick Start (One-time setup)

If you just want to get started quickly:

```bash
# Navigate to project directory
cd /Users/ernesto.ortega/Documents/Ernesto/Courses/Cursor/ParabolicShot

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the application
python tiro_parabolico.py
```

---

## Troubleshooting

### If you get "command not found" errors:
- Make sure Python 3 is installed: `python3 --version`
- On some systems, use `python` instead of `python3`

### If matplotlib doesn't display graphs:
- On macOS, you might need: `pip install --upgrade matplotlib`
- On Linux, you might need: `sudo apt-get install python3-tk`

### If you get permission errors:
- Use `pip install --user -r requirements.txt` to install in user directory
- Or make sure you're in an activated virtual environment

### To check if everything is working:
```bash
# Check Python version
python --version

# Check installed packages
pip list

# Test matplotlib
python -c "import matplotlib; print('matplotlib OK')"
python -c "import numpy; print('numpy OK')"
```

---

## Project Structure After Setup

```
ParabolicShot/
├── venv/                    # Virtual environment (created by you)
├── tiro_parabolico.py      # Main application
├── requirements.txt        # Dependencies
├── README.md              # Documentation
├── SETUP_INSTRUCTIONS.md  # This file
└── Description de la aplicacion.txt
```

---

## Daily Usage

Once set up, your daily workflow is:

```bash
# 1. Navigate to project
cd /Users/ernesto.ortega/Documents/Ernesto/Courses/Cursor/ParabolicShot

# 2. Activate environment
source venv/bin/activate  # On macOS/Linux

# 3. Run the application
python tiro_parabolico.py

# 4. When done, deactivate
deactivate
```

---

## Why Use Virtual Environments?

- **Isolation**: Keeps project dependencies separate from system Python
- **Reproducibility**: Ensures consistent environment across different machines
- **Clean System**: Prevents conflicts between different projects
- **Easy Cleanup**: Can delete the entire environment if needed

Choose the method that works best for your setup!
