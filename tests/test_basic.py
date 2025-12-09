from scantool import run_scan


def test_import():
    # Test if run_scan is callable
    assert callable(run_scan)


def test_scan_localhost():
    # Test scan on localhost (should return a dict)
    result = run_scan("127.0.0.1", "-F")
    assert isinstance(result, dict)
