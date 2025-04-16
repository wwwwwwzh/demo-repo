# main.py
import os
from utils.helpers import *

class DemoApp:
    """
    A class that encapsulates the main processing flow of the demo application.
    """
    def __init__(self, config):
        """
        Initialize the DemoApp with a given configuration.

        Args:
            config (dict): Configuration dictionary for the demo app.
        """
        self.config = config
        print(f"DemoApp initialized with config: {config}")

    def run_demo(self, input_path):
        """
        Run the full demo workflow using the provided input_path.
        
        Args:
            input_path (str): The path to the input file.
        """
        # Ensure the input is valid
        if validate_input(input_path):
            # Load data
            data = load_data(input_path)

            # Transform data
            transformed_data = transform_data(data)

            # Process data in batches
            processed_data = process_batch(
                transformed_data, 
                self.config["max_threads"]
            )

            # Save results
            output_path = f"{self.config['temp_dir']}/output.json"
            if save_results(processed_data, output_path):
                print("Results saved successfully!")

            # Display summary
            display_summary(processed_data)

            # Generate report
            report = generate_report(processed_data)
            print(f"Report generated: {report}")
        else:
            print("Invalid input. Exiting.")


def load_data(filepath):
    """
    Load data from the specified file path
    
    Args:
        filepath (str): Path to the data file
        
    Returns:
        dict: Loaded data
    """
    print(f"Loading data from {filepath}")
    # Simulate loading data
    return {"status": "success", "items": [1, 2, 3, 4, 5]}

def transform_data(data):
    """
    Transform the loaded data
    
    Args:
        data (dict): Data to transform
        
    Returns:
        dict: Transformed data
    """
    print("Transforming data...")
    # Apply some transformation
    result = {
        "status": data["status"],
        "items": [item * 2 for item in data["items"]],
        "timestamp": "2025-04-04"
    }
    return result

def save_results(data, output_path):
    """
    Save the results to the specified output path
    
    Args:
        data (dict): Data to save
        output_path (str): Path where to save the data
        
    Returns:
        bool: Success status
    """
    print(f"Saving results to {output_path}")
    # In a real scenario, this would write to a file
    return True

def display_summary(data):
    """
    Display a summary of the processed data
    
    Args:
        data (dict): Processed data
        
    Returns:
        None
    """
    print("\nSummary:")
    print(f"Status: {data['status']}")
    print(f"Items processed: {len(data['items'])}")
    print(f"Timestamp: {data['timestamp']}")
    
    # Get additional stats using the imported function
    formatted_data = format_data(data)
    print(f"Formatted data: {formatted_data}")

def setup_environment():
    """
    Set up the environment for the application
    
    Returns:
        dict: Environment configuration
    """
    print("Setting up environment...")
    return {
        "temp_dir": "/tmp/demo",
        "log_level": "INFO",
        "max_threads": 4
    }

def main():
    """
    Main entry point of the application
    """
    print("Starting demo application...")
    
    # Setup environment
    config = setup_environment()
    
    # Create the demo application object
    app = DemoApp(config)

    # Define input path
    input_path = "data/input.json"

    # Run the full workflow
    app.run_demo(input_path)
    
    print("Demo application completed.")

if __name__ == "__main__":
    main()
