# Disk-Space-Analyser
Python script to analyse your disk space and save the information to a CSV file.

`Incase of large file size, the program might take time to get fully executed.`

## 🛠 Installation

Use the package manager [pip3](https://pip.pypa.io/en/stable/) to install the libraries used first.

```bash
pip3 install package_name
```
### Packages Used

1. sys module

2. os module

3. pandas module

## Usage

Incase of default home directory
```python
./main.py
```

Incase of command line passed directory path
```python
./main.py directory_path
```

## Final Result

```
A CSV file in the same directory with Folder name and Disk space used as columns.
```
### ```Time to run for large file size due to indepth recursion will increase linearly.```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[GPL-3.0 License](https://choosealicense.com/licenses/mit/)

### Star the Repo in case you liked it :)

### © [kehsihba19](https://bit.ly/kehsihba19)
