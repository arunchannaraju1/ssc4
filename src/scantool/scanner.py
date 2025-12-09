import nmap


def run_scan(target="127.0.0.1", args="-sV"):
    """
    Perform a basic Nmap scan on a target host.
    Args:
        target (str): IP or hostname to scan.
        args (str): Nmap command-line arguments.
    Returns:
        dict: Scan results returned by python-nmap.
    """
    nm = nmap.PortScanner()
    return nm.scan(target, arguments=args)
