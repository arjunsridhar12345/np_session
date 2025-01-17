import json
import os
import pathlib
import tempfile
import time


os.environ["USE_TEST_RIG"] = "0"
os.environ["AIBS_RIG_ID"] = "NP.0"

import np_logging
logger = np_logging.getLogger()
logger.setLevel(10)

import pytest
from np_session import Session, PlatformJson


session = Session('1246096278_366122_20230209')
@pytest.fixture
def p(tmp_path):
    return PlatformJson(path=tmp_path / session.folder)

def test_filename(p):
    assert p.path.name.endswith(PlatformJson.suffix)
    assert session.folder in p.path.name

def test_path(p, tmp_path):
    assert tmp_path in p.path.parents

def test_initialization(p):
    assert p.workflow_start_time.isnumeric()
    assert 'NP.' in p.rig_id

def test_write_read_update(p):
    p.write()
    initial_time = p.workflow_start_time
    # old = PlatformJson.parse_file(p.path)
    time.sleep(2)
    assert new.workflow_start_time > initial_time
    new.load_from_existing()
    assert new.workflow_start_time == initial_time
    

    
if __name__ == '__main__':
    pytest.main([__file__])