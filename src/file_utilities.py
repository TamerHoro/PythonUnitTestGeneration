import os
import json


# Parses metadata from a file and returns it in a dictionary
def parse_metadata(filename):
    # Does the file exist?
    if not os.path.isfile(filename):
        raise FileNotFoundError("Metadata JSON not found.")

    with open(filename, "r") as file:
        data = file.read()

    file.close()

    metadata = json.loads(data)

    return metadata


# Prints genotype representation to a file (pytest code)
def write_to_file(metadata, test_suite, algorithm=""):
    outfile = metadata["location"] + "test_" + metadata["file"] +"_"+ algorithm + ".py"
    f = open(outfile, "w+")  # Overwrites the old file with this name w+ = Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
    f.write("import " + metadata["file"] + "\nimport pytest\n")

    for test in range(len(test_suite)):
        test_case = test_suite[test]
        f.write("\n\ndef test_%d():\n" % test)

        # Initialize the constructor
        parameters = test_case[0][1]

        if len(parameters)==0 :
            init_string = "\tcut = " + metadata["file"] + "." + metadata[
            "class"] + "("
        else:
            init_string = "\tcut = " + metadata["file"] + "." + metadata[
                "class"] + "(" + str(parameters[0])
        for parameter in range(1, len(parameters)):
            init_string = init_string + "," + str(parameters[parameter])

        init_string += ")\n"

        f.write(init_string)

        # Print each test step

        for action in range(1, len(test_case)):
            name = metadata["actions"][test_case[action][0]]["name"]
            parameters = test_case[action][1]
            action_type = metadata["actions"][test_case[action][0]]["type"]
            returnable = ""
            if "return" in metadata["actions"][test_case[action][0]]:
                returnable = metadata["actions"][test_case[action][0]]["return"]

            out_string = ""

            if action_type == "assign":
                out_string = "\tcut." + name + " = " + str(parameters[0]) + "\n"
            elif action_type == "method":
                if returnable  == "true":
                    out_string += "\tresult = "  
            
                if parameters:                    
                    out_string += "\tcut." + name + "(" + str(parameters[0])
                    for parameter in range(1, len(parameters)):
                        out_string = out_string + "," + str(parameters[parameter])
                    out_string += ")\n"                    
                else:
                    out_string = "\tcut." + name + "()\n"
            
            f.write(out_string)

    f.close()
