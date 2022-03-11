#!/usr/local/bin/python

import sys
import json

from pathlib import Path, PurePath
from jinja2 import Environment, select_autoescape, FileSystemLoader


def main():
    """Generate configs from templates"""

    if len(sys.argv) != 3:
        print('ERROR: missing required arguments <template_path> <output_path>')
        sys.exit(1)

    template_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    # output_path.
    print(template_path.parent)
    config_file = Path(template_path.parent, 'config.json')

    with config_file.open('r') as f:
        config = json.load(f)

    env = Environment(
        loader=FileSystemLoader(template_path.as_posix()),
        autoescape=select_autoescape()
    )

    # Get output directory and create it if it doesn't exist
    if not output_path.exists():
        print('Creating output directory: ' + output_path.as_posix())
        output_path.mkdir()

    # Get a list of the templates
    template_files = env.list_templates(extensions='j2')

    if not template_files:
        print('ERROR: No template files found in "' + template_path + '"')
        sys.exit(1)

    for file in template_files:
        print('Found template: ' + file)

        # Get the template file
        template = env.get_template(file)

        output_file = Path(PurePath(output_path, PurePath(file).stem))
        print('Creating file: ' + output_file.as_posix())
        with output_file.open('w') as ofp:
            # Write the template out to a file
            ofp.write(template.render(config))


if __name__ == '__main__':
    main()
