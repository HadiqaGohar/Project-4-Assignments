# # # import random

# # # def build_markov_chain(text, order=2):
# # #     """Creates a Markov chain dictionary from the input text."""
# # #     words = text.split()
# # #     markov_chain = {}

# # #     for i in range(len(words) - order):
# # #         key = tuple(words[i:i+order])  # Create key (tuple of words)
# # #         next_word = words[i + order]  # Get next word
        
# # #         if key not in markov_chain:
# # #             markov_chain[key] = []
# # #         markov_chain[key].append(next_word)

# # #     return markov_chain

# # # def generate_text(chain, length=50, order=2):
# # #     """Generates text using a Markov chain."""
# # #     key = random.choice(list(chain.keys()))  # Choose a random starting point
# # #     generated_words = list(key)

# # #     for _ in range(length - order):
# # #         if key in chain:
# # #             next_word = random.choice(chain[key])
# # #             generated_words.append(next_word)
# # #             key = tuple(generated_words[-order:])  # Update key
# # #         else:
# # #             break  # Stop if we reach an unknown state

# # #     return " ".join(generated_words)

# # # # Sample input text (you can replace this with a song lyrics file)
# # # sample_text = """This is a simple example of a Markov Chain text generator. 
# # # Markov chains are used to model sequences of words based on probabilities."""

# # # # Build and use the Markov Chain
# # # chain = build_markov_chain(sample_text)
# # # generated_text = generate_text(chain, length=20)

# # # print("🔹 Generated Text:\n", generated_text)


import os

file_path = input("Please enter the path to your text file: ")

# Print the absolute path to confirm it's being interpreted correctly
print(f"Absolute path: {os.path.abspath(file_path)}")

try:
    with open(file_path, 'r') as file:
        text = file.read()
    print("File successfully opened!")
except FileNotFoundError:
    print(f"Error: The file at the provided path could not be found.")
except Exception as e:
    print(f"An error occurred: {e}")
