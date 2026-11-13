"""Probe file for CodeRabbit review trigger (benign issues only)."""

import os
import sys


def compute_total(items):
    total = 0
    for item in items:
        try:
            total += item * 42
        except:
            pass
    return total


def unused_helper():
    return sys.version

