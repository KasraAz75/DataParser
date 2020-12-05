# Data Parser

Goal is to parse the Data.txt in Sample_data folder so that it can be ingested into some higher level tool that will synthesize relationships based on the dataset. This task includes two parts:

1. **Part1:** Returns a .json file with the following format;

```{
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
```

2. **Part2:** Receieves an input 'num_samples' and applies a moving average filter that will take the average of the previous `num_samples` number of samples per header. If `num_samples` is not  specified, then no moving average filter will be applied and the  code will run as in part1.py. 

## Dependencies
- [Pandas](https://pandas.pydata.org/)
- [json](https://docs.python.org/3/library/json.html)

## Sample Outputs

1. **Part1.py:**

```
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
```

2. **Part2.py:**

```
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
```

## Contact
If you want to contact me you can reach me at [kasra.azizbaigi@gmail.com](mailto:kasra.azizbaigi@gmail.com)

## License
This project uses the following license: [GNU General Public License v3.0](https://github.com/KasraAz75/LRUCache/blob/main/LICENSE).
