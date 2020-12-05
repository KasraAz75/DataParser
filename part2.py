from Parser import get_sorted_data
import json

"""
The data is now parsed as a JSON file that can be ingested
by a higher level entity. This issue now, however, is that we
wish to decrease reduce the amount of noise in the data. One method is
to apply a moving average filter. 

If `num_samples` is specified, get_sorted_data 
will apply a moving average filter that will take the average of the 
previous `num_samples` number of samples per header. If `num_samples` is not 
specified, then no moving average filter will be applied and the 
code will run as in part1.py. 

For example, in:
{
    "A1": [
            { "osTimeStamp": "1552242292.1146932", "value": 997 },
            { "osTimeStamp": "1552242292.1148102", "value": 997 },
            { "osTimeStamp": "1552242296.999962", "value": 995 },
            { "osTimeStamp": "1552242297.000105", "value": 995 },
            { "osTimeStamp": "1552242302.0143418", "value": 990 },
            { "osTimeStamp": "1552242302.014453", "value": 990 }
        ],
    "A2": [
            { "osTimeStamp": "1552242292.1153128", "value": 3602 },
            { "osTimeStamp": "1552242292.115364", "value": 3602 },
            { "osTimeStamp": "1552242297.0008519", "value": 3602 },
            { "osTimeStamp": "1552242297.000939", "value": 3602 },
            { "osTimeStamp": "1552242302.015125", "value": 3602 },
            { "osTimeStamp": "1552242302.015239", "value": 3602 },
            { "osTimeStamp": "1552242307.015094", "value": 3602 },
            { "osTimeStamp": "1552242307.0151591", "value": 3602 },
            { "osTimeStamp": "1552242311.983746", "value": 3603 }
        ]
}

If `num_samples` is given a value of '3' then a moving average filter
of length 3 will be applied to the "value" fields under A1 and A2 separately
"""

if __name__ == '__main__':
    input_filename = input('Enter the relative path of the file to parse: ')
    output_filename = input('Enter the relative path of the output file: ')

    # Sort the input data
    response = get_sorted_data(input_filename, num_samples=7)

    # Writing a JSON file with the new data
    with open(output_filename, 'w') as f:
        json.dump(response, f)
