# Indentation

[PEP8](https://peps.python.org/pep-0008/#indentation)

Use 4 spaces per indentation level.

Continuation lines should align wrapped elements either vertically using Python’s implicit line joining inside parentheses, brackets and braces, or using a hanging indent. `When using a hanging indent the following should be considered; there should be no arguments on the first line and further indentation should be used to clearly distinguish itself as a continuation line`:

## Correct

Aligned with opening delimiter.

```python
foo = long_function_name(var_one, var_two,
                         var_three, var_four)
```

Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.

```python
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
```

Hanging indents should add a level.

```python
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
```

## Wrong

Arguments on first line forbidden when not using vertical alignment.

```python
foo = long_function_name(var_one, var_two,
    var_three, var_four)
```

Further indentation required as indentation is not distinguishable.

```python
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)
```

The closing brace/bracket/parenthesis on multiline constructs may either line up under the first non-whitespace character of the last line of list, as in:

```python
my_list = [
    1, 2, 3,
    4, 5, 6,
    ]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
    )
```

or it may be lined up under the first character of the line that starts the multiline construct, as in:

```python
my_list = [
    1, 2, 3,
    4, 5, 6,
]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)
```
