# hpccout Extracter
A set of simple Python scripts that simplify getting interesting data from [HPC Challenge](https://icl.utk.edu/hpcc/) tests.
## Tutorial
### Configuration
A main config file is `config.yaml`. You can specify there input and output files:
#### Input
 - `hpccout` - a name of a file with output from hpccout or logs from the console; multiple `hpcc` runs are supported and read,
 - `metrics` - a name of a file with metrics whose values will be read and exported to `.csv`,
 #### Output
 - `extract_to` - a name of a `.csv` file to which the metrics' values will be extracted. This may be an absolute path with the filename in your file system. Pay attention to the slashes as they may be different depending on the shell and OS.

 ### Running
 Simply type: `python hpccoutExtracter.py`. The output will be saved to specified file and directory.
