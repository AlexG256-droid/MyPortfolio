# Imports the built-in os.path module
import os.path

# Defines the read_e_file function
def read_e_file(emoji_file_name):
    """
    Function read_e_file
    Takes one parameter: The name of the emoji file
    This function assigns each word and emojis from the emoji file to each
    language in a group of lisis which will then be assigned as values to a
    dictionary called emojis_dict
    """
    # Try/except block
    try:
        # Reads the emoji file as e_file
        fullpath = os.path.join(os.path.dirname(__file__), emoji_file_name)
        with open(fullpath, mode="r", encoding="utf-8") as e_file:
            # Defines a new dictionary called emojis_dict
            emojis_dict = {}
            # Defines some empty lists
            new_list_words = []
            new_list_emojis_w = []
            new_list_emojis_k = []
            everything = []
            # Iterates through the emoji file
            for line in e_file:
                # Strips out any blank spaces and replaces them with commas
                new_emojis = line.split()
                everything.append(line.split())
                # Updates the lists with words and their corresponding emojis
                english = new_emojis[0]
                western = new_emojis[1]
                kaomoji = new_emojis[2]
                emojis_dict[f"{everything[0][1].lower()}"] = new_list_words
                emojis_dict[f"{everything[0][1].lower()}"].append(english)
                emojis_dict[f"{everything[0][2].lower()}"] = new_list_emojis_w
                emojis_dict[f"{everything[0][2].lower()}"].append(western)
                emojis_dict[f"{everything[0][3].lower()}"] = new_list_emojis_k
                emojis_dict[f"{everything[0][3].lower()}"].append(kaomoji)
            # Removes the first words of each list
            new_list_words.remove(new_list_words[0])
            new_list_emojis_w.remove(new_list_emojis_w[0])
            new_list_emojis_k.remove(new_list_emojis_k[0])
            # Returns the updated list of words/emojis
            return emojis_dict

    # Lets user know if the file cannot be found
    except FileNotFoundError:
        print("Invalid file input. File must be found.")

    # Lets user know if the file cannot be read
    except OSError:
        print("Invalid input. File could not be read.")

# Defines the read_d_file function
def read_d_file(directives_file_name):
    """
    Function read_d_file
    Takes one parameter: The name of the directives file
    This function assigns each language from the directives file to another
    language or a file name to another file name in a group of dictionaries
    """
    # Try/except block
    try:
        # Reads the directory file as d_file
        path = os.path.join(os.path.dirname(__file__), directives_file_name)
        with open(path, mode="r", encoding="utf-8") as d_file:
            # Defines a new list called file_names_list
            file_names_list = []
            # Iterates through the directory file
            for task in d_file:
                # Strips out any blank spaces and replaces them with commas
                task_list = task.split()
                # Updates the list with languages and file names
                file_names_list.append(task_list)
            # Returns the new list
            return file_names_list

    # Lets user know if the file cannot be found
    except FileNotFoundError:
        print("Invalid file input. File must be found.")

    # Lets user know if the file cannot be read
    except OSError:
        print("Invalid input. File could not be read.")

# Defines the translate function
def translate(translate_from, translate_to, text, emoji_dict):
    """
    Function translate
    Takes four parameters:
    Three strings: The language to translate from (translate_from),
    the language to translate to (translate_to), and the text in a file (text)
    One dictionary: emoji_dict
    This function replaces a word or words with an emoji or emojis in the text
    or vice versa
    """
    # Try/except block
    try:
        if text:
            # Updates the translate lists
            from_list = emoji_dict[translate_from]
            to_list = emoji_dict[translate_to]
            # Iterates through the text
            for line in range(len(text)):
                # Iterates through the range of english_dict
                for i in range(len(from_list)):
                    # Iterates through every line
                    for j in range(len(text[line])):
                        # Changes every specific word or emoji
                        if text[line][j].lower() == from_list[i].lower():
                            text[line][j] = to_list[i]
                            # Makes sure that element is lowercase if word
                            # Source: GeeksforGeeks
                            if text[line][j].isalpha() is True:
                                text[line][j] = text[line][j].lower()
                # Joins the words together
                text[line] = " ".join(text[line])
            # Separates the lines and returns the text
            text = "\n".join(text)
            return text
    
    # Lets user know if the file cannot be found
    except FileNotFoundError:
        print("Invalid file input. File must be found.")

    # Lets user know if the file cannot be read
    except OSError:
        print("Invalid input. File could not be read.")

# Defines the batch_translate function
def batch_translate(emoji_file_name, directives_file_name):
    """
    Function batch_translate
    Takes two strings as parameters: The name of the emoji and directive files
    (emoji_file_name, directives_file_name)
    This function calls the first three functions and writes out the result
    for every file
    """
    # Try/except block
    try:
        # Calls the read_e_file function and also the read_d_file function
        # New variables are assigned
        emojis = read_e_file(emoji_file_name)
        directives = read_d_file(directives_file_name)
        # Iterates through the directives in the directives variable
        if directives:
            for dir in directives:
                # Defines outfile and infile
                outfile = dir[3]
                infile = dir[2]
                # Writes the new output files each as w_file
                with open(outfile, mode="w", encoding="utf-8") as w_file:
                    # Defines text (the third parameter)
                    text = read_d_file(dir[2])
                    # Calls the translation function/assigns it to a variable
                    conversion = f"{translate(dir[0], dir[1], text, emojis)}"
                    # Lets user know the files were processed
                    print(f"Processed {dir[2]} from {dir[0]} to {dir[1]}...")
                    # Writes out each file
                    # print(conversion)
                    w_file.write(conversion)
                    file_read = open(infile, mode="r", encoding="utf-8")
                    file_read.read()
            # Prints out output statement
            print("Finished processing.")

    # Lets user know if the file cannot be found
    except FileNotFoundError:
        print("Invalid file input. File must be found.")

    # Lets user know if the file cannot be read
    except OSError:
        print("Invalid input. File could not be read.")

def main():
    # Calls the batch_translate function (after the file is written and read)
    batch_translate("emojis.txt", "emoji_directives.txt")

if __name__ == "__main__":
    main()