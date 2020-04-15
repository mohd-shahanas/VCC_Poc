"""Test Tickets."""
import pytest

from Vcc.Library.vcc_actions import VccActions


def test_login():
    """Test get ticket classes."""
    obj = VccActions()
    obj.user_login()
