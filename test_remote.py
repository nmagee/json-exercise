import remote

def test_remote_api():
    status_code = remote.remote_api()
    assert status_code == 200