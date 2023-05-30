import sys
sys.path.insert(0, "../pages")

try:
    from adc_novo_jogo import *
except ImportError:
    print('No Import')