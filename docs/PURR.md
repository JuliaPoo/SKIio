# Purr

_Purr_ is a minimalistic untyped functional language.
It exists as a way to write large lambda expressions.
Here's what it looks like:

```clojure
; Z Combinator
#zcom
[f:[g:f(g(g))]([g:f([y:g(g)(y)])])]
~

; inc(a) computes a+1
#inc
[n:[f:[x:f(n(f)(x))]]]
~

; Main program
; Repeat forever: Read and print a byte of user input
!
zcom([f:
    [index:
        ATOM_OUT(ATOM_IN(index)) ; Print input byte at index
        (f(inc(index)))
    ]
])(.00)
~
```

There is no interpreter for _Purr_ itself, it is to be
compiled into _SKIio_ before being interpreted.

## Comments

```clojure
; A semicolon denotes a comment
; All content after a `;` in the same line is ignored
```

## Reserved keywords

- `ATOM_OUT`: The `o` combinator
    - `ATOM_OUT(x)` prints the church encoded integer `x` as a char (utf-8) and returns `ATOM_I`
- `ATOM_IN`: The `i` combinator
    - `ATOM_IN(x)`  returns the church encoded integer of a byte (utf-8) of input at index `x`, where `x` is a church encoded integer. If `x` is beyond what has been read, it pauses program execution and waits for more user input.
- `ATOM_S`: The `S` combinator `[x:[y:[z:x(z)(y(z))]]]`
- `ATOM_K`: The `K` combinator `[x:[y:x]]`
- `ATOM_I`: The identity combinator `I`: `[x:x]`


## Lambda Expressions

`[x:y]` denotes a function with input `x` and output `y`.
E.g. `[x:x]` is the identity function

You can call lambda expressions with `(argument)`.
E.g. `[x:x](a)` is equivalent to `a`

## Main Function Declaration

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

## Macro Declaration

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

### Macro Order

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

## Built-in Church Encodings

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

## Order of I/O Operations

`ATOM_IN` and `ATOM_OUT` are combinators with side effects. If the _SKIio_
interpreter assumes they are pure functions, these combinators might be
evaluated more than once/out of order.

Order of I/O operations are hence guaranteed by the interpreter. The interpreter
performs lazy evaluation from left to right. Hence the following prints `Hey`,
since the expression on the left is evaluated first.

```clojure
[o: ; Shortform
    o(.H)(o(.e))(o(.y))
](ATOM_OUT)
```

Another way to guarantee order of I/O operations is via "data dependency": Feed
the output of one I/O combinators into another to ensure that one is called after another. E.g.

```clojure
ATOM_OUT(
    ATOM_IN(.00)
)
```

Since `ATOM_OUT` requires the output of `ATOM_IN` in order to evaluate, `ATOM_OUT`
is guaranteed to execute after `ATOM_IN`.

Similarly, to guarantee that `ATOM_OUT` is never evaluated more than
once, ensure that its output is not fed and evaluated multiple times.
E.g.

```clojure
!
[x:
    x(x)(x)
](ATOM_OUT(.A))
~
```

Would print `AAA`:

```bash
> python -m skiio r -i uwu.ski
---- PROGRAM START ----
AAA
----- PROGRAM END -----
[*] Return: I
```

If only printing `A` is intended, the above should be rewritten as:

```clojure
!
ATOM_OUT(.A)(
    [x:
        x(x)(x)
    ](ATOM_I)
)
~
```

This "multiple evaluations" problem does not occur for `ATOM_IN`
as `ATOM_IN` requires the index into the user input buffer as argument.
It hence behaves more like a pure function without side effects (other
than halting the program execution).

A similar trick can be done for `ATOM_OUT` so that it behaves more like
a pure function (e.g. `ATOM_OUT(x)(idx)`, where `idx` specifies the order
of prints), but it makes using `ATOM_OUT` a lot more clunkier. I hence
decided to stick with this current implementation.