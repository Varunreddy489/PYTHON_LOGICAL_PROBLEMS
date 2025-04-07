import pytest
import src.regex as a

def test_email():
    email = 'varunsannapureddy@gmail.com'
    result = a.email(email)
    assert result is not None
