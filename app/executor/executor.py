from concurrent.futures import ThreadPoolExecutor

# Global ThreadPoolExecutor instance
executor = ThreadPoolExecutor(max_workers=1)

def submit_task(task, *args, **kwargs):
    """Submit a function to be executed asynchronously."""
    return executor.submit(task, *args, **kwargs)

def shutdown_executor():
    """Shut down the executor gracefully."""
    executor.shutdown(wait=True)
