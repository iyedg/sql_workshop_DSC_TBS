#!/usr/bin/env python
"""
Renamer.

Usage:
    renamer move_up <start_number> <end_number>
"""
from pathlib import Path
from pyprojroot import here
from docopt import docopt
from loguru import logger

sections_path = Path(here("sections"))
rmd_files = sections_path.glob("*.Rmd")

if __name__ == "__main__":
    arguments = docopt(__doc__, version = "0.1")
    if arguments["move_up"] is True:
        start_number = int(arguments["<start_number>"])
        end_number = int(arguments["<end_number>"])
        assert end_number > start_number
        for rmd_file in rmd_files:
            try:
                file_index = int(str(rmd_file.name)[:2])
            except Exception:
                logger.warning(f"Skipping {rmd_file.name}")
                continue
            if file_index >= start_number:
                new_file_index = file_index + (end_number - start_number)
                logger.debug(new_file_index)
                new_path = str(rmd_file).replace(str(file_index).rjust(2, "0"), str(new_file_index).rjust(2, "0"))
                rmd_file.replace(new_path)
                logger.debug(new_path)
    else:
        print(arguments)
