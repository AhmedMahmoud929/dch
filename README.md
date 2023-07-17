# ✨ Domain Checker (DCH) ✨

Domain Checker is a command-line tool written in Python that allows you to check the status of multiple domains at once. It sends HTTP requests to each domain and displays the response status code along with additional information.

## ✅ Features

- ✅ Check the status of multiple domains by providing a file containing the list of domains.
- ✅ Supports various status codes such as 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, and 500 Internal Server Error.
- ✅ Customizable timeout for each request.
- ✅ Option to display only live domains (status code 200 OK).
- ✅ Option to save the results to an output file.
- ✅ Specify custom User-Agent and headers for the HTTP requests.
- ✅ Follow redirects option to allow following HTTP redirects.
- ✅ Verbose output to display detailed information about each request.

## 🚀 Installation

1. Clone the repository or download the source code.
2. Make sure you have Python 3 installed on your system.
3. Install the required dependencies by running the following command:

```pip install -r requirements.txt```

## 💡 Usage

```python dch.py -i input.txt [OPTIONS]```


### Options

- `-i, --input`: Specifies the input file path containing the list of domains. **(required)**
- `-t, --timeout`: Sets the timeout for each request in seconds. Default is 5.0 seconds.
- `-l, --live`: Only displays live domains (status code 200 OK).
- `-o, --output`: Specifies the output file path to save the results.
- `-ua, --user-agent`: Sets the custom User-Agent header value.
- `-ch, --custom-header`: Sets a custom header in the format "Name: Value".
- `-v, --verbose`: Enables verbose output, providing more detailed information about each request.

### Example

Check the status of domains listed in `input.txt`, display only live domains, and save the results to `output.txt`:

```python dch.py -i input.txt -l -o output.txt```


## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙌 Acknowledgments

This tool was developed using Python and the following open-source libraries:
- requests
- urllib.parse
- colorama

## 🤝 Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## 📧 Contact

For any inquiries or questions, please contact Alrba2003@gmail.com

