import argparse
import gzip
import json
import random
from typing import Iterator, Optional, Tuple

import bs4

from schema import PageAnnotation
from annotate import annotate


def run(sample_rate: float = 1.0) -> None:
    """
    run reads an ndjson encoded sequence of {url response} and writes an ndjson
    encoded sequence of (url, PageAnnotation) pairs.
    """
    with open("output.ndjson", "w") as output_file:
        for (url, pa) in annotate_input("input.ndjson.gz", sample_rate):
            json.dump(
                {"url": url, "PageAnnotation": pa.to_dict() if pa else None},
                output_file,
            )
            output_file.write("\n")


def annotate_input(
    input_filename: str, sample_rate: float
) -> Iterator[Tuple[str, Optional[PageAnnotation]]]:
    with gzip.open(input_filename) as input_file:
        index = 0
        for line in input_file:
            if sample_rate == 1.0 or random.uniform(0, 1) < sample_rate:
                d = json.loads(line)
                url, body = d["url"], d["response"]
                yield (url, annotate(url, bs4.BeautifulSoup(body, "lxml"), body))
            index += 1


def restricted_float(x: str) -> float:
    try:
        parsed = float(x)
    except ValueError:
        raise argparse.ArgumentTypeError("Sample rate is not a floating-point literal")

    if parsed <= 0.0 or parsed > 1.0:
        raise argparse.ArgumentTypeError("Sample rate must be in range (0.0, 1.0]")
    return parsed


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument(
        "-r",
        type=restricted_float,
        dest="sample_rate",
        default=1.0,
        help="rate at which to sample input docs (by default includes all docs)",
    )

    args = p.parse_args()
    run(args.sample_rate)
