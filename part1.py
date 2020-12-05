from Parser import get_sorted_data
import json

"""
Goal is to parse the Data.txt in Sample_data folder so that
it can be ingested into some higher level tool that will synthesize relationships
based on the dataset. 

This higher level software will only accept JSON files in the following format:
{
    <HEADER_1> [
        {
            <OS_TIME_STAMP>: "string/float",
            <VALUE>: int
        },
        ... additional entries ...
    ]

    <HEADER_2> [
        {
            <OS_TIME_STAMP>: "string/float",
            <VALUE>: int
        },
        ... additional entries ...
    ]

    ... additional headers ...

}
Therefore for the file provided, your output file should be:

==== OutputFile.json ====
{
  "B1": [
    {
      "osTimeStamp": "1552242292.1146932",
      "value": 997
    },
    {
      "osTimeStamp": "1552242292.1148102",
      "value": 997
    },
    ... more entries ...
  ],
  "B2": [
    {
      "osTimeStamp": "1552242292.1153128",
      "value": 3602
    },
    ... more entries ...
  ],

  ... more headers ...
}

Requirements: 
    * The 2nd column of values in the data is sometimes prefixed with 'TS>'. This prefix is
        irrelevant and should not affect the grouping. Therefore an entry 'TS>B1' should be in the
        same group as 'B1'.

        For example: 
            1552242292.1146932 B1 997              
            1552242292.1148102 B1 997 

        Should be parsed as:
        "B1": [
            {
                "osTimeStamp": "1552242292.1146932",
                "value": 997
            },
            {
                "osTimeStamp": "1552242292.1148102",
                "value": 997
            }
        ]

    * any modification to Data.txt file is not permitted.
"""

if __name__ == '__main__':
    input_filename = input('Enter the relative path of the file to parse: ')
    output_filename = input('Enter the relative path of the output file: ')

    # Sort the input data
    response = get_sorted_data(input_filename)

    # Writing a JSON file with the new data
    with open(output_filename, 'w') as f:
        json.dump(response, f)
