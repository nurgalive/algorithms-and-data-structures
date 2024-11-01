# Run using this command python3 -m pytest

from simple_hashmap import Hashmap
import sys
from pathlib import Path
sys.path.append(str(Path(sys.argv[0]).resolve().parent.parent))

def test_should_create_hashmap():
    assert Hashmap(size=10) is not None

def test_should_report_capacity():
    assert len(Hashmap(size=100)) == 100
