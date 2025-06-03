#!/usr/bin/env python3
import os
import sys
from collections import defaultdict

def count_files_in_directory(directory_path):
    """
    Count files in the given directory and its subdirectories.
    Returns a dictionary with directory paths as keys and file counts as values.
    """
    if not os.path.exists(directory_path):
        print(f"Error: The path '{directory_path}' does not exist.")
        sys.exit(1)
    
    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' is not a directory.")
        sys.exit(1)
    
    file_counts = defaultdict(int)
    
    # Walk through the directory tree
    for root, dirs, files in os.walk(directory_path):
        # Count files in current directory
        file_counts[root] = len(files)
    
    return file_counts

def display_file_counts(file_counts):
    """Display the file counts in a readable format."""
    print("\nFile Count Summary:")
    print("-" * 80)
    
    # Calculate total files
    total_files = sum(file_counts.values())
    
    # Print counts for each directory
    for directory, count in sorted(file_counts.items()):
        print(f"{directory}: {count} file(s)")
    
    print("-" * 80)
    print(f"Total directories: {len(file_counts)}")
    print(f"Total files: {total_files}")

def main():
    # Check if directory path is provided as command-line argument
    if len(sys.argv) != 2:
        print("Usage: python file_counter.py <directory_path>")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    
    # Get absolute path for better readability
    directory_path = os.path.abspath(directory_path)
    
    print(f"Counting files in: {directory_path}")
    
    # Count files
    file_counts = count_files_in_directory(directory_path)
    
    # Display results
    display_file_counts(file_counts)

if __name__ == "__main__":
    main() 
