"""
Testing for Hilbert transform method

Using the math relation a^2 / (a^2 + x^2) (Lorentz/Cauchy) has an 
analytical Hilbert transform: x^2 / (a^2 + x^2)
"""

import numpy as np
from numpy.testing import assert_array_almost_equal

from crikit.cri.algorithms.kk import hilbertfft


def test_pyfftw_hilbert_no_pad():
    x = np.linspace(-100, 100, 1000)
    y = 2/(2**2 + x**2)
    hilb_y = hilbertfft(y, pad_factor=0, use_pyfftw=True)
    hilb_y_analytical = x/(2**2 + x**2)
    assert_array_almost_equal(hilb_y_analytical, hilb_y, decimal=2)

def test_pyfftw_hilbert_pad():
    x = np.linspace(-100, 100, 1000)
    y = 2/(2**2 + x**2)
    hilb_y = hilbertfft(y, pad_factor=10, use_pyfftw=True)
    hilb_y_analytical = x/(2**2 + x**2)
    assert_array_almost_equal(hilb_y_analytical, hilb_y, decimal=4)

def test_hilbert_no_pad():
    x = np.linspace(-100, 100, 1000)
    y = 2/(2**2 + x**2)
    hilb_y = hilbertfft(y, pad_factor=0, use_pyfftw=False)
    hilb_y_analytical = x/(2**2 + x**2)
    assert_array_almost_equal(hilb_y_analytical, hilb_y, decimal=2)

def test_hilbert_pad():
    x = np.linspace(-100, 100, 1000)
    y = 2/(2**2 + x**2)
    hilb_y = hilbertfft(y, pad_factor=10, use_pyfftw=False)
    hilb_y_analytical = x/(2**2 + x**2)
    assert_array_almost_equal(hilb_y_analytical, hilb_y, decimal=4)
