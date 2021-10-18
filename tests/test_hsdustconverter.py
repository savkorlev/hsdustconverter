#!/usr/bin/env python

"""Tests for `hsdustconverter` package."""

import pytest


from hsdustconverter import hsdustconverter


def test_content():
    expectedCommons = 100
    expectedRares = 200
    expectedEpics = 300
    expectedLegendaries = 400
    observedCommons = hsdustconverter.convertCommons(20)
    observedRares = hsdustconverter.convertRares(10)
    observedEpics = hsdustconverter.convertEpics(3)
    observedLegendaries = hsdustconverter.convertLegendaries(1)

    assert expectedCommons == observedCommons
    assert expectedRares == observedRares
    assert expectedEpics == observedEpics
    assert expectedLegendaries == observedLegendaries
