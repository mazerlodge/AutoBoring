# Not from AutoBor, just a test that came up while reviewing Airflow DAGs 

class MyContextManager:
    def __enter__(self):
        # Setup actions (e.g., acquire a resource)
        print("Entering the context")
        return self  # Optional: return a value to be used in the 'with' block

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Teardown actions (e.g., release a resource)
        print("Exiting the context")
        if exc_type:
            print(f"An exception of type {exc_type} occurred")
        # Return True to suppress the exception, or False (or None) to propagate it
        return False

    def do_something(self):
        print("Doing something within the context")

with MyContextManager() as context:
    context.do_something()
    # Raise an exception to test the __exit__ method
    # raise ValueError("Something went wrong")
    
	