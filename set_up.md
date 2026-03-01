================================================================
NLP SKILLS DEVELOPMENT PROGRAMME - ENVIRONMENT SETUP REFERENCE
================================================================

SET UP
------
conda create -n nlp-dev python=3.11 pandas matplotlib numpy scikit-learn -y
conda activate nlp-dev
pip install "numpy<2"
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
pip install jupyter jupyterlab
pip install transformers datasets tokenizers accelerate
pip install spacy nltk
python -m spacy download en_core_web_sm

SANITY CHECK (in Python)
------------------------
import torch, transformers, spacy, nltk
import pandas, matplotlib, numpy, sklearn
print(torch.cuda.is_available())
if torch.cuda.is_available():
    print(torch.cuda.get_device_name(0))    # NVIDIA GPU name
else:
    print("CUDA not available. Running on CPU.")
nlp = spacy.load("en_core_web_sm")
print(nlp("Hello NLP world."))
nltk.download('popular')

EXPORT ENVIRONMENT YAML
-----------------------
conda env export --no-builds > "C:\Users\UserPC\My Drive\research\nlp_learning\nlp-dev-environment.yml"

# To recreate environment on another machine:
conda env create -f nlp-dev-environment.yml

MAINTENANCE (run monthly or at start of each phase)
----------------------------------------------------
conda activate nlp-dev
pip check
conda update --all -y
pip list --outdated
pip install --upgrade transformers datasets tokenizers accelerate spacy
conda env export --no-builds > "C:\Users\UserPC\My Drive\research\nlp_learning\nlp-dev-environment.yml"

AT EACH COLAB SESSION (in Python)
----------------------------------
from google.colab import drive
drive.mount('/content/drive')
base_path = '/content/drive/MyDrive/research/nlp_learning'

SAVING EXAMPLE IN COLAB (in Python)
-------------------------------------
model.save_pretrained(f'{base_path}/models/my_model')

FOLDER STRUCTURE
----------------
nlp_learning/
├── SETUP.md
├── nlp-dev-environment.yml
├── notebooks/
├── models/
├── data/
└── outputs/

ENVIRONMENT NOTES
-----------------
- GPU:          NVIDIA GeForce 940MX (2GB VRAM)
- CUDA:         12.4
- Python:       3.11
- PyTorch:      installed via pip wheel (not conda) for CUDA support
- NumPy:        pinned to <2 for PyTorch compatibility
- Local use:    Weeks 1-5 (lighter tasks)
- Colab use:    Week 6 onwards (fine-tuning, larger models)
- Drive path:   C:\Users\UserPC\My Drive\research\nlp_learning
- Colab path:   /content/drive/MyDrive/research/nlp_learning
================================================================