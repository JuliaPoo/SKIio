# SKIio

This repository implements an interpreter for _SKIio_ and a compiler from a higher level language _Purr_ to _SKIio_. A description of _Purr_ can be found below.

_SKIio_ is an extremely minimal programming language that's an extension of [SKI Combinator Calculus](https://en.wikipedia.org/wiki/SKI_combinator_calculus) for I/O. Here's what it looks like:

```clojure
; Repeat forever: Read and print a byte of user input
S(K(S(S(S)(K(S(K(S(K(S(S(K(o))(i))))))(S(K(S(S)(K(K))))
(S(K(K))(S(K(S(S)))(K)))))))(K(S(S(K(S))(K))))))(S(K(K)
)(S(S)(K(K(K(I))))))(S(S(K(S(S)(K(S(I)(I)))))(K))(S(K(S
(S)(K(S(I)(I)))))(K)))
```

_SKIio_ consists of 5 combinators: `S`, `K`, `I`, as defined in the original SKI Combinator Calculus, and `i` and `o`, which does input and output.

- `i(x)`: Reads a byte of input at index `x`
    - `x` is a church encoded integer
    - Returns a church encoded integer
- `o(x)`: Prints the byte `x`
    - `x` is a church encoded integer
    - Returns `I`.

E.g. The program `o(i(K(I)))` reads a byte of user input and prints it.

To see the _Purr_ spec read [PURR.md](https://github.com/JuliaPoo/SKIio/tree/main/docs/PURR.md).

To see the _SKIio_ spec read [SKIIO.md](https://github.com/JuliaPoo/SKIio/tree/main/docs/SKIIO.md)

For more information about how _SKIio_ and _Purr_ is implemented, see [DETAILS.md](https://github.com/JuliaPoo/SKIio/tree/main/docs/DETAILS.md)

## Quickstart

### Installation

```
pip install skiio
```

### Running

You could write an _SKIio_ program in a file, say `test.ski`, and run it with:

```
python -m skiio run -i test.ski
```

You could also write a _Purr_ program in a file, say `test.purr`, and compile it:

```
python -m skiio compile -i test.purr -o test
python -m skiio run -i test.ski
```

More options (e.g. optimizations, debugging) can be found with

```
python -m skiio -h
```

Full usage:

```
usage: SKIio [-h] {compile,c,run,r} ...

SKIio interpreter and compiler, command-line interface

positional arguments:
  {compile,c,run,r}  Action
    compile (c)      Compile Purr code
    run (r)          Run SKIio code

optional arguments:
  -h, --help         show this help message and exit  


usage: SKIio {compile, c} [-h] -i INFILE -o OUTFILE [-opt OPTIMIZE] [-m INTERMEDIATE]

optional arguments:
  -h, --help            show this help message and exit
  -i INFILE, --infile INFILE
                        Input filename with Purr code
  -o OUTFILE, --outfile OUTFILE
                        Output filename (without extension)
  -opt OPTIMIZE, --optimize OPTIMIZE
                        Toggle off optimization (default: True)
  -m INTERMEDIATE, --intermediate INTERMEDIATE
                        Output intermediate representation (default: False)     

usage: SKIio {run, r} [-h] -i INFILE [-v] [-vv]

optional arguments:
  -h, --help            show this help message and exit
  -i INFILE, --infile INFILE
                        Input filename with SKIio code
  -v, --verbose         Prints debugging info (default: None)
  -vv, --veryverbose    Steps through execution (default: None)
```

## Examples

Examples can be found in the [examples](https://github.com/JuliaPoo/SKIio/tree/main/examples) folder

Purr:
- [Echo Server](https://github.com/JuliaPoo/SKIio/tree/main/examples/echo-server.purr)
- [Hello World](https://github.com/JuliaPoo/SKIio/tree/main/examples/hello-world.purr)
- [Fizz Buzz](https://github.com/JuliaPoo/SKIio/tree/main/examples/fizz-buzz.purr)
- [Rot Strings](https://github.com/JuliaPoo/SKIio/tree/main/examples/rot-strings.purr)

SKIio:
- [Echo Server](https://github.com/JuliaPoo/SKIio/tree/main/examples/echo-server.ski)
- [Hello World](https://github.com/JuliaPoo/SKIio/tree/main/examples/hello-world.ski)
- [Fizz Buzz](https://github.com/JuliaPoo/SKIio/tree/main/examples/fizz-buzz.ski)
- [Rot Strings](https://github.com/JuliaPoo/SKIio/tree/main/examples/rot-strings.ski)