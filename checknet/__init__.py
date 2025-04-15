import socket

def is_connected(host="8.8.8.8", port=53, timeout=3):
    """
    Tests internet connectivity using a TCP socket.
    
    Args:
        host (str): IP address to test against (default: 8.8.8.8)
        port (int): TCP port to use (default: 53)
        timeout (int): Connection timeout in seconds

    Returns:
        bool: True if the connection is successful, False otherwise
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error:
        return False
