#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from enum import Enum


class IndexType(Enum):
    # Primary index type.
    PRIMARY = 0
    # Normal index type.
    NORMAL = 1
    # Unique index type.
    UNIQUE = 2
    # Full text index type.
    FULL_TEXT = 3
