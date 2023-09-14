import re

class ReferenceSorter:
    """
    A class for organizing and alphabetically sorting references according to first Author's name.
    """

    def __init__(self, input_file:str, output_file) -> None:
        """
        Initialize the arrange_reference object with input and output file paths.
        
        Args:
            input_file (str): Path to the input file containing references.
            output_file (str): Path to the output file to write sorted references.
        """
        self.input_file = input_file
        self.output_file = output_file
        
    def do_the_job(self):
        """
        Perform the reference sorting and writing.
        """
        self.reference_list = []
        try:
            with open(self.input_file, "r", encoding="utf-8") as fhand:
                flines = fhand.readlines()
                self.fh = [item for item in flines if item != "\n"]
                for line in self.fh:
                    match_cond = re.match(r"^\d+\.", line)
                    if match_cond:
                        strip_line = line[len(match_cond.group(0)):]
                        words= strip_line.strip("\t ")
                        self.reference_list.append(words)
                        
            self.reference_list.sort()
        except FileNotFoundError:
            print(f"Error: Input file '{self.input_file}' not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        
        with open(self.output_file, "w", encoding="utf-8") as realdeal:
            for references in self.reference_list:
                realdeal.write(references + "\n")
                
    def job_result_info(self):
        """
        Print information about the job results.
        """
        print(f"NUmber of Non-white space Character before parsing is {len(self.fh)}")
        print(f"NUmber of refrences after parsing is {len(self.reference_list)}")
        print("Status: Success sire")
        
            
        


