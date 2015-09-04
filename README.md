# logsimple

### A dirt simple package for Python logging

There are a lot of different packages out there for logging in Python. Many of them are very good. Very few of them are simple.

My long-time favorites, [coloredlogs](https://coloredlogs.readthedocs.io/en/latest/), and [logutils](https://bitbucket.org/vinay.sajip/logutils/) are awesome, but if you follow those links you will find tons of documentation. The loggers that already exist have a lot of features and are probably the right choice for experienced Python programmers. But for inexperienced programmers, something simple will probably work a whole lot better.

logsimple is, well, simple. Instead of having tons of lines for set up, you can just import it and use it right away.

### Installation

logsimple is managed under PyPI, which means all you have to do is type

```
$ sudo pip install logsimple
```

in your terminal and the project directory you're working in will now have access to the logsimple package.

Then in your project code, just import it like this:

```
from logsimple import logger
```

and your're good to go!

### Usage

To use logsimple, wherever you would have normally typed

```
print my_string
```

instead type

```
logger.log(my_string)
```

In the event that you want to add special formatting or color to your logs (if you don't then you don't need this package), all you have to do is pass parameters to ```logger.log()```. You can change the format (bold/underline), color, and highlight of the text.

So a call to ```logger.log()``` with all options would look like:

```
logger.log(my_string, color='r', format='b', highlight='y')
```

This would output ```my_string``` in the color red, with bold formatting, highlighted yellow.

Here are all the options you have for changing the look of your output:

* format:
	* bold:			'b'
	* underlined:	'u'

* color:
	* red: 			'r'
	* green: 		'g'
	* yellow: 		'y'
	* blue:			'b'
	* purple:		'p'
	* cyan:			'c'

* highlight:
	* red: 			'r'
	* green: 		'g'
	* yellow: 		'y'
	* blue:			'b'
	* purple:		'p'
	* cyan:			'c'

### Examples:

```python
logger.log(my_string, color='r')
```
![example](https://raw.githubusercontent.com/jamoque/logsimple/master/examples/color_red.png "Red text")


```python
logger.log(my_string, format='u')
```
![example](https://raw.githubusercontent.com/jamoque/logsimple/master/examples/underline.png "Underlined text")


```python
logger.log(my_string, format='b', highlight='y')
```
![example](https://raw.githubusercontent.com/jamoque/logsimple/master/examples/color_blue-highlight_yellow.png "Blue, highlighted yellow")


```python
logger.log(my_string, format='u', color='c')
```
![example](https://raw.githubusercontent.com/jamoque/logsimple/master/examples/underline-color_cyan.png "Underlined cyan text")


```python
logger.log(my_string, format='b', color='y', highlight='p')
```
![example](https://raw.githubusercontent.com/jamoque/logsimple/master/examples/bold-color_yellow-highlight_purple.png "Bold, yellow, highlighted purple")
