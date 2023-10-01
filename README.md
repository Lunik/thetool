# GetTool

This script is used to download and install tools from the internet. It is designed to be used with Linux, but it can be used with any operating system that has Python installed.

## Installation

To install GetTool, run the following command:

```bash
python3 -m pip install gettool
```

## Usage

To use GetTool, run the following command:

```bash
gettool install <tool>
```

To uninstall a tool, run the following command:

```bash
gettool uninstall <tool>
```

To see a list of available tools, run the following command:

```bash
gettool list
```

To see the list and version of installed tools, run the following command:

```bash
gettool list --installed
```

To get information about a tool, run the following command:

```bash
gettool info <tool>
```

To update GetTool, run the following command:

```bash
gettool update
```

To upgrade a tool, run the following command:

```bash
gettool upgrade <tool>
```

To upgrade all tools, run the following command:

```bash
gettool upgrade --all
```

To clean up the cache, run the following command:

```bash
gettool clean
```

## Database

GetTool uses a database to store information about tools. The database is stored in another GitHub repository, [GetTool-Database](https://github.com/Lunik/gettool_database)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
