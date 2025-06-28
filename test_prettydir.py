import re
import pandas
import pytest
import prettydir

def test_get_module():
    with pytest.raises(ModuleNotFoundError) as module:
        prettydir.get_module("something_something")
    
    assert prettydir.get_module("re") is re

    with pytest.raises(AssertionError) as assertion:
        assert prettydir.get_module("pandas") is re