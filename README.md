# SKIio

## Workflow

[About Purr -> SKIio and running SKIio]

## Purr Spec

_Purr_ is a minimalistic untyped functional language.
It exists as a way to scalably write large lambda expressions.

There is no interpreter for _Purr_ itself, it is to be
compiled into _SKIio_ before being interpreted.

### Comments

```lisp
; A semicolon denotes a comment
; All content after a `;` in the same line is ignored
```

### Reserved keywords

- `ATOM_OUT`: The `o` combinator
    - `ATOM_OUT(x)` prints the church encoded integer `x` as a char (utf-8) and returns `ATOM_I`
- `ATOM_IN`: The `i` combinator
    - `ATOM_IN(x)` discards `x` (without evaluating), reads one byte of user input and returns the church encoded integer of the byte (utf-8)
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

```lisp
!
<lambda expression>
~
```

E.g:

```lisp
; Main program
!
ATOM_OUT(ATOM_IN(I)) ; Main program reads and prints one byte of user input
~
```

### Macro Declaration

You can declare other macros to be called elsewhere.
Macro names cannot be a reserved keyword.

```lisp
#<function name>
<lambda expression>
~
```

E.g:

```lisp
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

```lisp
#self_reference
self_reference() ; No recursive macros!
~
```

```lisp
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