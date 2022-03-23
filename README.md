# SKIio

This repository implements an interpreter for _SKIio_ and a compiler from a higher level language _Purr_ to _SKIio_. A description of _Purr_ can be found below.

_SKIio_ is a programming language that's an extension of [SKI Combinator Calculus](https://en.wikipedia.org/wiki/SKI_combinator_calculus). Here's what it looks like:

```clojure
; Repeat forever: Read and print a byte of user input
S(K(S(S(S)(K(S(K(S(K(S(S(K(o))(i))))))(S(K(S(S)(K(K))))(S(K(K))(S(K(S(S)))(K)))))))(K(S(S(K(S))(K))))))(S(K(K))(S(S)(K(K(K(I))))))(S(S(K(S(S)(K(S(I)(I)))))(K))(S(K(S(S)(K(S(I)(I)))))(K)))
```

_SKIio_ consists of 5 combinators: `S`, `K`, `I`, as defined in the original SKI Combinator Calculus, and `i` and `o`, which does input and output.

- `i(x)`: Reads a byte of input at index `x`
    - `x` is a church encoded integer
    - Returns a church encoded integer
- `o(x)`: Prints the byte `x`
    - `x` is a church encoded integer
    - Returns `I`.

E.g. The program `o(i)` reads a byte of user input and prints it.

For more information about how _SKIio_ and _Purr_ is implemented, see [DETAILS.md](https://github.com/JuliaPoo/SKIio/DETAILS.md)

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

Examples can be found in the [examples](https://github.com/JuliaPoo/SKIio/examples) folder

- [Echo Server](https://github.com/JuliaPoo/SKIio/examples/echo-server.ski)
- [Hello World](https://github.com/JuliaPoo/SKIio/examples/hello-world.ski)
- [Fizz Buzz](https://github.com/JuliaPoo/SKIio/examples/fizz-buzz.ski)

## Purr

_Purr_ is a minimalistic untyped functional language.
It exists as a way to scalably write large lambda expressions.

There is no interpreter for _Purr_ itself, it is to be
compiled into _SKIio_ before being interpreted.

### Comments

```clojure
; A semicolon denotes a comment
; All content after a `;` in the same line is ignored
```

### Reserved keywords

- `ATOM_OUT`: The `o` combinator
    - `ATOM_OUT(x)` prints the church encoded integer `x` as a char (utf-8) and returns `ATOM_I`
- `ATOM_IN`: The `i` combinator
    - `ATOM_IN(x)`  returns the church encoded integer of a byte (utf-8) of input at index `x`, where `x` is a church encoded integer. If `x` is beyond what has been read, it pauses program execution and waits for more user input.
- `ATOM_S`: The `S` combinator `[x:[y:[z:x(z)(y(z))]]]`
- `ATOM_K`: The `K` combinator `[x:[y:x]]`
- `ATOM_I`: The identity combinator `I`: `[x:x]`


### Lambda Expressions

`[x:y]` denotes a function with input `x` and output `y`.
E.g. `[x:x]` is the identity function

You can call lambda expressions with `(argument)`.
E.g. `[x:x](a)` is equivalent to `a`

### Main Function Declaration

The _Main Function_ will be the "entrypoint" of the program.
This function is the only function called by the interpreter.

```clojure
!
<lambda expression>
~
```

E.g:

```clojure
; Main program
!
ATOM_OUT(ATOM_IN(.00)) ; Main program reads and prints one byte of user input
~
```

### Macro Declaration

You can declare other macros to be called elsewhere.
Macro names cannot be a reserved keyword.

```clojure
#<function name>
<lambda expression>
~
```

E.g:

```clojure
; Prints a char
#WRITE_CHAR
[char: ATOM_OUT(char)]
~

; Main program
!
WRITE_CHAR(ATOM_IN(I)) ; Prints one byte of user input
~
```

#### Macro Order

Macros are not allowed to call itself, and macros cannot be recursive.
E.g. The following are not valid:

```clojure
#self_reference
self_reference() ; No recursive macros!
~
```

```clojure
#defined_before
defined_after(I)
~

#defined_after
defined_before(I) ; Calling a macro that called itself (loop!)
~
```

### Built-in Church Encodings

If would be extremely clunky to write church encodings of integers you need.
Say if you need the number `5`, you'd have to write `[f:[x:f(f(f(f(f(x)))))]]`.

To shorten this, you can refer to the church encoding of `5` as `.05`, where `05`
refers to the hex of `5`. Similarly `100 => .64`, `16 => .0f`. The hex has to be
2 characters wide and padded with `0`, so `16 => .f` is invalid. As a result, you
can't represent a number `n < 0` or `n > 255` with this.

Furthermore, to refer to the church encoding ascii char `H`, one can also do `.H`,
which is equivalent to doing `.48`. This option is available for the following set
of characters:

```
0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
```