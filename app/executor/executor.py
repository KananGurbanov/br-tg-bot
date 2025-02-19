from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=1)

def submit_task(task, *args, **kwargs):
    return executor.submit(task, *args, **kwargs)

def shutdown_executor():
    executor.shutdown(wait=True)
