#!/usr/bin/env python
"""Main module for AI Article Generator."""

import sys
import os
import argparse
from dotenv import load_dotenv
import google.generativeai as genai
from .crew import AI_Article_Generator

# Load environment variables
load_dotenv()

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="AI Article Generator")
    parser.add_argument("--article_topic", type=str, default="Artificial Intelligence in Healthcare",
                      help="Topic for the article to be generated")
    parser.add_argument("--vector_db_url", type=str, default="https://example-vector-db.com/api",
                      help="URL of the vector database for research")
    parser.add_argument("--article_sources", type=str, default="https://www.nature.com,https://scholar.google.com",
                      help="Comma-separated list of source URLs for research")
    
    return parser.parse_args()

def run():
    """
    Run the crew with custom inputs.
    """
    # Get command line arguments if available
    if len(sys.argv) > 1 and sys.argv[1] == "run":
        sys.argv.pop(1)  # Remove the "run" command to allow argparse to work
        args = parse_arguments()
        
        inputs = {
            'article_topic': args.article_topic,
            'vector_db_url': args.vector_db_url,
            'article_sources': args.article_sources
        }
    else:
        # Default inputs if not specified
        inputs = {
            'article_topic': 'Artificial Intelligence in Healthcare',
            'vector_db_url': 'https://example-vector-db.com/api',
            'article_sources': 'https://www.nature.com,https://scholar.google.com'
        }
    
    # Load user preferences
    try:
        with open('knowledge/user_preference.txt', 'r') as f:
            user_preferences = f.read()
    except FileNotFoundError:
        try:
            with open('AI_Article_Generator/knowledge/user_preference.txt', 'r') as f:
                user_preferences = f.read()
        except FileNotFoundError:
            user_preferences = "No user preferences found."
    
    # Add user preferences to inputs
    inputs['user_preferences'] = user_preferences
    
    # Initialize and run the crew
    crew_instance = AI_Article_Generator()
    result = crew_instance.crew().kickoff(inputs=inputs)
    
    # Save the output to a file
    with open(f"article_{inputs['article_topic'].replace(' ', '_')}.md", 'w') as f:
        f.write(result)
    
    print(f"Article generated and saved to article_{inputs['article_topic'].replace(' ', '_')}.md")
    
    return result


def train():
    """
    Train the crew for a given number of iterations.
    """
    args = parse_arguments()
    inputs = {
        'article_topic': args.article_topic,
        'vector_db_url': args.vector_db_url,
        'article_sources': args.article_sources
    }
    
    try:
        if len(sys.argv) < 4:
            print("Usage: main.py train <iterations> <filename>")
            return
        
        AI_Article_Generator().crew().train(
            n_iterations=int(sys.argv[2]), 
            filename=sys.argv[3], 
            inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        if len(sys.argv) < 3:
            print("Usage: main.py replay <task_id>")
            return
            
        AI_Article_Generator().crew().replay(task_id=sys.argv[2])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    args = parse_arguments()
    inputs = {
        'article_topic': args.article_topic,
        'vector_db_url': args.vector_db_url,
        'article_sources': args.article_sources
    }
    
    try:
        if len(sys.argv) < 4:
            print("Usage: main.py test <iterations> <model_name>")
            return
            
        AI_Article_Generator().crew().test(
            n_iterations=int(sys.argv[2]), 
            openai_model_name=sys.argv[3], 
            inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [<args>]")
        print("Available commands: run, train, replay, test")
        sys.exit(1)

    command = sys.argv[1]
    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)