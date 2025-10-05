# minor_fus_mod.py
# Patch-like helper to integrate into gem5's MinorDefaultFUPool.py
# This file provides a snippet you can paste into MinorDefaultFUPool.py (or include in your own config)
# to pick FloatSimdFU (opLat, issueLat) configurations via an environment variable.
# Use in Ubuntu/WSL environment before runs: export GEM5_FLOATSIMD_CONFIG="op2_iss5"

import os

FLOATSIMD_CONFIGS = {
    "op1_iss6": (1, 6),
    "op2_iss5": (2, 5),
    "op3_iss4": (3, 4),
    "op4_iss3": (4, 3),
    "op5_iss2": (5, 2),
    "op6_iss1": (6, 1),
}

DEFAULT_FLOATSIMD_CONFIG_KEY = "op4_iss3"
_selected_key = os.environ.get("GEM5_FLOATSIMD_CONFIG", DEFAULT_FLOATSIMD_CONFIG_KEY)
_opLat, _issueLat = FLOATSIMD_CONFIGS.get(_selected_key, FLOATSIMD_CONFIGS[DEFAULT_FLOATSIMD_CONFIG_KEY])

# Example usage: paste the following where FloatSimdFU is constructed in MinorDefaultFUPool.py:
# FloatSimdFU = MinorFU(opLat=_opLat, issueLat=_issueLat, count=1)
