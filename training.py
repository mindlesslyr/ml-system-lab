import argparse
from dataclasses import asdict
import json
from pathlib import Path
import sys

#neural network natin
import torch

ROOT = Path(__file__).resolve.parents[0]
sys.path.insert(0, str(ROOT / "src"))


