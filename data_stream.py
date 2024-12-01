class DataStream:
    def __init__(self):
        # Dictionary to track the most recent timestamp of each string
        self.last_printed = dict()

    def should_output_data_str(self, timestamp: int, data_string: str) -> bool:
        """
        Determines whether a string should be printed based on the rule:
        - A string can only be printed if it has not been printed in the last 5 seconds.
        - Always updates the timestamp for the given string, whether it is printed or not.

        Args:
        - timestamp (int): The current timestamp when the string arrives.
        - data_string (str): The string to evaluate.

        Returns:
        - bool: True if the string can be printed; False otherwise.
        """
        # Check if the string is new or enough time has passed since it was last printed

        if data_string not in self.last_printed or timestamp - self.last_printed[data_string] >= 5:
            self.last_printed[data_string] = timestamp  # Update the timestamp
            return True
        else:
            self.last_printed[data_string] = timestamp  # Update the timestamp
            return False

# Test the functionality


output=[]
data_stream = DataStream()
output.append(data_stream.should_output_data_str(timestamp=0, data_string="hello"))
output.append(data_stream.should_output_data_str(timestamp=1, data_string="world"))
output.append(data_stream.should_output_data_str(timestamp=6, data_string="hello"))
output.append(data_stream.should_output_data_str(timestamp=7, data_string="hello"))
output.append(data_stream.should_output_data_str(timestamp=8, data_string="world"))

# Print results
print(output)  # Expected output: [True, True, True, False, True]
