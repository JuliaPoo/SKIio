# SKIio

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


## Order of I/O Operations

`i` and `o` are combinators with side effects. If the _SKIio_
interpreter assumes they are pure functions, these combinators might be
evaluated more than once/out of order.

Order of I/O operations are hence guaranteed by the interpreter. The interpreter
performs lazy evaluation from left to right. Hence the following prints `Hey`,
since the expression on the left is evaluated first.

```clojure
; ATOM_OUT(.H)(ATOM_OUT(.e))(ATOM_OUT(.y))
o(
    ; H
    S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(I))(S(S(K(S))(K))(I)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(I))))
(o(
    ; e
    S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(I)))
)
(o(
    ; y
    S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I))))(I))
)
```

Another way to guarantee order of I/O operations is via "data dependency": Feed
the output of one I/O combinators into another to ensure that one is called after another. E.g.

```clojure
o(i(K(I)))
```

Since `o` requires the output of `i` in order to evaluate, `o`
is guaranteed to execute after `i`.

Similarly, to guarantee that `o` is never evaluated more than
once, ensure that its output is not fed and evaluated multiple times.
E.g.

```clojure
;[x: x(x)](ATOM_OUT(.Q))
S(I)(I)(o(
    ; Q
    S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(I)))
))
```

Would print `QQ`:

```bash
> python -m skiio r -i uwu.ski
---- PROGRAM START ----
QQ
----- PROGRAM END -----
[*] Return: I
```

If only printing `Q` is intended, the above should be rewritten as:

```clojure
;ATOM_OUT(.A)(
;    [x: x(x)(x)](ATOM_I)
;)

o(
    ; Q
    S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(I)))
)(S(S(I)(I))(I)(I))
```

This "multiple evaluations" problem does not occur for `i`
as `i` requires the index into the user input buffer as argument.
It hence behaves more like a pure function without side effects (other
than halting the program execution).

A similar trick can be done for `o` so that it behaves more like
a pure function (e.g. `o(x)(idx)`, where `idx` specifies the order
of prints), but it makes using `o` a lot more clunkier. I hence
decided to stick with this current implementation.