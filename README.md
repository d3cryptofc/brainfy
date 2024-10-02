<p align="center">
  <img title="Fun fact: the sketch for this art cost me R$100. I know, it's sad." align="center" width="170" src="https://svgur.com/i/1B3H.svg"/><br><br>
  Amazing interpreter for the esoteric language brainf*ck written in Python.
</p>

<p align="center">
  <a href="https://pypi.org/project/brainfupy"><img src="https://img.shields.io/badge/v0.1.0-282C34?style=flat-square"></a>
  <a href="https://pypi.org/project/brainfupy"><img src="https://img.shields.io/badge/Python 3.8 | 3.9 | 3.10 | 3.11 | 3.12-282C34?style=flat-square"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/MIT%20License-282C34?style=flat-square"></a>
</p>

#### 🧩 Code Example: `main.bf`
```python
# Increase decimal value two times, contains decimal 2.
++

# Increase decimal value more 68 times, now contains 70, equivalent to 'F' letter.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# This dot print the decimal number as ASCII letter.
.

# I am tired of this address space, I'm going to next because the decimal number is 0.
>

# Ok, on second thought, I would like to back..
<

# I will use a loop to decrease until it reaches 0.
[-]
```

---

#### ⚙️ Command Usage

```
usage: brainfy [-h] FILE

An amazing interpreter for the esoteric language brainf*ck written in Python.

positional arguments:
  FILE        read BF script instructions from file

optional arguments:
  -h, --help  show this help message and exit
```

#### 🌟 Currently Available Tokens

| Token           | Description                                                   |
|:---------------:|---------------------------------------------------------------|
| **#**           | Create safe comments (isn't multiline).                       |
| **.**           | Print current decimal value as ASCII.                         |
| **+**           | Increase +1 to current decimal value.                         |
| **-**           | Decrease -1 to current decimal value.                         |
| **>**           | Move pointer to next address space.                           |
| **<**           | Move pointer to previous address space.                       |
| **[**`EXP`**]** | Repeat given expression while current decimal value is not 0. |


#### ❤️ Contribute

Do you have any ideas? open an issue or make a pull request. You are welcome!