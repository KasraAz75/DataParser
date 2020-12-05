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

## Contact
If you want to contact me you can reach me at [kasra.azizbaigi@gmail.com](mailto:kasra.azizbaigi@gmail.com)

## License
This project uses the following license: [GNU General Public License v3.0](https://github.com/KasraAz75/LRUCache/blob/main/LICENSE).
