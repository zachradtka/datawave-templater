# Datawave Templater

This is a docker application that generates config files from templates.

## Requirements

The directory structure containing the templates and the configuration to use during templating is as follows:

```
data
+-- templates
|   +-- *.j2
+-- config.json

```

All templates should be under the directory named `template` and must end with the extension `.j2`. The configuration file should be named `cofig.json`, in the parent of the `template` directory, and be of JSON format.

## Building

To build the docker image, run the following command suppling a value for `<tag>`:

```
docker build -t <tag> .
```

## Running

To generate config files, run the following command supplying the same value for `<tag>` (as previously defined) and the path to the directory containing the templates and config.

```
docker run --rm -v $(pwd)/data:/data <tag> /data/templates /data/output
```
