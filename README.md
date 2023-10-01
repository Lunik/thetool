# thetool

This script is used to download and install tools from the internet. It is designed to be used with Linux, but it can be used with any operating system that has Python installed.

## Installation

To install thetool, run the following command:

```bash
python3 -m pip install thetool
```

## Usage

To use thetool, run the following command:

```bash
thetool install <tool>
```

To uninstall a tool, run the following command:

```bash
thetool uninstall <tool>
```

To see a list of available tools, run the following command:

```bash
thetool list
```

To see the list and version of installed tools, run the following command:

```bash
thetool list --installed
```

To get information about a tool, run the following command:

```bash
thetool info <tool>
```

To update thetool, run the following command:

```bash
thetool update
```

To upgrade a tool, run the following command:

```bash
thetool upgrade <tool>
```

To upgrade all tools, run the following command:

```bash
thetool upgrade --all
```

To clean up the cache, run the following command:

```bash
thetool clean
```

## Database

thetool uses a database to store information about tools. The database is stored in another GitHub repository, [thetool-Database](https://github.com/Lunik/thetool_database)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
