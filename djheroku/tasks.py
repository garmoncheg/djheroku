from celery import task


@task()
def echoe():
    """
    A simple task that fetches the provided URL and returns a tuple
    with the HTTP status code and binary response body (if any)
    """
    print('Hello World!')