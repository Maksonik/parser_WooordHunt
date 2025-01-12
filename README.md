[![Maintainability](https://api.codeclimate.com/v1/badges/3d3393fea44c81694cf8/maintainability)](https://codeclimate.com/github/Maksonik/parser_WooordHunt/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/3d3393fea44c81694cf8/test_coverage)](https://codeclimate.com/github/Maksonik/parser_WooordHunt/test_coverage)
# Parser WooordHunt

This Python library allows you to fetch detailed descriptions of words from www.wooordhunt.ru.

## Installation

To install the library, use `pip`:

```bash
pip install wooordhunt_parser
```

## Usage

This library fetches the detailed description of a word by providing a URL or the word itself. 

### Example:

```python
import asyncio
from wooordhunt_parser import get_word

# Word URL (e.g., www.wooordhunt.ru/word/get or just 'get')
WORD = "get"

async def main():
    word_description = await get_word(WORD)
    print(word_description)

asyncio.run(main())
```

## License

MIT License