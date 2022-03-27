# _Purr_ -> _SKIio_ Compiler

You could read about how I compiled lambda expressions to `SKI`,
and an optimal-ish way to represent large church integers as SKI
combinators [here](https://juliapoo.github.io/ctf/2022/03/13/ctfsg2022-author-writeup.html#the-making-3).

## Notable Challenges

### Namespaces

Consider the following `[x:[y:x]]`. The 2nd `x` is a reference to
the argument of the outer function. This is rather standard, but
introduces challenges when it comes to renaming variables.

In _Purr_, the _SKIio_ combinator names have different names. E.g.
if you wanna reference the `i` combinator in _SKIio_ in _Purr_, you
write `ATOM_IN`.

When compiling _Purr_ to _SKIio_, we need to rename `ATOM_IN` to `i`.
Your first thought might be a trivial string replace. However, consider
this example:

```clojure
[i:ATOM_IN] => [i:i] ; String replace
```

We have string replaced `ATOM_IN` to `i`, but since `i` is part of
the current namespace, the result is wrong. To deal with this, lets
check if the replacement is in the namespace, and rename the variable
something else:

```clojure
[i:ATOM_IN] 
    => [i:i] ; rename ATOM_IN => i
    => [a:i] ; rename i => a
```

And it works! However, even this isn't enough. Consider:

```clojure
[a:[i:ATOM_IN(a)(i)]] 
    => [a:[i:i(a)(i)]] ; rename ATOM_IN => i
    => [a:[a:a(a)(a)]] ; rename i => a
```

Now it's wrong again! This is because when we renamed `i` with `a`,
we encounter the same problem: `a` is already in the namespace! To
properly due with this, we'd have to _recursively_ rename any conflicting
names.

This substitution funciton is really useful, including performing
[beta_eta_reduce](https://en.wikipedia.org/wiki/Lambda_calculus#%CE%B2-reduction) 
where new variables have to be created occasionally.

# _SKIio_ Interpreter

The _SKIio_ interpreter is a stack machine that (mostly)
evaluates from left to right. The interpreter maintains two stacks,
`ret` and `hold`. There's an additional variable `curr` that stores
the current expression that's being evaluated. I'd go through `ret` first.

`ret` is a stack that contains all the expressions that is yet
to be evaluated. 

[TODO]

### Can't just evaluate everything from left to right

[TODO]

### Designing combinators with side effects

[TODO]