# -*- coding: utf-8 -*-
#
# Copyright (c) 2022, Globex Corporation
# All rights reserved.
import random
import secrets

def generate(
    client=None,
    input_data=None,
    progress_callback=None,
    renderer_type='csv',
    extra_context_callback=None,
):
    max_rows = int(input_data.get('size', 100000000000000))
    for i in range(max_rows):
        result = [i]
        result.extend([
            secrets.token_hex(64) for _ in range(150)
        ])
        yield result
        progress_callback(i, max_rows)
