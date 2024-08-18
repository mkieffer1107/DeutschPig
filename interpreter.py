# part of the PIG family of languages https://esolangs.org/wiki/Pig
import random
import sys

class SchweinError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        """Simulate a German pig that is dying"""
        return f"OINK! OINK! GRUUUNZZZZ... {self.message} 💀"

words = [
    "GRUNZ",
    "SCHWEINEHUND",
    "GERTENSCHLANK",
    "SCHROTT",
    "PLATZFRESSER",
    "AUSGEZEICHNET",
    "SCHLAMMSCHLACHT",
]

def handle_SCHWEIN(content: str) -> str:
    """Replaces all instances of 'SCHWEIN' in string with random German pig noise"""
    non_schwein = content.split("SCHWEIN")
    new_content = non_schwein[0]
    for substr in non_schwein[1:]:
        new_content += random.choice(words) + substr
    return new_content

def handle_file(filename: str):
    """If file exists, replace all instances of 'SCHWEIN' with a German pig noise"""
    with open(filename, "r") as f:
        content = f.read()
    if "SCHWEIN" in content:
        new_content = handle_SCHWEIN(content)
        with open(filename, "w") as f:
            f.write(new_content)
        print(f"File '{filename}' processed gut.")
    else:
        raise SchweinError("Kein 'SCHWEIN' found in der file.")

def handle_line(line: str):
    """
    Creates a new file by processing as line as follows:
      line: {filename}SCHWEIN{file content}
    where SCHWEIN is the first instance of the phrase in the line
    """
    if "SCHWEIN" in line:
        # only split at the first instance of SCHWEIN
        parts = line.split("SCHWEIN", 1) 
        if len(parts) == 2:
            filename = parts[0].strip()
            # replace all other instances of SCHWEIN with a random word
            file_content = handle_SCHWEIN(parts[1].strip())
            with open(f"{filename}.txt", "w") as f:
                f.write(file_content)
            print(f"File '{filename}.txt' created with content: {file_content}")
        else:
            raise SchweinError("Falsch SCHWEIN zyntax.")
    else:
        raise SchweinError("Kein 'SCHWEIN' keyword found in der input.")
    
if __name__ == "__main__":
    print("Willkommen in DeutschPig")
    if len(sys.argv) > 1:
        # process a file
        filename = sys.argv[1]
        try:
            handle_file(filename)
        except FileNotFoundError:
            print(f"File '{filename}' nicht gefunden.") 
        except SchweinError as e:
            print(f"SchweinError: {e}")
    else:
        # DeutschPIG cli
        end = False
        while not end:
            try:
                line = input("Schnüffel 🐽> ")
                if line.lower() == "exit" or line.lower() == "q":
                    end = True
                else:
                    handle_line(line)
            except SchweinError as e:
                print(f"SchweinError: {e}")
