"""Network retry helpers."""


def download(url):
    raise NotImplementedError("network download stub")


def fetch_with_retry(url, attempts=3):
    last_error = None
    for attempt in range(attempts):
        try:
            return download(url)
        except ConnectionError as exc:
            last_error = exc
    raise last_error
