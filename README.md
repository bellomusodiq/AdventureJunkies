# Writing an annotator

## Suggested Workflow

- Edit the `annotate.py` file.
  In particular, fill in the `annotate()` function  which takes three arguments:
  1. `url`: The URL of the page to annotate
  2. `soup`: The parsed representation of the contents of the page (a `bs4.BeautifulSoup` object).
  And returns either `None` (if no information can be extracted from the page) or a `PageAnnotation`
  object which has the fields requested.
  3. `raw_body`: The raw html of the page to annotate. `soup` should be enough for most of the cases. 

- Run the program with:

  ```sh
  python main.py
  ```

- If this succeeds, view statistics on the output using:
  
  ```sh
  # On Mac
  verify.mac metrics --pa=output.ndjson
  # On Linux
  verify.linux metrics --pa=output.ndjson
  ```

## Optional, but Recommended: Inspecting the inputs

- The `jq` command-line tool is useful for inspecting the inputs and outputs.
  For example:

  ```sh
  # List out the URLs in the input
  gzcat ./input.ndjson.gz | jq -r '.url'
  # Extract the HTML/body for a single URL in the input
  gzcat ./input.ndjson.gz | 
    jq '. | select(.url|test("https://url-i-am-interested-in.com"))' |
    jq -r '.response'
  ```

  If you save these files locally & open within your browser make sure to *disable Javascript* in order to see only the raw page. To do this:
  - Open Dev Tools
  - ctrl+shift+P and search for Javascript
  - See option to Disable Javascript and select it

## List of files

- `annotate.py`: This is the only file you should edit.
- `main.py`: The driver program
- `schema.py`: Defines the schema of the output of the `annotate` function
- Verification tools:
  - `verify.mac` for MacOS
  - `verify.linux` for Linux
  These are command-line tools to help verify the output.