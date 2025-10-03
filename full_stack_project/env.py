import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
os.environ.setdefault('DATABASE_URL', 'postgresql://neondb_owner:npg_HVwn4IjR0uzo@ep-tiny-sky-agei7xbq.c-2.eu-central-1.aws.neon.tech/slash_goal_moan_300035')
os.environ.setdefault('SECRET_KEY', 'fg#^cghe)n$hehme29f95etffu-w)7$8&lz-(7d@1g_41y#mad')
os.environ.setdefault('DEBUG', 'True')
BASE_DIR = Path(__file__).resolve().parent.parent

