# "Random" Password Generator

## How it Works
This script generates pseudo random password using Python's native 'random' module. As the official [python documentation](https://docs.python.org/3/library/random.html#:~:text=The%20pseudo-random%20generators%20of%20this%20module%20should%20not%20be%20used%20for%20security%20purposes.) says, DO NOT use this forsecurity purposes. 

That being said I would like to remake this or tweak it to use python's native 'secret' module so that passwords generated would be cryptographically secure.

You can choose the length of your password and what you want to include in your password (Upper and lower case letters, or both, numbers, symbols, or all of them).

The "password" function in password_generator.py accepts string arguments, which can be hardcoded (like in program.py at the moment) or can be the users input (these are commented out in program.py at the moment).

## Example Passwords Generated

I generated a million password just for fun, here are some of them. This took about a minute and some change and wasn't all that CPU intensive, the highest my CPU spiked to was 46%.

```
S$7h99bo&
&ycF$0_-Ru]d7kR81
KrwCF,<-
w]~]'.F?LY:v
`,Jmh[h=hq7GEk|052th
8%2;FvfKspR~Bj9Vv
St-:.K5?bW2Ax8#ZY
0F/7UV2S3:[fIV;LZQ?*X
3mpEdB6L*Q7LnNg
a)V&o)X{3,3
```